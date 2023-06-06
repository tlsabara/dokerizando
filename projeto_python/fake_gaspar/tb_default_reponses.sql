insert into main.tb_default_reponses (default_reponses_id, default_reponses_route, default_reponses_tag, default_reponses_content, default_reponses_is_active)
values  (1, '*', 'def_POST_200', '{
    "method": "POST",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', 1),
        (2, '*', 'def_GET_200', '{
    "method": "GET",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', 1),
        (3, '*', 'def_PUT_200', '{
    "method": "PUT",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', 1);