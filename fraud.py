import requests
from bs4 import BeautifulSoup

def check_fraudulent(url):

    '''Check if a website is fraudulent by analyzing the links on the website.'''

    # Fetch the HTML content of the website using GET request
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        return True

    # Extract all the links from the HTML content
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Check if the website contains any malicious links
    for link in links:
        if 'http' in link and link != url:
            # Fetch the HTML content of the linked website using GET request
            try:
                link_response = requests.get(link)
                link_soup = BeautifulSoup(link_response.text, 'html.parser')
            except:
                continue

            # Check if the linked website is fraudulent
            if check_fraudulent(link):
                return True

    # Return False if no malicious links are found
    return False
