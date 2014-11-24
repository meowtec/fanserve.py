# coding:utf-8

import sys

sys.path.append("..")
import tornado.ioloop
import tornado.web
import fanserve as fans


class MyTornadoFans(fans.Tornado):
    app_secret = 'appsecretEnF5leY4V'

    def receive_text(self, text):
        if text == '文章':
            self.reply_articles([
                {
                    "display_name": "两个故事",
                    "summary": "今天讲两个故事，分享给你。谁是公司？谁又是中国人？",
                    "image": "http://storage.mcp.weibo.cn/0JlIv.jpg",
                    "url": "http://e.weibo.com/mediaprofile/article/detail?uid=1722052204&aid=983319"
                }
            ])
        else:
            self.reply_text(text)

    def receive_event(self, event):
        self.reply_text('event: ' + event)

    def receive_default(self):
        self.reply_text('发送『文章』，将返回文章；发送其他文字将原文返回。')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        MyTornadoFans(context=self).get()

    def post(self):
        MyTornadoFans(context=self).post()


application = tornado.web.Application([
    (r"/weibo/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()