# coding:utf-8

from .core import Core


class Tornado(Core):

    def __init__(self, context):
        self.__cxt = context

    def get_argument(self, name):
        return self.__cxt.get_argument(name, None)

    def body_raw(self):
        return self.__cxt.request.body.decode()

    def write(self, text):
        self.__cxt.write(text)

class Webpy(Core):

    def __init__(self, context):
        self.__cxt = context
        self.__querys = context.input(_method='get')

    def get_argument(self, name):
        return self.__querys.get(name)

    def body_raw(self):
        return self.__cxt.data()

    def write(self, text):
        #self.__cxt.write(text)
        pass
