from entidades import EntidadBase
from excepciones import ClienteError


class Cliente(EntidadBase):
    """
    Clase Cliente con encapsulación y validaciones.
    """

    def __init__(self, nombre, identificacion, correo):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__correo = correo

        self.validar_datos()

    def validar_datos(self):
        if not self.__nombre.strip():
            raise ClienteError("El nombre del cliente no puede estar vacío")

        if len(self.__identificacion) < 5:
            raise ClienteError("La identificación es inválida")

        if "@" not in self.__correo:
            raise ClienteError("Correo electrónico inválido")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"ID: {self.__identificacion} | "
            f"Correo: {self.__correo}"
        )