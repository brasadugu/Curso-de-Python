playlist = {} #Diccionario vacio
playlist['canciones'] = [] #Lista vacia de canciones


#Funcion principal
def app():
    
    #Agregar playlist
    agregar_playlist = True
    
    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist? \r\n')
        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            #Ya tenemos un niombre, desactivar el true
            agregar_playlist = False
            
            #Mandar llamar la función para agregar canciones
            agregar_canciones()
            
def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    
    while agregar_cancion:
        #Preguntar al usuario que canciond esea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'
        
        cancion = input(pregunta)
        
        if cancion == 'X':
            #dejar de agregar canciones
            agregar_cancion = False
            
            #Mostrar resumen de la la playlist
            mostrar_resumen()
            
            
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)
            
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('canciones: \r\n')
    for cancion in playlist ['canciones']:
        print(cancion)
                
app()    