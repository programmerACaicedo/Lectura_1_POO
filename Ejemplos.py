# Clases y Objetos

class Mascota:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def __str__(self):
        return f'Nombre: {self.nombre}, Raza: {self.raza}'

mascota = Mascota('Rex', 'Pastor Alemán')
print(mascota)

# Metodo __init__

class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.saldo = cantidad
    def mostrar_saldo(self):
        print(f'El saldo es {self.saldo}$')
        
t = Tarjeta('1111111111', 1000)
t.mostrar_saldo()

# Herencia 

class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.saldo = cantidad

    def get_id(self):
        return self.numero

    def __str__(self):
        return f'Tarjeta número {self.numero} con saldo {self.saldo}€'

class TarjetaDescuento(Tarjeta):
    def __init__(self, numero, descuento):
        super().__init__(numero)
        self.descuento = descuento

    def mostrar_descuento(self):
        print(f'Descuento de {self.descuento}% en los pagos.')

    def __str__(self):
        return f'Tarjeta número {self.numero} con descuento del {self.descuento}%'

t_d = TarjetaDescuento('0123456789', 2)
print(t_d)
print(t_d.get_id())
t_d.mostrar_descuento()


# Metodo __str__

class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.saldo = cantidad

    def __str__(self):
        return f'Tarjeta número {self.numero} con saldo {self.saldo}$'

t = Tarjeta('0123456789', 1000)
print(t)


# Encapsulamiento

class Clase:
    def __init__(self, atributo_instancia):
        self.__atributo_instancia = atributo_instancia  # Privado

    def get_atributo(self):
        return self.__atributo_instancia

    def set_atributo(self, valor):
        self.__atributo_instancia = valor

mi_clase = Clase("Valor Inicial")
print(mi_clase.get_atributo())  # Acceso al atributo
mi_clase.set_atributo("Nuevo Valor")
print(mi_clase.get_atributo())  # Acceso al atributo modificado
