from basic import Basic
import requests


class Media(object):
    def __init__(self):
        pass

    def upload(self, accessToken, filePath, mediaType):
        openFile = {'file':open(filePath, "rb")}
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        r = requests.post(postUrl, files=openFile)


if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "111.png"
    mediaType = "image"
    myMedia.upload(accessToken, filePath, mediaType)

