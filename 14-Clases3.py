class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.__precio = precio #Default: public, POTECTED
        
         
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}') 
    
    #Getters y setters -  get= obtiene un valor set= agregar o modifica un valor
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
          
#Instanciar la clase
restaurant = Restaurant('Pizzeria Colombia', 'Comida Italiana', 50)

#restaurant.__precio = 80 #No será posible modificarlo con PRIVATE __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)
 

restaurant2 = Restaurant('Hamburguesas La nota', 'Comida rápida', 20)

#restaurant2.__precio = 40
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()