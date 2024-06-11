class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


    def alta(self):
        print(f"El alumno {self.nombre} {self.apellido} se dio de alta en un curso.")

    def __eq__(self, other):
        return self.dni == other.dni

class Docente:
    def __init__(self, dni):
        self.dni = dni

    def __eq__(self, other):
        return self.dni == other.dni

alumno1 = Alumno("Carlos","López", 1234)
alumno2 = Alumno("Coni","Fernández", 5474)

docente1 = Docente(5474)

print(alumno1.nombre, alumno1.apellido)

alumno1.alta()
alumno2.alta()

print(alumno1 == alumno2)
print(alumno1 == docente1)