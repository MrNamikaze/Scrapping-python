import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://peraturan.bpk.go.id/Home/Search?filter=1&search=&jenis=8&tema=61'  # Replace with the URL of the website you want to scrape
response = requests.get(
    url='https://peraturan.bpk.go.id/Home/Search?filter=1&search=&jenis=8&tema=61', 
    headers={'User-Agent': 'Mozilla/5.0'}
    )

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract information from the parsed HTML
# Example: Extract all the links on the page
links = soup.find_all("li", attrs={'class':'text-left font-sm'})
# print(links)
for link in links:
    href = link.find("a", attrs={'class':'text-danger'})
    for rem in href:
        print(rem)
    