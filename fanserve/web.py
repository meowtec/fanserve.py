# coding:utf-8
from core import Core


class Tornado(Core):

    def __init__(self, context):
        self.__cxt = context

    def get_argument(self, name):
        return self.__cxt.get_argument(name, None)

    def body_raw(self):
        return self.__cxt.request.body

    def write(self, text):
        self.__cxt.write(text)