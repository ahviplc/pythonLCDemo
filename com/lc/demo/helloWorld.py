print("hello world")

name = input('你是: ')
print('我是：'+name)


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']