import fitz  # PyMuPDF
import sys
import os
import shutil
import pymupdf4llm

def convert_pdf_to_md(pdf_path, output_md_path, assets_dir):
    """
    Converts a PDF to Markdown using pymupdf4llm for better formatting (headers, tables, etc.).
    Extracts images to the specified assets directory.
    Moves the source PDF to a 'done' folder upon completion.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        sys.exit(1)

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    print(f"Processing {pdf_path} (High Quality Mode)...")
    
    # Calculate relative path for assets from the markdown file location
    md_dir = os.path.dirname(output_md_path)
    # pymupdf4llm expects image_path to be where images are written relative to CWD or absolute.
    # We want them in assets_dir.
    
    try:
        # returns markdown string
        md_text = pymupdf4llm.to_markdown(
            pdf_path,
            write_images=True,
            image_path=assets_dir,
            image_format="png"
        )
        
        # Post-processing to clean up text (using the same logic as before for artifact removal)
        import re
        
        # Remove Loop specific print artifacts (e.g. "12/15/25, 12:41 PM Title", URLs)
        # Remove lines looking like timestamps
        md_text = re.sub(r'^\d{1,2}/\d{1,2}/\d{2,4}.*?PM.*?$', '', md_text, flags=re.MULTILINE)
        md_text = re.sub(r'^\d{1,2}/\d{1,2}/\d{2,4}.*?AM.*?$', '', md_text, flags=re.MULTILINE)
        # Remove Lines that are just URLs (often at bottom of pages)
        md_text = re.sub(r'^https://loop\.cloud\.microsoft.*?$', '', md_text, flags=re.MULTILINE)
        # Remove "Add icon Add cover"
        md_text = re.sub(r'^Add icon Add cover$', '', md_text, flags=re.MULTILINE)
        
        # Replace <br> with space
        md_text = md_text.replace("<br>", " ")
        
        # Compress multiple newlines
        md_text = re.sub(r'\n{3,}', '\n\n', md_text)
        
        # Fix image paths. pymupdf4llm writes images to assets_dir, but the links in MD 
        # might be absolute or relative to CWD. We need them relative to the MD file.
        # pymupdf4llm usually creates links like "![image](assets_dir/image.png)" if we pass assets_dir.
        # But if assets_dir is absolute, the link is absolute.
        # We want relative link: "assets/image.png" if md is in parent of assets, OR
        # if md is in "Sales/" and assets is in "5. Documents/assets", we need "../assets/image.png".
        
        # Let's fix the links.
        # 1. Identify where pymupdf4llm thought it was writing vs where MD file lives.
        # The links in md_text will likely be `![...](/absolute/path/to/assets/img.png)`.
        
        def rel_link_repl(match):
            alt_text = match.group(1)
            full_path = match.group(2)
            fname = os.path.basename(full_path)
            
            # Construct relative path from MD file to this image file
            # assets_dir is where the image actually IS.
            # output_md_path is where the MD IS.
            
            # Target image path
            actual_image_path = os.path.join(assets_dir, fname)
            
            # Relative path from MD directory to Image
            rel_path = os.path.relpath(actual_image_path, os.path.dirname(output_md_path))
            
            return f'![{alt_text}]({rel_path})'

        md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', rel_link_repl, md_text)

        # Write Markdown file
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print(f"Successfully converted to {output_md_path}")
        
        # Move processed PDF to 'done' folder
        source_dir = os.path.dirname(pdf_path)
        done_dir = os.path.join(source_dir, "done")
        
        if not os.path.exists(done_dir):
            os.makedirs(done_dir)
            
        filename = os.path.basename(pdf_path)
        destination = os.path.join(done_dir, filename)
        
        try:
            shutil.move(pdf_path, destination)
            print(f"Moved source PDF to {destination}")
        except Exception as e:
            # If move fails (e.g. same filesystem issue), copy then remove? 
            # Or maybe it's already there (overwrite).
            if os.path.exists(destination):
                 print(f"File already exists in done, removing source.")
                 os.remove(pdf_path)
            else:
                print(f"Warning: Could not move PDF to done folder: {e}")

    except Exception as e:
        print(f"Conversion failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python pdf_to_md.py <pdf_path> <output_md_path> <assets_dir>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_md_path = sys.argv[2]
    assets_dir = sys.argv[3]
    
    convert_pdf_to_md(pdf_path, output_md_path, assets_dir)
