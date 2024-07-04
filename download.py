import requests

filename = 'C:\\Development\\Scraping python\\file.pdf'  # Specify the filename for saving the downloaded file

# Send a GET request to the file URL
response = requests.get(
    url='https://peraturan.bpk.go.id/Home/Download/153567/UU_Nomor_11_Tahun_2020-compressed.pdf',
    headers={'User-Agent': 'Mozilla/5.0'}
    )

# Check if the request was successful (status code 200)
print(response)
if response.status_code == 200:
    # Open a file in binary write mode and write the response content to it
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File '{filename}' downloaded successfully.")
else:
    print("Failed to download the file.")