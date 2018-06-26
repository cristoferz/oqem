from BaseHTTPServer import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path.startswith("/teste",0):
            self.wfile.write("<html><body><h1>No teste</h1></body></html>")    
        else:
            self.wfile.write("<html><body><h1>"+self.path+"</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")