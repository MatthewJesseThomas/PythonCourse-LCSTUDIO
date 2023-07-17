import os
import requests
from bs4 import BeautifulSoup
import sys
import csv

# Define the URL of the website you want to scrape
url = 'https://lifechoicesacademy.com/'

# Send an HTTP GET request and retrieve the webpage content
response = requests.get(url)
content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Extract the page title
page_title = soup.title.get_text().encode(sys.stdout.encoding, errors='replace').decode()

# Extract all routes and their corresponding requests
routes_requests = []
for link in soup.find_all('a'):
    route = link.get('href').encode(sys.stdout.encoding, errors='replace').decode(errors='ignore')
    request = link.get_text().encode(sys.stdout.encoding, errors='replace').decode(errors='ignore')
    routes_requests.append({'Route': route, 'Request': request})

# Extract all styles
styles = []
for style in soup.find_all('style'):
    style_content = style.get_text().encode(sys.stdout.encoding, errors='replace').decode(errors='ignore')
    styles.append({'Style': style_content})

# Extract all tables and their data
tables_data = []
for table in soup.find_all('table'):
    table_data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells:
            row_data = [cell.get_text().encode(sys.stdout.encoding, errors='replace').decode(errors='ignore') for cell in cells]
            table_data.append(row_data)
    tables_data.append({'Table': table_data})

# Extract image URLs
image_urls = []
for img in soup.find_all('img'):
    image_url = img.get('src').encode(sys.stdout.encoding, errors='replace').decode(errors='ignore')
    image_urls.append({'Image URL': image_url})

# Extract URLs from CSS stylesheets
stylesheet_urls = []
for link in soup.find_all('link', {'rel': 'stylesheet'}):
    href = link.get('href')
    if href:
        stylesheet_url = href.encode(sys.stdout.encoding, errors='replace').decode(errors='ignore')
        stylesheet_urls.append({'Stylesheet URL': stylesheet_url})

# Get the domain name from the URL
domain = url.split('//')[1].split('/')[0]
folder_name = f'web_scrapped_{domain}'

# Create the folder for the current website
os.makedirs(folder_name, exist_ok=True)


# Function to save scraped information to a CSV file inside the folder
def save_to_csv(data, folder_name, file_name):
    keys = data[0].keys() if data else []
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


# Save scraped information to CSV files inside the folder
save_to_csv([{'Page Title': page_title}], folder_name, 'page_title.csv')
save_to_csv(routes_requests, folder_name, 'routes_requests.csv')
save_to_csv(styles, folder_name, 'styles.csv')
save_to_csv(tables_data, folder_name, 'tables_data.csv')
save_to_csv(image_urls, folder_name, 'image_urls.csv')
save_to_csv(stylesheet_urls, folder_name, 'stylesheet_urls.csv')

print(f"Scraped information has been saved to the '{folder_name}' folder.")
