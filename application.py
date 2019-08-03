def application(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/html')])
    return ["<h1>Hello world!</h1>\n"]
