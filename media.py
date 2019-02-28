from basic import Basic
import requests


class Media(object):
    def __init__(self):
        pass

    def upload(self, accessToken, filePath, mediaType):
        openFile = {'file':open(filePath, "rb")}
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        r = requests.post(postUrl, files=openFile)
        print(r.text)


if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "1.jpg"
    mediaType = "thumb"
    myMedia.upload(accessToken, filePath, mediaType)

