import csv
import web_scrapping

###################
# opening csv file and put it's content into a list of urls
###################
csv_contents = []

with open("resources/furniture stores pages.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        csv_contents.append(row[0])

csv_contents.remove("max(page)")

print(len(csv_contents))

###################
# Fetch HTML content for each URL
###################

html_contents = []

for url in csv_contents:
    html_content = web_scrapping.fetch_html_content(url)
    if html_content:
        html_contents.append(html_content)

print(f"Fetched HTML content from {len(html_contents)} URLs")

