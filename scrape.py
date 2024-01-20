# from bs4 import BeautifulSoup
# import requests
# import csv

# with open("simple.html") as html_file:
# 	soup = BeautifulSoup(html_file, 'lxml')

# # print(soup.prettify()) # string type 

# # match = soup.title.text

# # match = soup.find('div', class_='footer')

# article = soup.find('div',class_='article')

# # print(article)

# headline = article.h2.a.text
# summary = article.p.text

# print(headline, summary)

# for article in soup.find_all('div', class_ ='article'):
# 	headline = article.h2.a.text
# 	summary = article.p.text

# 	print(headline, summary)


# source = requests.get('https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/').text

# soup = BeautifulSoup(source, 'lxml')

# csv_file = open('cms_scrape.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)

#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']

#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None

#     print(yt_link)

#     print()

#     csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()

from bs4 import BeautifulSoup
import requests
import csv
import re
import pandas as pd

source = requests.get('https://www.nytimes.com/').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

csv_file = open('nytimes_scrape.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])

count  = 0
existing_data = set()

for article in soup.find_all('section', class_='story-wrapper'):
    try:
        headline = article.find('div', class_='css-xdandi').p.text.strip()
    except AttributeError:
        headline = None

    try:
        summary = article.find('p', class_=re.compile(r'summary-class css-\w{6,7}')).text.strip()
    except AttributeError:
        summary = None

    if headline and summary:
        row = (headline, summary)

        if row not in existing_data:
            if count > 4 :
                break
            count += 1 
            csv_writer.writerow(list(row))
            existing_data.add(row)

csv_file.close()








