import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import uuid

URL = 'http://export.arxiv.org/api/query?search_query=ti:llm+AND+ti:attack&sortBy=lastUpdatedDate&sortOrder=descending'

def get_recent_papers(num_papers:int = 1) -> dict:
    """
    Retrieves the most recent papers related to the topic "llm" and "attack" from the arXiv API.

    Args:
        num_papers (int): The number of recent papers to retrieve. Default is 1.

    Returns:
        dict: A list of dictionaries, where each dictionary represents a paper and contains the following information:
            - 'title': The title of the paper.
            - 'authors': A list of authors of the paper.
            - 'url': The URL of the paper.
            - 'published_date': The published date of the paper.
            - 'id': A unique identifier for the paper.
    """
    response = requests.get(URL)
    response = response.text

    # Parse the XML data
    root = ET.fromstring(response)

    # Get the entry element
    papers = []

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        paper_data = {}

        # Extract the title
        title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
        if title_elem is not None:
            paper_data['title'] = title_elem.text

        # Extract the authors
        authors = []
        for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
            author_name_elem = author.find('{http://www.w3.org/2005/Atom}name')
            if author_name_elem is not None:
                authors.append(author_name_elem.text)
        paper_data['authors'] = authors

        # Extract the URL
        url_elem = entry.find('{http://www.w3.org/2005/Atom}link[@rel="alternate"]')
        if url_elem is not None:
            paper_data['url'] = url_elem.get('href')

        # Extract the published date
        published_elem = entry.find('{http://www.w3.org/2005/Atom}published')
        if published_elem is not None:
            paper_data['published_date'] = published_elem.text

        # Add a unique id
        paper_data['id'] = str(uuid.uuid4())

        papers.append(paper_data)

    return papers

# papers = get_recent_papers(10)
# for paper in papers:
#     print(paper)
