import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
a = 1
for x in range(3):
    jumlah = x+1
    halaman = str(x+1)
    response = requests.get(
    url='https://peraturan.bpk.go.id/Home/Search?filter=1&search=&jenis=8&tema=61&page='+halaman, 
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information from the parsed HTML
    # Example: Extract all the links on the page
    links = soup.find_all("div", attrs={'class':'search-page search-content-4'})
    # print(links)
    for link in links:
        href = link.find_all("span", attrs={'class':'font-blue'})
        href1 = link.find_all("span", attrs={'class':'lead bold'})
        # print(href)
        for rem in href:
            for ran in rem:
                print(ran)
                # marks_data = pd.DataFrame({'ID': {a: ran}})
                # a += 1
        # for rem1 in href1:
        #     ran = rem1.find('a')
        #     for ran1 in ran:
        #         print(ran1)
# file_name = 'C:\\Development\\Scraping python\\MarksData.xlsx'
  
# # saving the excel
# marks_data.to_excel(file_name)
# print('DataFrame is written to Excel File successfully.')