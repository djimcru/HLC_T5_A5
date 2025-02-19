class Persona:
    def __init__(self, nombre, edad, profesion,estudios):
        self.nombre= nombre
        self.edad= edad
        self.profesion = profesion 
        self.estudios = estudios

    def presentacion(self):
        print(f"me llamo {self.nombre},tengo {self.edad} años , soy {self.profesion} y estudio {self.estudios}")
Carlos=Persona('Carlos',22,'Estudiante','Matematica')
Carlos.presentacion()