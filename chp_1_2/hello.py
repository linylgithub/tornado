#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

#从命令行中读取设置。指定应用监听HTTP请求的端口
from tornado.options import define,options
define("port",default=8383,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting','Hello')
        self.write(greeting + ',friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

