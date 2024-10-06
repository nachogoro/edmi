from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Define the service
class HelloWorldService(ServiceBase):

    @rpc(Unicode(min_occurs=1), _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}"

# Create the application
application = Application(
    [HelloWorldService],
    tns='spyne.examples.helloworld',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Create the WSGI app
wsgi_app = WsgiApplication(application)

# Create a simple server for the /hello path
class HelloWSGIApp:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # Only allow access if the path is /hello
        if environ['PATH_INFO'] == '/hello':
            return self.wsgi_app(environ, start_response)
        else:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return [b'404 Not Found']

if __name__ == '__main__':
    # Use the HelloWSGIApp to route requests to /hello
    app_with_route = HelloWSGIApp(wsgi_app)
    server = make_server('127.0.0.1', 8000, app_with_route)

    print("SOAP server is running at http://127.0.0.1:8000/hello")
    server.serve_forever()
