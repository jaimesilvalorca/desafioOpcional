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
    
    #POST
    created_user = crear_usuario(post=post_user)
    print(created_user)
    
    #PUT
    update_user = actualizar_usuario(put=put_user, id=2)
    print(update_user)
    
    #DELETE 
    e_user = eliminar_usuario(id='6')
    if(e_user == None):
        print("Problema con la repsuesta de la api")
    
    
    
    
    
    
    
    
    
    

    
    