class Tamagotchi():
    def __init__(self,nombre):
        self.nombre = nombre
        self.hambre = 30
        self.energia = 100
        self.estado = "huevo"

    def serialize(self):
        if(self.hambre <=0 or self.energia<=0):
            return {"mensaje": f'{self.nombre} esta muerto :( '}
        else:
            return {
                "nombre": self.nombre,
                "hambre": self.hambre,
                "energia":self.energia,
                "estado":self.estado
            }
    def crecer(self):
        if(self.estado=='huevo'):
            self.estado ='ninio'
        elif(self.estado=='ninio'):
            self.estado ='adolescente'
        elif(self.estado=='adolescente'):
            self.estado ='adulto'
        else:
            self.estado ='adulto'
            return f'{self.nombre} no puede crecer más, ya está grande'
        
        return f'{self.nombre} ha pasado a etapa {self.estado}'
