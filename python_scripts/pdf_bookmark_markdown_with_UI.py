import tkinter as tk
from tkinter import filedialog
import fitz
import re

def get_bookmarks(bookmarks, indent_level=0):
    markdown_content = ""

    for bookmark in bookmarks:
        if isinstance(bookmark, list):
            # Case 1: Bookmark is a list
            title = bookmark[1]
            page_number = bookmark[0] + 1  # Page numbers start from 0, add 1 to start from 1
        elif isinstance(bookmark, dict):
            # Case 2: Bookmark is a dictionary
            title = bookmark["title"]
            page_number = bookmark["page"] + 1  # Page numbers start from 0, add 1 to start from 1
        else:
            # Case 3: Bookmark structure not recognized
            continue

        # Add indentation to represent the hierarchical structure
        indent = "    " * indent_level

        # Check if the line has numbering format "X." or "X.Y" using regex
        match = re.match(r"^(\d+(\.\d+)*)\.\s(.+)$", title)
        if match:
            numbering = match.group(1)  # Extract the numbering format
            num_segments = numbering.count('.') + 1  # Count the number of segments in the numbering format

            # Generate the Markdown format for the bookmark with appropriate number of hashtags
            markdown_content += f"{indent}- {'#' * (num_segments + indent_level)} {title}(#{page_number})\n"
        else:
            # Generate the Markdown format for the bookmark without any additional hashtags
            markdown_content += f"{indent}- {title}(#{page_number})\n"

        # Recursively process child bookmarks
        if "children" in bookmark:
            markdown_content += get_bookmarks(bookmark["children"], indent_level + 1)

    return markdown_content

def pdf_bookmarks_to_markdown(file_path):
    pdf_document = fitz.open(file_path)
    bookmarks = pdf_document.get_toc()

    markdown_content = get_bookmarks(bookmarks)

    return markdown_content

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select a PDF file using the file dialog
file_path = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF Files", "*.pdf")]
)

# Check if a file was selected
if file_path:
    # Process the selected PDF file
    markdown_content = pdf_bookmarks_to_markdown(file_path)
    print(markdown_content)
else:
    print("No file selected.")

