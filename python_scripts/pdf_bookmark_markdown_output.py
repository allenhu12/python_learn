import fitz

def get_bookmarks(bookmarks, indent_level=0):
    markdown_content = ""

    for bookmark in bookmarks:
        if isinstance(bookmark, list):
            # Case 1: Bookmark is a list
            level = bookmark[0] # Bookmark level
            title = bookmark[1]
            page_number = bookmark[2]  # Page numbers start from 0, add 1 to start from 1
        elif isinstance(bookmark, dict):
            # Case 2: Bookmark is a dictionary
            title = bookmark["title"]
            page_number = bookmark["page"] + 1  # Page numbers start from 0, add 1 to start from 1
        else:
            # Case 3: Bookmark structure not recognized
            continue

        # Add indentation to represent the hierarchical structure
        indent = "  " * level
        title = title.replace('\r', ' ')

        # Generate the Markdown format for the bookmark
        markdown_content += f"{indent} [{title}](#{page_number})\n"

        # Recursively process child bookmarks
        if "children" in bookmark:
            markdown_content += get_bookmarks(bookmark["children"], indent_level + 1)

    return markdown_content

def pdf_bookmarks_to_markdown(file_path):
    pdf_document = fitz.open(file_path)
    bookmarks = pdf_document.get_toc()

    markdown_content = get_bookmarks(bookmarks)

    return markdown_content

# Usage example
pdf_path = "/Users/hubo/Library/CloudStorage/Nutstore-allenhu12@qq.com/300-LEARN/wireshark参考书/Mastering Wireshark.pdf"  # Replace with the actual path of your PDF file
markdown_content = pdf_bookmarks_to_markdown(pdf_path)
print(markdown_content)
