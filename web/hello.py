def app (environ, start_response):
    """Simplest possible application object"""
    data = "\n".join(environ.get('QUERY_STRING').split("&"))
    #data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
   # body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')] 
    start_response(status, response_headers)
    return iter([data.encode('utf-8')])
   
