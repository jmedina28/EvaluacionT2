
class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        
    def __str__(self):
        return f"El alumno: {self.nombre} {self.apellido} con una nota de {self.nota} se ha creado con éxito." 
    
    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspenso"