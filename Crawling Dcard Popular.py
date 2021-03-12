import requests
import json
from bs4 import BeautifulSoup

def printing_Dcard_popular(): # 列印熱門貼文
    global counter_Dcard_popular
    for post_Dcard_popular in posts_Dcard_popular:
        try:
            counter_Dcard_popular += 1
            print("熱門編號 : ", counter_Dcard_popular)
            print("識別編號 : ", post_Dcard_popular['id'])
            print("標題         : ", post_Dcard_popular['title'])
            print("內文         : ", post_Dcard_popular['excerpt'])
            print("按讚         : ", post_Dcard_popular['likeCount'])
            print("回應         : ", post_Dcard_popular['commentCount'])
        except UnicodeEncodeError:
            print("UnicodeEncodeError")

url_Dcard_popular = 'https://www.dcard.tw/_api/posts?popular=true'    # 進入Dcard熱門板面的網址
posts_Dcard_popular = list(requests.get(url_Dcard_popular).json())
counter_Dcard_popular = 0
printing_Dcard_popular()  # 印第1組前30熱門
last_id = posts_Dcard_popular[-1]['id']   # 第1組最後一筆熱門id

page_num = 2
for i in range(page_num):   # 印第2-3組前30熱門
    posts_Dcard_popular = list(requests.get(url_Dcard_popular + '&before=' + str(last_id)).json())
    printing_Dcard_popular()
    last_id = posts_Dcard_popular[-1]['id']   # 第2-3組最後一筆熱門的id

page_num = 3
for i in range(page_num):   # 印第3-4組前30熱門
    posts_Dcard_popular = list(requests.get(url_Dcard_popular + '&before=' + str(last_id)).json())
    printing_Dcard_popular()
    last_id = posts_Dcard_popular[-1]['id']   # 第3-4組最後一筆熱門的id
