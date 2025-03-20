import fandom
from urllib.parse import unquote
import os
import json

# Set the wiki you want to access
fandom.set_wiki("starscape-roblox")

def extract_page_content(page_title):
    try:
        # Get the page object
        page = fandom.page(title=page_title)
        
        # Extract different types of content
        content = {
            'title': page.title,
            'url': page.url,
            'summary': page.summary,
            'full_text': page.plain_text,
            'content_structure': page.content,  # Returns structured dict with sections
            'images': page.images  # List of image URLs
        }
        return content
    except Exception as e:
        print(f"Error extracting {page_title}: {e}")
        return None

# Create pages-extracted directory if it doesn't exist
os.makedirs('pages-extracted', exist_ok=True)

# Read URLs from file
with open('fandom_links.txt', 'r') as f:
    urls = f.readlines()

# Process each URL and save to individual files
for url in urls:
    # Extract and decode page title from URL
    page_title = unquote(url.split('wiki/')[-1].strip())
    content = extract_page_content(page_title)
    
    if content:
        # Create filename from page title
        filename = content['title'].lower().replace(' ', '-')
        # Remove any other special characters that might cause issues
        filename = ''.join(c for c in filename if c.isalnum() or c == '-')
        filepath = os.path.join('pages-extracted', f'{filename}.json')
        
        # Save content to JSON file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print(f"Saved {filename}.json")
