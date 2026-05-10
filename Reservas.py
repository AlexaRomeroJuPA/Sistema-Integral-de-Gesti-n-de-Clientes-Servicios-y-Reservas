from excepciones import ReservaError


class Reserva:
    """
    Clase Reserva.
    """

    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

        if horas <= 0:
            raise ReservaError("Las horas de reserva deben ser mayores a cero")

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self, descuento=0):
        try:
            costo = self.servicio.calcular_costo(self.horas, descuento)
            self.confirmar()

        except Exception as error:
            raise ReservaError(
                "Error procesando la reserva"
            ) from error

        else:
            return costo

        finally:
            print("Proceso de reserva finalizado")

    def mostrar_reserva(self):
        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
