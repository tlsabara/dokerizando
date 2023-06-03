from flask import Flask
from flask_restful import Api

import api_core
# todo melhorar o import

app = Flask(__name__)
api = Api(app)

api.add_resource(api_core.PingPost, '/v1/ping_post')
api.add_resource(api_core.PingGet, '/v1/ping_get')
api.add_resource(api_core.Ping, '/', '/v1/ping', '/v1')


if __name__ == '__main__':
    app.run()
