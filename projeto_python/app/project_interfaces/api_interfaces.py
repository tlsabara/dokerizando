from abc import ABC, abstractmethod

from flask import jsonify, request
from flask_restful import Resource


class ApiBasePostRoute(ABC, Resource):
    @abstractmethod
    def _method_post(self, post_data, **kwargs) -> dict:
        return {'message': 'POST not allowed'}

    @abstractmethod
    def _valitaditon_post(self, **kwargs):
        return kwargs

    def post(self):
        post_data = request.get_json()
        self._valitaditon_post()
        return jsonify(self._method_post(post_data=post_data))


class ApiBaseGetRoute(ABC, Resource):
    @abstractmethod
    def _method_get(self, **kwargs):
        return jsonify(
            {'message': 'GET not allowed'}
        )

    @abstractmethod
    def _valitaditon_get(self, **kwargs):
        return kwargs.get('to_return')

    def get(self):
        return self._valitaditon_get(to_return=self._method_get())
