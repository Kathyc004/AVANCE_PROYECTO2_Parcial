#Katherine Coronel
#Steven Bajaña
#Odalys Cedeño
#Carlos Guerrero

from Material import Material

class Revista(Material):

    contador_revista = 0

    def __init__(self, codigo:str, autor:str, titulo:str, año:int, editorial:str, disponible:bool, cantidad_disponible:int,tipo:str):
        Revista.contador_revista +=1
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._año = año
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
        self._id = Revista.contador_revista
        self._tipo = tipo
        super(Revista, self).__init__(codigo=codigo, autor=autor, titulo=titulo, año = año, editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible)


    def __str__ (self):
        return f' Revista : {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @classmethod
    def actualizar_disponibilidad(self)-> bool :
        pass


if __name__ == '__main__':
    revista666 = Revista(codigo='123', autor='Leo', titulo='Ánalizando el comportamiento de una mente perturbada', año='2010', editorial='CEGO',
                        disponible=True, cantidad_disponible=17, tipo='FISICO')
    print(revista666)
