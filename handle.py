import hashlib
import reply
import receive
import web


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello,this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr =data.echostr
            token = "hello2019"
            print(signature)

            list = [token, timestamp, nonce]
            list.sort()
            list = ''.join(list)

            # sha1 = hashlib.sha1()
            # map(sha1.update, list)
            hashcode = hashlib.sha1(list.encode('utf8')).hexdigest()

            if hashcode == signature:
                print(echostr)
                return echostr
            else:
                print("22222")
                return "22"
        except IndexError:
            print("123")

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)

            recMsg = receive.parse_xml(webData)
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName

            if isinstance(recMsg, receive.Msg):
                if recMsg.MsgType == 'text':
                    content = "test"
                    print(toUser)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == "image":
                    mediaId = recMsg.MediaId
                    print(mediaId)
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                # else:
                #    return reply.Msg().send()

            if isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpGuide':
                        content = u"编写中".encode('utf8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()

            print("暂不处理")
            return reply.Msg().send()
        except Exception as e:
            return e
