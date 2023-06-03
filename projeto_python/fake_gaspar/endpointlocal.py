from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import  Path
import os
from datetime import datetime

ROOT_DIR = Path(os.path.abspath(os.path.curdir))


class APIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f'{"requisicao":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("GET hora: ", timestamp_)
        print(self.headers.as_string())
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg_get_response = 'GET respondendo'
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')

    def do_POST(self):
        print(f'{" requisicao ":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("POST hora: ", timestamp_)
        print(self.headers.as_string())
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg_get_response = 'POST respondendo'
        length = int(self.headers["Content-Length"])
        path = ROOT_DIR / 'downloads' / f'request_test__POST__{timestamp_}__ep_({self.path[1:]}).json'

        with open(path, "wb") as dst:
            dst.write(self.rfile.read(length))
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')

    def do_PUT(self):
        print(f'{" requisicao ":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print(self.headers)
        print("PUT hora: ", timestamp_)
        print(self.headers.as_string())
        length = int(self.headers["Content-Length"])
        path = ROOT_DIR / 'downloads' / f'request_test__PUT__{timestamp_}.json'

        with open(path, "wb") as dst:
            dst.write(self.rfile.read(length))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        msg_get_response = 'PUT respondendo'
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')

if __name__ == '__main__':
    base_port = 8000

    with HTTPServer(('', base_port),APIServer) as local_api_server:
        print(f'Server ON, listen: {base_port}\n{"-"*50}')
        local_api_server.serve_forever()
