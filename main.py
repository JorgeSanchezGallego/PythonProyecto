

from funciones import mostrar_menu, preguntas_colegio, cargar_test, preguntas_pokemon, test_colegio, test_pokemon, \
    test_futbol, usuario, clasificacion, ranking, IndiceInvalido, mostrar_resultado, mostrar_test

opcion = -1

while opcion != 3:
    score = 0

    try:
        mostrar_menu()
        opcion = int(input("¿Cúal es tu opción?\n"))
        if opcion not in [1, 2, 3]:
            raise IndiceInvalido
    except ValueError:
        print("Por favor, introduce un número, no una palabra.")
        continue
    except IndiceInvalido:
        print("Error de indice")
        continue


    if opcion == 1:
        nick_name = usuario()
        mostrar_test(nick_name)
        try:
            test_elegido = int(input("¿Por cual te decides?\n"))
            if test_elegido not in [1, 2, 3]:
                raise IndiceInvalido
        except ValueError:
            print("Por favor, introduce un número, no una palabra.")
            continue
        except IndiceInvalido:
            print("Error de índice")
            continue

        if test_elegido == 1:
            cargar_test(test_elegido)
            calificacion =test_colegio()

        elif test_elegido == 2:
            cargar_test(test_elegido)
            calificacion = test_pokemon()
        elif test_elegido == 3:
            cargar_test(test_elegido)
            calificacion = test_futbol()
        else:
            print("Error de índice")
            continue

        mostrar_resultado(calificacion)

        clasificacion[nick_name] = calificacion

    elif opcion == 2:
        ranking()
    else:
        print("Apagando.")

print("Gracias por jugar!")




