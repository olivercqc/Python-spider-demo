from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url = "https://m.weibo.cn/api/container/getIndex?"

headers = {
    'Referer': 'https://m.weibo.cn/u/2191344824',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2191344824',
        'containerid': '1076032191344824',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        #print(items)
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

if __name__ == "__main__":
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)