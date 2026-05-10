from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import *

def registrar_log(mensaje):
    with open("sistema_logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

clientes = []
servicios = []
reservas = []

print("\n========== SOFTWARE FJ ==========")
print("Sistema de Gestión de Clientes, Servicios y Reservas\n")

# OPERACIÓN 1
try:
    cliente1 = Cliente("Carlos Pérez", "12345", "carlos@gmail.com")
    clientes.append(cliente1)
    print(cliente1.mostrar_informacion())
except Exception as e:
    registrar_log(str(e))

# OPERACIÓN 2
try:
    cliente2 = Cliente("", "22222", "correo@gmail.com")
    clientes.append(cliente2)
except Exception as e:
    registrar_log(f"Error cliente: {e}")
    print(f"Error detectado: {e}")

    # OPERACIÓN 3
try:
    cliente3 = Cliente("Ana Torres", "12", "ana@gmail.com")
    clientes.append(cliente3)
except Exception as e:
    registrar_log(f"Error cliente: {e}")
    print(f"Error detectado: {e}")

# OPERACIÓN 4
try:
    sala = ReservaSala("Sala Premium", 100000, 20)
    servicios.append(sala)
    print(sala.descripcion())
except Exception as e:
    registrar_log(str(e))

    # OPERACIÓN 5
try:
    equipo = AlquilerEquipo("Portátiles", 80000, "Computadores")
    servicios.append(equipo)
    print(equipo.descripcion())
except Exception as e:
    registrar_log(str(e))

# OPERACIÓN 6
try:
    asesoria = AsesoriaEspecializada(
        "Consultoría TI",
        150000,
        "Ingeniero Senior"
    )

    servicios.append(asesoria)
    print(asesoria.descripcion())

except Exception as e:
    registrar_log(str(e))

    # OPERACIÓN 7
try:
    servicio_invalido = ReservaSala("Sala Básica", -50000, 10)
    servicios.append(servicio_invalido)

except Exception as e:
    registrar_log(f"Error servicio: {e}")
    print(f"Error detectado: {e}")

# OPERACIÓN 8
try:
    reserva1 = Reserva(cliente1, sala, 5)
    costo = reserva1.procesar_reserva(0.10)

    reservas.append(reserva1)

    print(reserva1.mostrar_reserva())
    print(f"Costo total: ${costo}")

except Exception as e:
    registrar_log(f"Error reserva: {e}")
    print(f"Error detectado: {e}")

    # OPERACIÓN 9
try:
    reserva2 = Reserva(cliente1, equipo, -2)
    reservas.append(reserva2)

except Exception as e:
    registrar_log(f"Reserva inválida: {e}")
    print(f"Error detectado: {e}")

# OPERACIÓN 10
try:
    reserva3 = Reserva(cliente1, asesoria, 3)
    costo = reserva3.procesar_reserva()

    reservas.append(reserva3)

    print(reserva3.mostrar_reserva())
    print(f"Costo total asesoría: ${costo}")

except Exception as e:
    registrar_log(f"Error final: {e}")
    print(f"Error detectado: {e}")


print("\nSistema ejecutado correctamente.")
print("Revise el archivo sistema_logs.txt para ver los errores registrados.")
