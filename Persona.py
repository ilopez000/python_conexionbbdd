class Persona:
    def __init__(self, id, nombre, apellido1, apellido2):
        self.id = id
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Apellido1: {self.apellido1}, Apellido2: {self.apellido2}'

    def imprimir_persona(self):
        print(f'ID: {self.id}, Nombre: {self.nombre}, Apellido1: {self.apellido1}, Apellido2: {self.apellido2}')