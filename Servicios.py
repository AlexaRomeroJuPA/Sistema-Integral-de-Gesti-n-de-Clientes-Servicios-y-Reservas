from abc import ABC, abstractmethod
from entidades import EntidadBase
from excepciones import ServicioError


class Servicio(EntidadBase, ABC):
    """
    Clase abstracta Servicio.
    """

    def __init__(self, nombre, tarifa_base):
        self.nombre = nombre
        self.tarifa_base = tarifa_base

        if tarifa_base <= 0:
            raise ServicioError("La tarifa base debe ser mayor que cero")

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

        class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def __init__(self, nombre, tarifa_base, capacidad):
        super().__init__(nombre, tarifa_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores que cero")

        costo = self.tarifa_base * horas
        costo -= costo * descuento
        return costo

    def descripcion(self):
        return f"Reserva de sala para {self.capacidad} personas"

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Sala"

        class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def __init__(self, nombre, tarifa_base, tipo_equipo):
        super().__init__(nombre, tarifa_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, horas, descuento=0):
        costo_total -= costo_total * descuento

        return costo_total

    def descripcion(self):
        return f"Alquiler de equipo tipo {self.tipo_equipo}"

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Equipo"


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def __init__(self, nombre, tarifa_base, especialista):
        super().__init__(nombre, tarifa_base)
        self.especialista = especialista

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("La duración debe ser válida")

        costo = (self.tarifa_base * horas) + 50000
        costo -= costo * descuento

        return costo

    def descripcion(self):
        return f"Asesoría especializada por {self.especialista}"

    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} - Asesoría"
