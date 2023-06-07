insert into public.tb_default_reponses (default_reponses_route, default_reponses_tag, default_reponses_content, default_reponses_is_active)
values  ( '*', 'def_POST_200', '{
    "method": "POST",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', true),
        ( '*', 'def_GET_200', '{
    "method": "GET",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', true),
        ( '*', 'def_PUT_200', '{
    "method": "PUT",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', true),
        ( '/NONE', 'def_PATH_200', '{
    "method": "PATH",
    "status_code": 200,
    "message": "Request recebida com sucesso"
}', true);