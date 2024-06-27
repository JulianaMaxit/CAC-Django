class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

        #Proceso de limpieza de nombre y apellido (la clase Persona lo sabe hacer)

    def saludar(self):
        print(f"Mi nombre es {self.nombre} {self.apellido}")
        

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, turno):
        super().__init__(nombre, apellido, dni)
        self.turno = turno
    
    def inscribirse(self):
        print("Me inscribí como alumn@")

class Docente(Persona):
    def __init__(self, nombre, apellido, dni, CUIT):
        super().__init__(nombre, apellido, dni)
        self.CUIT = CUIT

    def tomar_curso(self):
        print("Tomé un curso como docente")

alumno1 = Alumno("Juliana","Maxit", 39031074, "Mañana")

alumno1.saludar()
alumno1.inscribirse()

docente1 = Docente("Marta", "Martinez", 3525235, 22322332)
docente1.saludar()
docente1.tomar_curso()