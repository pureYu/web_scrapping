""" Scrapping using Requests HTML:
    site https://coreyms.com:
    search for articles, their titles, summaries and youtube links
    and save this info into the CSV file
"""

# (web_scrapping_env) $ pip install requests-html

import csv
from requests_html import HTML, HTMLSession


csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
r = session.get('https://coreyms.com')


articles = r.html.find('article')
for article in articles:
    headline = article.find(".entry-title-link", first=True).text
    summary = article.find(".entry-content p", first=True).text
    try:
        vid_src = article.find("iframe", first=True).attrs['src'] # https://www.youtube.com/embed/2Fp1N6dof0Y?version=3&...
        vid_id = vid_src.split('/')[4]  # '2Fp1N6dof0Y?version=3&...
        vid_id = vid_id.split('?')[0]   # 2Fp1N6dof0Y
        yt_link = f'http://youtube.com/watch?v={vid_id}' # http://youtube.com/watch?v=2Fp1N6dof0Y
    except Exception as e:
        yt_link = None
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()










