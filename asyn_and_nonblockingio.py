#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: asyn_and_nonblockingio.py
@time: 2018/9/15 11:16
"""
"""
    实时web功能需要为每个用户提供一个多数时间被闲置的长连接, 在传统的同步web服务器中，这意味着要为每个用户提供一个
线程, 当然每个线程的开销都是很昂贵的.
    为了尽量减少并发连接造成的开销，Tornado使用了一种单线程事件循环的方式. 这就意味着所有的应用代码都应该是异步
非阻塞的, 因为在同一时间只有一个操作是有效的.
    异步和非阻塞是非常相关的并且这两个术语经常交换使用,但它们不是完全相同的事情.
"""

# 一个简单的同步函数

from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response

# 把上面的例子改写回调参数重写的异步函数

from tornado.httpclient import AsyncHTTPClient

def asynchronous_fetch(url,callback):
    http_client = AsyncHTTPClient()
    def handle_response(response):
        callback(response.body)
    http_client.fetch(url,callback=handle_response)

# 使用Future代替回调

from tornado.concurrent import Future

def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f : my_future.set_result(f.result())
    )
    return my_future
# 协程版本

from tornado import gen

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client(url)
    raise gen.Return(response.body)