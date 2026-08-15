
import pymupdf  
import shutil
import os
import datetime

# Open PDF
pdf_path = "lattermann-Laurenz_4239646_DLBDSPBDM01_P1_S.pdf"
page_number = 0  # zero-based index (0 = first page)

# Clear image folder
import shutil
shutil.rmtree("images/pdf_images", ignore_errors=True) 
os.makedirs("images/pdf_images", exist_ok=True)

with pymupdf.open(pdf_path) as doc:
    img_count = len(doc)
    for i, page in enumerate(doc): # iterate the document pages
        pix = page.get_pixmap(dpi=300)  # adjust DPI for resolution
        pix.save(f"./images/pdf_images/page{i}.png")

# Get a update timestamp
update_timestamp = datetime.datetime.now()
update_timestamp = update_timestamp.strftime("%d/%m/%Y %H:%M")

# Generate README.md string
base_string = f"""
# LaTeX University Paper Template 
*Updated at: {update_timestamp}*

This repository contains my personal **LaTeX template** for university papers and written assignments.  
It’s designed for clean formatting, academic readability, and easy customization for future projects.

The template is mainly for my own use, but I’ve made it public so others can benefit from it as well.  
You’re welcome to **clone, reuse, or adapt** it for your own studies or reports.

> ⚙️ The template will be updated now and then.

## Features
- Preconfigured page layout and headers
- Section and subsection styling for academic papers
- Built-in support for Arial font, justified text, and 1.5 line spacing
- Ready-to-use structure for title page, requirements, and references

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/l-lattermann/LaTex-Template--Uni-Assignments.git

"""

# Add the image display part
"""Styling:
<p align="center">
  <img src="images/img1.png" width="800"><br>
  <img src="images/img2.png" width="800"><br>
  <img src="images/img3.png" width="800">
</p>
"""

# Add Header
base_string += '# Preview' + '\n'
# Add styling beginning
base_string += '<p align="center">' + '\n'

# Define Path
img_path = 'images/pdf_images'


# Add all images
if img_count < 12:
    for i in range(img_count):
        base_string += f'<img src="{img_path}/page{i}.png" width="800"><br>' + '\n' 
else:
    for i in range(0, 5):
        base_string += f'<img src="{img_path}/page{i}.png" width="800"><br>' + '\n' # Add the first 4
    for i in range(img_count-5, img_count):
        base_string += f'<img src="{img_path}/page{i}.png" width="800"><br>' + '\n'# Add the last 4

# Add style ending
base_string += '</p>' 

# Open and write the files
with open("README.md", "w", encoding="utf-8") as f:
    f.write(base_string)
