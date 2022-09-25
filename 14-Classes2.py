class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.precio = precio
        
         
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}') 
          
#Instanciar la clase
restaurant = Restaurant('Pizzeria Colombia', 'Comida Italiana', 50)
restaurant.mostrar_informacion()
 

restaurant2 = Restaurant('Hamburguesas La nota', 'Comida rápida', 20)
restaurant2.mostrar_informacion()



