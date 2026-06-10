class Carrera:

    #Constructor
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def mostar_info(self):
        return f"Carrera ID: {self.id}, Nombre: {self.nombre}"