
from datetime import date

class Persona:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Fecha de nacimiento: {self.fecha_nacimiento}"
