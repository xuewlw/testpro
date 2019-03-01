from basic import Basic
import requests


class Media(object):
    def __init__(self):
        pass

    def upload(self, accessToken, filePath, mediaType):
        openFile = {'media': open(filePath, 'rb')}
        # postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        r = requests.post(postUrl, files=openFile)
        print(r.text)


if __name__ == '__main__':
    myMedia = Media()
    # accessToken = Basic().get_access_token()
    accessToken = '19_3NuYtsVv322Zrsg0pa7ZwGmR9sBmkHAPT73KBe4stEUoDzk5HO2Y5IzjfPpOQusmFsADljC7WFUYYeFH2okiOOdXFeCF173Ckj4cQZyHl44694Yaa42zYVry8jYEBDdBb26AHSfYrME9dUEPNERgAJAULY'
    filePath = "1.jpg"
    mediaType = "thumb"
    myMedia.upload(accessToken, filePath, mediaType)

# {"media_id":"oV-d-Gt0UUGRkmYOoqzwde8bAw3KdXUeImjb2_gX-oA","url":"http:\/\/mmbiz.qpic.cn\/mmbiz_jpg\/YXicRWmyowt8xMCdDPCjEzEjyzBpTIXBTn1A3UeOhRLU9icodxEgp7PLLq1CyLGiapslW5vJlLWqTYFqHNTpYJ4QQ\/0?wx_fmt=jpeg"}

