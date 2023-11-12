#!/usr/bin/env python3


# Yes I used chatgpt, I normally don't comment that well
import sys
import datetime

def create_markdown_file(title):
    # Get the current date
    current_date = datetime.date.today()
    # Format the date as YYYY-MM-DD
    formatted_date = current_date.strftime("%Y-%m-%d")

    format_title = title.replace(" ", "-").lower()

    # Generate the filename
    filename = f"{formatted_date}-{format_title}.md"

    # Add the front matter content
    front_matter = f"---\nlayout: single\ntitle: {title}\ndate: {formatted_date}\n---\n"

    # Create the file and write the front matter
    with open(filename, "w") as file:
        file.write(front_matter)

    print(f"Markdown file '{filename}' created successfully!")

# Check if the script is run with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python make_post.py <title>")
else:
    title = sys.argv[1]
    create_markdown_file(title)
