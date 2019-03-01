import requests
import json
import urllib.request

from basic import Basic


class Material(object):
    def __init__(self):
        pass

    def add_new(self, access_Token, news):
        print(news)
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % access_Token
        urlResp = requests.post(postUrl, data=news)
        print(urlResp.text)
        print(postUrl)
        # urlResp = urllib.request.urlopen(postUrl, data=news.encode('utf8'))
        # print(urlResp.read())


if __name__ == '__main__':
    myMaterial = Material()
    # accessToken = Basic().get_access_token()
    accessToken = '19_3NuYtsVv322Zrsg0pa7ZwGmR9sBmkHAPT73KBe4stEUoDzk5HO2Y5IzjfPpOQusmFsADljC7WFUYYeFH2okiOOdXFeCF173Ckj4cQZyHl44694Yaa42zYVry8jYEBDdBb26AHSfYrME9dUEPNERgAJAULY'
    newss = {
            "articles": [{
                "title": "test",
                "thumb_media_id": "oV-d-Gt0UUGRkmYOoqzwde8bAw3KdXUeImjb2_gX-oA",
                "author": "vickey",
                "digest": "",
                "show_cover_pic": 1,
                "content": "<p>123456789</p>",
                "content_source_url": "",
            }]
    }

    print(newss)
    newsss = json.dumps(newss, ensure_ascii=False)
    print(newsss)
    myMaterial.add_new(accessToken, newsss)

# {"media_id":"oV-d-Gt0UUGRkmYOoqzwdbxh3AO2JjiVLA3iMdqdW2c"}
