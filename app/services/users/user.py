import app.services.repository.api_manager as api_manager

URL_USERS = "https://reqres.in/api/users/"

def obtener_usuario(id:str = None):
    url = URL_USERS if id is None else f"{URL_USERS}{id}"
    respuesta = api_manager.get(url)
    return respuesta

def crear_usuario(post: dict):
    headers = {'Content-Type': 'application/json'}
    url = f"{URL_USERS}{id}"
    return api_manager.post(url=url, headers=headers, payload=post)

def actualizar_usuario(put: dict, id: str):
    headers = {'Content-Type': 'application/json'}
    url = f"{URL_USERS}{id}"
    return api_manager.put(url=url, headers=headers, payload=put)

def eliminar_usuario(id: str):
    headers = {'Content-Type': 'application/json'}
    url = f"{URL_USERS}{id}"
    return api_manager.delete(url=url, headers=headers)