from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import os
from datetime import datetime
from sqlalchemy.sql.expression import select

from endpoint_orm import Session, Base, engine

ROOT_DIR = Path(os.path.abspath(os.path.curdir))


def fn_app_log(message: str, error_trace: str = None) -> bool:
    log_folder = ROOT_DIR / 'app_logs'
    log_folder.mkdir(parents=True, exist_ok=True)
    with open(log_folder / 'app_log.txt', 'a') as file:
        file.write(f'|{f"LOG:{datetime.now()}":-^50}|\n')
        file.write(f'|{f"MESSAGE:{message}": <50}|\n')
        if error_trace:
            file.write(error_trace)
            file.write('\n')
        file.write(f'|{f"END LOG":-^50}|\n')


def save_request_data(path: str, recived_content: str) -> bool:
    from endpoint_orm import TbRequestsRecived
    try:
        with Session() as db:
            request_inst = TbRequestsRecived(
                requests_recived_route=path,
                requests_recived_content=recived_content,
                requests_recived_timestamp=datetime.now()
            )
            db.add(request_inst)
            db.commit()
            fn_app_log('Dados Salvos corretamente.')
    except Exception as e:
        fn_app_log('Erro ao salvar no DB', str(e))
        return False
    else:
        return True


def collect_response_data(where_tag=None, where_id=None) -> str:
    from endpoint_orm import TbDefaultResponses
    response = ""
    try:
        if where_id is not None and where_tag is None:
            with Session() as db:
                response = db.execute(
                    select(TbDefaultResponses).where(
                        TbDefaultResponses.default_reponses_id == where_id
                    )
                ).one()
            fn_app_log('Dados Localizados corretamente.')
        elif where_tag is not None and where_id is None:
            with Session() as db:
                response = db.execute(
                    select(TbDefaultResponses).where(
                        TbDefaultResponses.default_reponses_tag == where_tag
                    )
                ).one()
            fn_app_log('Dados Localizados corretamente.')
        else:
            raise ValueError("Parâmetros inválidos.")
    except Exception as e:
        fn_app_log('Erro ao carregar dados do DB', str(e))
        return "{'message':'data not found.'}"
    else:
        return response[0].default_reponses_content


class APIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f'{"requisicao":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("GET hora: ", timestamp_)
        print(self.headers.as_string())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        clean_response = 'GET respondido'
        msg_get_response = collect_response_data(where_tag="def_GET_200")
        msg_get_response = msg_get_response if msg_get_response else clean_response
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')

    def do_POST(self):
        print(f'{" requisicao ":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("POST hora: ", timestamp_)
        print(self.headers.as_string())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        clean_response = 'POST respondido'
        length = int(self.headers["Content-Length"])

        save_request_data(self.path, self.rfile.read(length).decode('UTF-8'))
        msg_get_response = collect_response_data(where_tag="def_POST_200")
        msg_get_response = msg_get_response if msg_get_response else clean_response
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
        clean_response = 'PUT respondido'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        save_request_data(self.path, str(self.rfile.read(length)))
        msg_get_response = collect_response_data(where_tag="def_PUT_200")
        msg_get_response = msg_get_response if msg_get_response else clean_response
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')


if __name__ == '__main__':
    with Session() as db:
        Base.metadata.create_all(engine)

    base_port = 8000

    with HTTPServer(('', base_port), APIServer) as local_api_server:
        print(f'Server ON, listen: {base_port}\n{"-" * 50}')
        local_api_server.serve_forever()
