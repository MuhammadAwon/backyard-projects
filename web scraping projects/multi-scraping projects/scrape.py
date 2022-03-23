'''Make a program that gets the data from multiple pages of a website and shows the headlines, links and votes
but it should only display the posts who have more than 100 votes sorted by a decending order and then save
the file in to json format'''
# Note: The code is working fine but error('End of File') on opening json file


# import requests, json, time
# from bs4 import BeautifulSoup
# from pprint import pprint as pp


# for i in range(5):  # number of pages plus one
#     url = f'https://news.ycombinator.com/news?p={i}'
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')

#     title = soup.select('.storylink')
#     subtext = soup.select('.subtext')

#     def sort_by_votes(hnlist):
#         return sorted(hnlist, key=lambda k: k['Votes'], reverse=True)

#     def blog_posts(title, subtext):
#         hn = []
#         for idx, item in enumerate(title):
#             post_name = item.get_text()
#             post_link = item.get('href', None)
#             point = subtext[idx].select('.score')

#             if len(point):
#                 votes = point[0].get_text().replace(' points', '')
#                 votes = int(votes.replace(' point', ''))
#                 try:
#                     if votes > 99:
#                         data = {
#                             'News': post_name,
#                             'Link': post_link,
#                             'Votes': votes,
#                         }
#                         hn.append(data)
#                 except Exception:
#                     return 'All links have less than 100votes on this web page'
                # time.sleep(res.elapsed.total_seconds())
#         return sort_by_votes(hn)

#     myfile = blog_posts(title, subtext)

#     with open('data.json', 'a', encoding='utf-8') as f:
#         json.dump(myfile, f, sort_keys=True, ensure_ascii=False, indent=2)
