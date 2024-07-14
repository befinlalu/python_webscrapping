import requests
from bs4 import BeautifulSoup

# Get the URL from the user
url = input("Please enter the URL of the job listings page: ")

# Make a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')
    highlight = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    
    if highlight:
        title = highlight.find('h2').text.strip()
        print(title)
    else:
        print("No job listing found")
else:
    print("Failed to retrieve the webpage")
