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
        
        # Extract different types of content with error handling
        content = {
            'title': page.title,
            'url': page.url,
            'summary': page.summary if hasattr(page, 'summary') else '',
            'full_text': '',  # We'll build this manually
            'content_structure': None,  # Will store the raw content structure
            'images': page.images if hasattr(page, 'images') else []
        }

        # Try to get the raw content structure
        try:
            raw_content = page._content  # Access the raw content directly
            content['content_structure'] = raw_content
            
            # Build full text from main content and sections
            full_text_parts = []
            if 'content' in raw_content:
                full_text_parts.append(raw_content['content'])
            
            # Extract text from sections recursively
            def extract_section_text(sections):
                text = []
                for section in sections:
                    if 'content' in section and section['content']:
                        text.append(section['content'])
                    if 'sections' in section:
                        text.extend(extract_section_text(section['sections']))
                return text
            
            if 'sections' in raw_content:
                full_text_parts.extend(extract_section_text(raw_content['sections']))
            
            content['full_text'] = '\n\n'.join(filter(None, full_text_parts))
            
        except (KeyError, AttributeError) as e:
            print(f"Warning: Could not extract content structure: {str(e)}")
            pass

        return content
    except Exception as e:
        print(f"Error extracting {page_title}: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        # Print the full error traceback for debugging
        import traceback
        print(traceback.format_exc())
        return None

# Create pages-extracted directory if it doesn't exist
os.makedirs('pages-extracted', exist_ok=True)

# Read URLs from file
with open('extraction-fail.txt', 'r') as f:
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
