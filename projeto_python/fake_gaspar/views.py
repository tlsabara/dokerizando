from orm import queries
from jinja2 import Environment, FileSystemLoader



def render_template_like_flask(template_namefile:str, jinja_vars:dict):
    environment = Environment(loader=FileSystemLoader("./templates/"))
    template = environment.get_template(template_namefile)
    try:
        return template.render(
            **jinja_vars
        )
    except Exception as e:
        return False


def request_recived_repot() -> str:
    requests_list = queries.collect_last_50_recived_requests()
    template_vars = {"request_list": [request_._asdict() for request_ in requests_list]}
    return render_template_like_flask('request_recived_report.html.jinja', template_vars)
