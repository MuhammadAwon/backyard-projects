# A simple working example of web scrapping for basic concepts

import requests, time, csv
import pandas as pd
from bs4 import BeautifulSoup

for page in range(3):
    url = f'https://coreyms.com/page/{page}'
    res = requests.get(url)
    time.sleep(res.elapsed.total_seconds())
    soup = BeautifulSoup(res.text, 'html.parser')

    myfile = open('video.csv', 'a')
    writer = csv.writer(myfile)
    writer.writerow(['Title', 'Summary', 'Link'])

    for content in soup.find_all('article'):
        # print(content)

        # title = content.find(class_='entry-title-link').text
        title = content.h2.a.text

        # summary
        summary = content.find('div', class_='entry-content').p.text

        try:
            video = content.find('iframe', class_='youtube-player')['src']
            vid_id = video.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f'https://www.youtube.com/watch?v={vid_id}'
        except:
            yt_link = None

        writer.writerow([title, summary, yt_link])
    myfile.close()
