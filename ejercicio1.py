class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad= edad
        self.profesion = profesion

    def presentacion(self):
        print(f"me llamo {self.nombre},tengo{self.edad} años y soy {self.profesion}")

Ana=Persona('Ana', 28, 'Ingeniera')
Ana.presentacion()