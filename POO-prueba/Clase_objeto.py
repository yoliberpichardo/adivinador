#####clase y objecto 1####

# class Car:
#     marca = ""
#     modelo = 2005
#     placa = ""

# taxi = Car()
# print(taxi.modelo)

####clases y objetos 2####
# class personas:
#     pass

# isidro = personas()
# roque = personas()

# # ###objecto.atributo = valor

# roque.edad = 18
# roque.sexo = "8 al dia"
# roque.estatura = "mediano"

# isidro.edad = 17
# isidro.sexo = "3 al dia"
# isidro.estatura = "pequeño"

# print(isidro)
#####metodos#####

# ###forma tradicional

# class matematicas:
#     def operacion(self):
#         self.n1 = 4
#         self.n2 = 6

# d = matematicas()
# d.operacion()
# print(d.n1 + d.n2)

#####forma simple#####
# class ropa():
#     def __init__(self):
#         self.marca = "adidas"
#         self.Size = 44
#         self.color = "blancos con negros"
    
# tenis = ropa()
# print(tenis.marca)
# print(tenis.color)

# ###funciones para atributos
# class Personas:
#     edad = 30
#     nombre ='starlin'
#     def __init__(self,edad,nombre):
#         self.nombre = nombre
#         self.edad = edad
#     def renombrar(self):
#         return '{} tiene {}'.format(self.nombre,self.edad)


# beisbolistas = Personas()
# ###forma tradicional de buscar un valor de un atributo
# print('la edad es: ', beisbolistas.edad)
# ###forma directa de buscar el valor de un atributo
# print('la edad es: ', getattr(beisbolistas,'edad'))

# ###funcion para saber si una funcion tiene un atributo
# print('el beisbolista tiene nombre? ', hasattr(beisbolistas,'nombre'),'es:',beisbolistas.nombre)

# ###funcion para cambiar un valor de un atributo
# print('antes: ',beisbolistas.edad)
# setattr(beisbolistas,'edad',24)
# print('ahora: ',beisbolistas.edad)

# ###funcion para eliminar un valor de un atributo
# print('antes: ',beisbolistas.edad)
# delattr(beisbolistas,'edad')
# print('ahora: ',beisbolistas.edad)


###### metodos constructores#######
# class estudiantes:
#     pass
#     def __init__(self,curso,grado):
#         self.curso = curso
#         self.grado = grado
#     def estudios(self):
#         return ' {} es de {}'.format(self.curso,self.grado)

#     def comentario(self,notas):
#         return '{} es: {}'.format(self.curso,notas)

# escanor = estudiantes('jorge','de 6to')
# print(escanor.estudios())

# ####modificar atributo####
# class Correo:
#     def __init__(self):
#         self.enviado = False
#     def enviar_correo(self):
#         self.enviado = True
# mi_gmail = Correo()

# print(mi_gmail.enviado)
# mi_gmail.enviar_correo()
# print(mi_gmail.enviado)

######Herencia#########
# class nanatsu_no_Taizai:
#     pass
#     def __init__(self,nombre,raza):
#         self.nombre = nombre
#         self.raza = raza
#     def datos(self):
#         return '{}  es de la raza de: {}'.format(self.nombre,self.raza)

# class demonios(nanatsu_no_Taizai):
#     def clanes(self,clan):
#         return '{}  es de la raza de: {}'.format(self.nombre,self.clan)

# class diosas(nanatsu_no_Taizai):
#     def clanes(self,clan):
#         return '{}  es de la raza de: {}'.format(self.nombre,self.clan)

# class hadas(nanatsu_no_Taizai):
#     def clanes(self,clan):
#         return '{}  es de la raza de: {}'.format(self.nombre,self.clan)

# integr_del_clan = demonios("meliodas","demonios")
# print(integr_del_clan.datos())
# print(integr_del_clan.nombre)

##########ejercicio con herencia######### 

# import math
# class Calculos:
#     def __init__(self,numero):
#         self.n = numero
#         self.datos = [0 for i in range(numero)] 
    
#     def igresodato(self):
#         self.datos = [int(input('ingresar datos '+ str(i+1) + ' = '))for i in range(self.n)]

# class operaciones_b(Calculos):
#     def __init__(self):
#         Calculos.__init__(self,2)

#     def multi(self):
#         a,b, = self.datos
#         m = a * b
#         return 'el resultado es: {}'.format(m)  

#     def div(self):
#         a,b, = self.datos
#         d = a / b
#         return 'el resultado es: {}'.format(d)

# class raiz(Calculos):
#     def __init__(self):
#        Calculos.__init__(self,1)
    
#     def cuadrada(self):
#         a, = self.datos
#         return 'el resultado es: {}'.format(math.sqrt(a))


# ejemplo = operaciones_b()
# print(ejemplo.igresodato())
# print(ejemplo.multi())

 ##### herencia multiples#####
class estudios:
    def __init__(self):
        pass
    
    def escuela(self):
        return "estudio en el ITM"

class trabajo:
    def __init__(self):
        pass

    def empresa(self):
        return "Trabaja Intellisy"

class profeccion:
    def __init__(self):
        pass 
    
    def Ing(self):
        return "es ingeniero en sistema"

class datos_personales(estudios,trabajo,profeccion):
    def __del__(self):
        return "la informacion no esta completa"

isidro = datos_personales()

print(isidro.empresa())


########### f- string############

 


