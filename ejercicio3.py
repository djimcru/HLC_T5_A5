class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad= edad
        self.profesion = profesion
    def presentacion(self):
        print(f"me llamo {self.nombre},tengo{self.edad} años y soy {self.profesion}")


class Trabajador(Persona):
    def __init__(self,nombre, edad, profesion,empresa):
        super().__init__( nombre, edad, profesion)
        self.empresa=empresa
    
    def presentacion(self):
        print(f"me llamo {self.nombre},tengo{self.edad} años y trabajo en  {self.empresa}")

Elena=Trabajador('Elena',35,'Arquitecto','Construcciones xyz')
Elena.presentacion()

