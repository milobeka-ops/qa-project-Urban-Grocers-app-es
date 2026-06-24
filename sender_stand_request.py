import configuration
import data
import requests



def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)



def post_new_client_kit(kit_body, auth_token):
    # Copiamos los encabezados base para no modificar el archivo data.py original
    current_headers = data.headers.copy()
    # Agregamos el token de autenticación al encabezado Authorization
    current_headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=current_headers)