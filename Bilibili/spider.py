import requests
import time
import pandas as pd

def get_content(mid, page_size, page_number):
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
        "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid={0}&pagesize={1}&page={2}".format(mid, page_size, page_number)
    r = requests.get(url)
    time.sleep(0.6)
    if r.status_code == 200:
        return r.json()
    return None

def parse_content(mid, page_size, page_number):
    json_data = get_content(mid, page_size, page_number)
    video_data_list = json_data["data"]["vlist"]
    return video_data_list

comments = []
play_num = []
title = []
timestamp = []
#description = []
length = []
video_review = []
favorites = []
video_id = []

def process_data(mid, page_size, page_number):
    video_data_list = parse_content(mid, page_size, page_number)
    for i in video_data_list:
        comments.append(i["comment"])
        play_num.append(i['play'])
        title.append(i['title'])
        timestamp.append(i['created'])
        #description.append(i['description'])
        length.append(i['length'])
        video_review.append(i['video_review'])
        favorites.append(i['favorites'])
        video_id.append(i['aid'])
    data_dict = {
        "comments": comments,
        "play_num": play_num,
        "title": title,
        "timestamp": timestamp,
        #"description": description,
        "length": length,
        "video_review": video_review,
        "favorites": favorites,
        "video_id": video_id
    }
    return data_dict

if __name__ == "__main__":
    mid = str(82366241)
    page_size = 100
    for page_num in range(5):
        data_dict = process_data(mid, page_size, page_num)
        df = pd.DataFrame.from_dict(data_dict)
        df.to_csv("movie_data.csv", index=False)