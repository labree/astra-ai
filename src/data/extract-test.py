import fandom
from urllib.parse import unquote
import os
import json

# Set the wiki you want to access
fandom.set_wiki("starscape-roblox")

with open('extraction-fail.txt', 'r') as f:
    urls = f.readlines()

# Extract and decode page title from URL
url = urls[0].strip()
page_title = unquote(url.split('wiki/')[-1].strip())

try:
    page = fandom.page(title=page_title)
    print(f"Successfully found page: {page.title}")
    print(f"URL: {page.url}")
    print(f"Summary: {page.summary}")
    print(f"\nContent structure: {page.content}")
except Exception as e:
    print(f"Error: {str(e)}")
    print(f"Error type: {type(e).__name__}")
    # Try searching for the page
    search_results = fandom.search(page_title)
    print(f"\nSearch results for '{page_title}':")
    for result in search_results:
        print(f"- {result}")