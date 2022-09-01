#Creando u diccionario simple
cancion = {
    'artista' : 'Metallica', #llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}

#acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])


#Mezclar con un String

artista = cancion['artista']
print(f'Estoy escuchando a {artista}')
print(cancion)