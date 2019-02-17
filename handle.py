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
                return echostr
            else:
                return ""
        except IndexError:
            print("123")

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)

            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.ToUserName
                fromUser = recMsg.FromUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print("暂不处理")
                return "success"
        except Exception as e:
            return e
