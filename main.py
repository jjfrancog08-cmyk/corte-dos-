from datetime import date
from persona import Persona
from jugador import Jugador

def main():
    
    p1 = Persona("Joaquin Quin", "12345678A", date(1995, 4, 10))
    p2 = Persona("Jose Jose", "23456789B", date(1990, 11, 2))
    p3 = Persona("Robert pattinson", "34567890C", date(1988, 7, 21))

    
    j1 = Jugador("Max verstappen", "45678901D", date(2000, 1, 15), 101)
    j2 = Jugador("Lewis Hamilton", "56789012E", date(1998, 3, 8), 102)
    j3 = Jugador("Nico Rosberg", "67890123F", date(2002, 9, 30), 103)

    
    print(p1)
    print(p2)
    print(p3)
    print(j1)
    print(j2)
    print(j3)


    personas = [p1, j1, j2]
    for persona in personas:
        print(persona)  

    
    j1.entrenar()

    
    j1.num_fed = 999
    print("Después de actualizar num_fed:", j1)

if __name__ == "__main__":
    main()
    