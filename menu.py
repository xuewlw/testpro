import requests
from basic import Basic

class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        # if isinstance(postData,unicode):
        urlResp = requests.post(postUrl, data=postData.encode('utf8'))
        print(urlResp.text)


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type":"click",
                "name":"开发指引",
                "key":"mpGuide"
            },
            {
                "name":"公众平台",
                "sub_button":
                [
                    {
                        "type":"view",
                        "name":"更新公告",
                        "url":"http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type":"view",
                        "name":"接口权限说明",
                        "url":"http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type":"view",
                        "name":"返回码说明",
                        "url":"http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type":"media_id",
                "name":"旅行",
                "media_id":"oV-d-Gt0UUGRkmYOoqzwdbxh3AO2JjiVLA3iMdqdW2c"
            }
        ]
    }
    """
    print(type(postJson))
    # accessToken = Basic().get_access_token()
    accessToken = '19_3NuYtsVv322Zrsg0pa7ZwGmR9sBmkHAPT73KBe4stEUoDzk5HO2Y5IzjfPpOQusmFsADljC7WFUYYeFH2okiOOdXFeCF173Ckj4cQZyHl44694Yaa42zYVry8jYEBDdBb26AHSfYrME9dUEPNERgAJAULY'
    # myMenu.create(postJson,accessToken)
