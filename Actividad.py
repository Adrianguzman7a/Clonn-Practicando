#Class Desarrollador
def __init__(self, nombre, lenguaje):
    self.nombre = nombre
    self.lenguaje = lenguaje # Esto sera una lista
    self.nivel_energia = 150

def programar(self, horas):
    # Cada hora de programar reduce 10 puntos de energia
    gasto = horas * 10
    self.nivel_energia -= gasto
    print(f"{self.nombre} ha programado durante {horas} horas y ahora tiene {self.nivel_energia} puntos de energía.")
    if self.nivel_energia <= 0:
        print(f"{self.nombre} está agotado y necesita descansar.")
    else:
        print(f"{self.nombre} tiene suficiente energía para seguir programando.")
def entrenar(self, horas):
    # Cada hora de entrenamiento aumenta 25 puntos de energia
    aumento = horas * 25
    self.nivel_energia += aumento
    print(f"{self.nombre} ha entrenado durante {horas} horas y ahora tiene {self.nivel_energia} puntos de energía.")
    if self.nivel_energia > 150:
        self.nivel_energia = 150  # Limitar la energía máxima a 150
        print(f"{self.nombre} ha alcanzado su nivel máximo de energía.")
    else:
        print(f"{self.nombre} tiene suficiente energía para seguir entrenando.")
def mostrar_info(self):
    print(f"Nombre: {self.nombre}")
    print(f"Lenguajes de programación: {', '.join(self.lenguaje)}")
    print(f"Nivel de energía: {self.nivel_energia}")
