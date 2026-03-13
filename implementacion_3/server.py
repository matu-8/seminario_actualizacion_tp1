from wsgiref.simple_server import make_server

# En python, environ y start_response, de manera basica, serian como reques y response en nodeJS
def application(environ, start_response):
    try:
        with open('./index.html', 'rb') as f:
            contenido = f.read()
            headers = [
                ("Content-Type","text/html; charset=utf-8"),
                ('Content-Length', str(len(contenido)))
    ]
        start_response('200 OK', headers)
        return[contenido]

    except FileNotFoundError:
        status = '404 Not Found'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return[b"Archivo no encontrado"]

server = make_server('localhost', 5000, application)
print('>>> Servidor corriendo en http://localhost:5000')
server.serve_forever()