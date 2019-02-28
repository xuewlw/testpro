import requests
import json
import urllib.request

from basic import Basic


class Material(object):
    def __init__(self):
        pass

    def add_new(self,access_Token, news):
        print(news)
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % access_Token
        urlResp = requests.post(postUrl, data=news.encode())
        print(urlResp.text)
        # urlResp = urllib.request.urlopen(postUrl, data=news)
        # print(urlResp.read())

if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    news = (
        {
            "articles": [{
                "title": "test",
                "thumb_media_id": "dQeBhDjmiWu5s7DPrlpF0mu35APe-swOfemDgnp1YCguUG-7Qs72GtF9omDRlsR5",
                "author": "vickey",
                "digest": "",
                "show_cover_pic": 1,
                "content": "<p>123456789</p>",
                "content_source_url": "",
            }]
    })

    news = json.dumps(news, ensure_ascii=False)
    myMaterial.add_new(accessToken, news)
