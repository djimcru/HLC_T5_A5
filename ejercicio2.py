class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad= edad
        self.profesion = profesion 

    def presentacion(self):
        print(f"me llamo {self.nombre},tengo {self.edad} años , soy {self.profesion} y estudio {self.estudios}")

class Estudiante(Persona):
    def __init__(self,nombre, edad, profesion,estudios):
        super().__init__( nombre, edad, profesion)
        self.estudios=estudios
    def presentacion(self):
        print(f"me llamo {self.nombre},tengo {self.edad} años , soy {self.profesion} y estudio {self.estudios}")


Carlos=Estudiante('Carlos', 22, 'Estudiante','Matematicas')
Carlos.presentacion()
