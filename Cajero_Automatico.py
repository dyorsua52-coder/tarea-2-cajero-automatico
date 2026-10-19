# TAREA 2 : Cajero Automático
# Estudiante
# Dylan Garos Quesada 
# Constantes
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# Variables iniciales
saldo = SALDO_INICIAL
contador = 0
continuar = input("¿Desea realizar un retiro? (s/n): ").lower()

# Ciclo principal
while continuar == "s" and saldo >= RETIRO_MINIMO:
    monto = int(input("¿Cuánto desea retirar? "))

    if monto >= RETIRO_MINIMO and monto <= RETIRO_MAXIMO and monto <= saldo:
        saldo = saldo - monto
        contador = contador + 1
        print("Retiro aprobado.")
    else:
        print("Retiro rechazado. Revise el monto o el saldo.")

    print("Saldo disponible:", saldo)

    if saldo >= RETIRO_MINIMO:
        continuar = input("¿Desea realizar otro retiro? (s/n): ").lower()
    else:
        continuar = "n"

# Resultado final
print("Saldo final:", saldo)
print("Retiros exitosos:", contador)