saldo = 1000

while True:
    print('consultar saldo: ')
    print('depositar dinero: ')
    print('retirar dinero: ')
    print('salir: ')
    opcion =  input('elije una opcion: ')
    if opcion == '1':
        print(f"tu saldo actual es: ${saldo} dolares. ")
    elif opcion == '2':
        deposito = int(input("¿cuanto deseas depositar: ?"))
        saldo += deposito
        print(f"¡Depósito exitoso! Tu nuevo saldo es: ${saldo} dolares.")
    elif opcion=='3':
       print('has seleccionado: retirar dinero.')
       retiro = int(input("¿cuanto dinero deseas retirar: ?"))
       if retiro <= saldo:
           saldo -= retiro
           print(f"✅ ¡Retiro exitoso! Has retirado ${retiro}. Tu saldo actual es de ${saldo}.")
       else:
           print("saldo insuficiente: ")
    elif opcion == '4':
        print("gracias por usar nuestro cajero. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige un número del 1 al 4.")
    
    