from persona import Persona

class Jugador(Persona):
    def __init__(self, nombre, dni, fecha_nacimiento, num_fed):
        super().__init__(nombre, dni, fecha_nacimiento)
        self.num_fed = num_fed

    def entrenar(self):
        print(f"{self.nombre} está entrenando...")

    def __str__(self):
        return f"{super().__str__()}, Número de federación: {self.num_fed}"