from app.services.users.user import obtener_usuario, crear_usuario, actualizar_usuario, eliminar_usuario

def app():
    #GET
    users_data = obtener_usuario()
    print(users_data)
    
    #Usario
    post_user = {
            "name": "Ignacio",
            "job": "Profesor"
                }
    
    put_user = {
                "name": "morpheus",
                "residence": "zion"
             }
    

    created_user = crear_usuario(post=post_user)
    print(created_user)
    

    update_user = actualizar_usuario(put=put_user, id=2)
    print(update_user)
    

    e_user = eliminar_usuario(id='6')
    if(e_user['data'] == None):
        print(f"Respuesta de la api: {e_user['message']}")
    print(e_user)
    
    
    
    
    
    
    
    
    
    

    
    