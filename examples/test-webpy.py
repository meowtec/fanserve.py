# coding:utf-8

import sys

import web
sys.path.append("..")
import fanserve as fans
web.config.debug = False
urls = (
    '/weibo/', 'Hello'
)

class MyWebpyFans(fans.Webpy):

    app_secret = 'appsecretEnF5leY4V'

    def receive_text(self, text):
        if text == u'文章':
            print('receive wz')
            self.reply_articles([
                {
                    "display_name": "两个故事",
                    "summary": "今天讲两个故事，分享给你。谁是公司？谁又是中国人？",
                    "image": "http://storage.mcp.weibo.cn/0JlIv.jpg",
                    "url": "http://e.weibo.com/mediaprofile/article/detail?uid=1722052204&aid=983319"
                }
            ])
        else:
            print('receive text')
            self.reply_text(text)

    def receive_event(self, event):
        self.reply_text('event: ' + event)

    def receive_default(self, data):
        self.reply_text('发送『文章』，将返回文章；发送其他文字将原文返回。')


class Hello:
    def GET(self):
        return MyWebpyFans(context=web).get()

    def POST(self):
        return MyWebpyFans(context=web).post()

app = web.application(urls, globals())
app.run()
