# Buggy program

# import requests, time
# from bs4 import BeautifulSoup
# from pprint import pprint


# url = 'https://www.skinnytaste.com'
# res = requests.get(url)
# soup = BeautifulSoup(res.content, 'html.parser')

# links = soup.select('article.post.teaser-post') #.odd + .even
# posts = soup.select('.recipe-meta')


# def skinny_content(links, posts):
#     st = []
#     for idx, article in enumerate(links):
#         for name in article.select('h2.title'):
#             title = name.text
#         for summ in article.select('p.excerpt'):
#             description = summ.text
#         for img in article.select('img.lazyload.attachment-teaser.size-teaser.wp-post-image'):
#             image = img.get('data-src')

#         # Not all articles have points
#         item = posts[idx]
#         if len(item):
#             for blue in item.select('.smart-points.blue'):
#                 bp = blue.text
#             for green in item.select('.smart-points.green'):
#                 gp = green.text
#             for purple in item.select('.smart-points.purple'):
#                 pp = purple.text
#             for cal in item.select('.icon-star'):
#                 calories = cal.text.replace('Calories', '')

#         meta = []
#         #Not all articles have icons so get it here
#         div_icon = article.find('div', {"class":"icons"})
#         if div_icon:
#             span_icons = div_icon.findAll('span', recursive=False)
#             for mta in span_icons:
#                 meta.append(mta.find('img').get('alt'))

#         st.append(
#             {
#                 'Title': title,
#                 'Image': image,
#                 'Summary': description,
#                 'Blue points': bp,
#                 'Green points': gp,
#                 'Purple points': pp,
#                 'Calories': calories,
#                 'Recipe Keys':meta,
#             }
#         )

#     return st

# data = skinny_content(links, posts)
# pprint(data)
# pprint(f'{len(data)} articles found......end!')
