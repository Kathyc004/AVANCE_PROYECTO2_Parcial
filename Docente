#Bajaña Acosta Luis Steven
#Coronel Macias Katherine Jamilet
#Cedeño Maridueña Odalys Nicole
#Guerrero Ormeño Carlos Eduardo
from Persona import Persona

class Docente(Persona):
    contador_docente = 0
    def __init__(self ,cedula :str ,nombre :str ,apellido :str ,email :str ,telefono :str ,direccion :str
                 ,numero_libros :int ,activo :bool ,carrera :str, titulo_3er_nivel :str ,titulo_4to_nivel :str):
        Docente.contador_docente +=1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        super(Docente, self).__init__(cedula = cedula, nombre = nombre, apellido= apellido, email=email, telefono=telefono, direccion=direccion, numero_libros=numero_libros, activo=activo, carrera=carrera)

    def __str__ (self):
        return f' Docente : {self.__dict__.__str__()}'
    @property
    def id (self):
        return self._id
    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel
    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel
    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
    dato1 = Docente(cedula='0123456789', nombre='Catherine', apellido='Coronel', email='Ccoronel20@gmail.com',telefono='0987456321', direccion='Batallón', numero_libros=0, activo=True, carrera='Medicina',
                 titulo_3er_nivel='LCD', titulo_4to_nivel=',MSC')
    dato2 = Docente(cedula='0930731518', nombre='Steven', apellido='Bajañ0061', email='Sbajaña@hotmail.com',telefono='0975316489', direccion='Miraflores', numero_libros=0, activo=True, carrera='Lic',
                 titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

    print(dato1)
    print(dato2)
