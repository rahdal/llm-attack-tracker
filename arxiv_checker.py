import requests
import xml.etree.ElementTree as ET
from datetime import datetime

url = 'http://export.arxiv.org/api/query?search_query=ti:llm+AND+ti:attack&sortBy=lastUpdatedDate&sortOrder=descending&max_results=1'

response = requests.get(url)
response = response.text
print(response)

# Parse the XML data
root = ET.fromstring(response)

# Get the entry element
entry = root.find('{http://www.w3.org/2005/Atom}entry')

if entry is not None:
    # Extract the title
    title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
    if title_elem is not None:
        title = title_elem.text
    else:
        title = "No title found"

    # Extract the authors
    authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]

    # Extract the URL
    url_elem = entry.find('{http://www.w3.org/2005/Atom}link[@rel="alternate"]')
    if url_elem is not None:
        url = url_elem.get('href')
    else:
        url = "No URL found"

    # Extract the published date
    published_elem = entry.find('{http://www.w3.org/2005/Atom}published')
    if published_elem is not None:
        published_date = published_elem.text
    else:
        published_date = "No published date found"

    # Print the results
    print("Title:", title)
    print("Authors:", ", ".join(authors))
    print("URL:", url)
    print("Published Date:", published_date)
else:
    print("No entry element found in the XML data")