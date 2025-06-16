# utils.py

saludo_global = "Hola desde utils.py"

def saludar(nombre):
    return f"{saludo_global}, {nombre}!"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."
