#Bajaña Acosta Luis Steven
#Coronel Macias Katherine Jamilet
#Cedeño Maridueña Odalys Nicole
#Guerrero Ormeño Carlos Eduardo

from persona import Persona

class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula: str, nombre: str, apellido: str, email: str, telefono: str, direccion: str,
                 numero_libros: int, activo: bool, carrera: str, nivel: int):
        Estudiante.contador_estudiante += 1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Estudiante.contador_estudiante
        self._nivel = nivel
        super(Estudiante, self).__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email,
                                         telefono=telefono, direccion=direccion, numero_libros=numero_libros,
                                         activo=activo, carrera=carrera)

    def __str__(self):
        return f' Estudiante : {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
    Est1 = Estudiante(cedula='0947859632', nombre='Odalys', apellido='Cedeño', email='odalys_ _bonititap95@gmail.com',
                    telefono='0978964158', direccion='Garzota', numero_libros=0, activo=True, carrera='Lic',
                    nivel=3)
    Est2 = Estudiante(cedula='0986523018', nombre='Carlos', apellido='Guerrero', email='keguerreroo@gmail.com',
                    telefono='0978885875', direccion='Sauces', numero_libros=0, activo=True, carrera='Lic',
                    nivel=3)
    Est3 = Estudiante(cedula='0978594320', nombre='Tonny', apellido='Paredes', email='Tommy_lindo90@hotmail.com',
                    telefono='0978594115', direccion='Sergio Toral', numero_libros=0, activo=True, carrera='Lic',
                    nivel=3)
    Est4 = Estudiante(cedula='0989441552', nombre='Jhonny', apellido='Mite', email='jmitecoral@gmail.com',
                    telefono='0994568282', direccion='Daule', numero_libros=0, activo=True, carrera='Ing',
                    nivel=3)

    print(Est1)
    print(Est2)
    print(Est3)
    print(Est4)
