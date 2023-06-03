from project_interfaces.api_interfaces import ApiBasePostRoute, ApiBaseGetRoute
from core.works import ping_pong, application_logs


class PingPost(ApiBasePostRoute):
    """Endpoint for ping request based on POST

    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    """

    def _valitaditon_post(self, *args, **kwargs):
        return super()._valitaditon_post(*args, **kwargs)

    def _method_post(self, post_data, **kwargs):
        try:
            message = ping_pong.ping_post('ping')
        except ValueError as e:
            application_logs.log_ext(e)
            status_code = 400
            application_logs.log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            application_logs.log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message': message,
                'status_code': status_code
            }
        return ret_dict


class PingGet(ApiBaseGetRoute):
    """Endpoint for ping request based on GET

    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    """

    def _valitaditon_get(self, **kwargs):
        return super()._valitaditon_get(**kwargs)

    def _method_get(self, **kwargs):

        try:
            message = ping_pong.ping_get()
        except ValueError as e:
            application_logs.log_ext(e)
            status_code = 400
            application_logs.log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            application_logs.log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message': message,
                'status_code': status_code
            }
        return ret_dict


class Ping(ApiBasePostRoute, ApiBaseGetRoute):
    """Endpoint for ping request on GET or POST methods

    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    Long description of this endpoint, Long description of this endpoint,
    """

    def _valitaditon_post(self, **kwargs):
        return super()._valitaditon_post(**kwargs)

    def _method_get(self, **kwargs):
        return ping_pong.ping_get()

    def _valitaditon_get(self, **kwargs):
        return super()._valitaditon_get(**kwargs)

    def _method_post(self, post_data, **kwargs):
        try:
            message = ping_pong.ping_post(post_data.get('key'))
        except ValueError as e:
            application_logs.log_ext(e)
            status_code = 400
            application_logs.log_ext("Erro nos inputs")
        except Exception as e:
            application_logs.log_text(e)
            status_code = 405
            application_logs.log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message': message,
                'status_code': status_code
            }
        return ret_dict
