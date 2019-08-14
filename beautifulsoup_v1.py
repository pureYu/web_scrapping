""" Scrapping using BeautifulSoup:
    site https://coreyms.com:
    search for articles, their titles, summaries and youtube links
    and save this info into the CSV file
"""

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/page/3').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# exit()

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'href', 'summary', 'video'])

for article in soup.find_all('article'):
    art_title = article.h2.a.text
    art_href = article.h2.a.attrs['href']
    art_summary = article.find('div', class_="entry-content").p.text
    try:
        art_video_src = article.iframe.attrs['src']
        art_video_src = art_video_src.split('/')[4]
        art_video_src = art_video_src.split('?')[0]
        art_video_href = f"https://www.youtube.com/watch?v={art_video_src}"
    except Exception as e:
        art_video_href = None

    csv_writer.writerow([art_title, art_href, art_summary, art_video_href])

csv_file.close()


