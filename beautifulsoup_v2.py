""" Scrapping using BeautifulSoup:
    site https://stackoverflow.com/questions/tagged/python:
    search for questions, their summaries and links
    and save this info into the CSV file
"""

from bs4 import BeautifulSoup
import requests
import csv

request = requests.get('https://stackoverflow.com/questions/tagged/python').text
soup = BeautifulSoup(request, "lxml")

csv_file = open('cms_scrape_stackoverflow.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['question', 'href', 'summary'])

questions = soup.find_all('div', class_="question-summary")
# print(len(questions))
for question in questions:
    q_title = question.find('a', class_="question-hyperlink").text
    q_href = question.find('a', class_="question-hyperlink").attrs['href']
    q_href = f"https://stackoverflow.com{q_href}"
    q_text = question.find('div', class_="excerpt").text

    csv_writer.writerow([q_title, q_href, q_text])

csv_file.close()