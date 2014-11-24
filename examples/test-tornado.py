import sys
sys.path.append("..")
import tornado.ioloop
import tornado.web
import fanserve as fans


class MyTornadoFans(fans.Tornado):
    app_secret = 'appsecretEnF5leY4V'

    def receive_text(self, text):
        self.reply_text('123')

    def receive_event(self, event):
        self.reply_text('event: ' + event)


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