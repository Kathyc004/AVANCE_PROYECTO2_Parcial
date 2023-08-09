#Bajaña Acosta Luis Steven
#Coronel Macias Katherine Jamilet
#Cedeño Maridueña Odalys Nicole
#Guerrero Ormeño Carlos Eduardo

from Docente import Docente
from Estudiante import Estudiante

dato1 = Docente(cedula='0123456789', nombre='Catherine', apellido='Coronel', email='Ccoronel20@gmail.com',
                telefono='0987456321', direccion='Batallón', numero_libros=0, activo=True, carrera='Medicina',
                titulo_3er_nivel='LCD', titulo_4to_nivel=',MSC')
dato2 = Docente(cedula='0930731518', nombre='Steven', apellido='Bajañ0061', email='Sbajaña@hotmail.com',
                telefono='0975316489', direccion='Miraflores', numero_libros=0, activo=True, carrera='Lic',
                titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
print(dato1)
print(dato2)

# Estudiantes
Est1 = Estudiante(cedula='0947859632', nombre='Odalys', apellido='Cedeño', email='odalys_ _bonititap95@gmail.com',
                    telefono='0978964158', direccion='Garzota', numero_libros=0, activo=True, carrera='Lic',
                    nivel=3)
Est4 = Estudiante(cedula='0989441552', nombre='Jhonny', apellido='Mite', email='jmitecoral@gmail.com',
                    telefono='0994568282', direccion='Daule', numero_libros=0, activo=True, carrera='Ing',
                    nivel=3)
print(Est1)
print(Est4)
