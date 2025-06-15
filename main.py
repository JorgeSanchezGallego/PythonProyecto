

from funciones import mostrar_menu, preguntas_colegio, cargar_test, preguntas_pokemon, test_colegio, test_pokemon, \
    test_futbol, usuario, clasificacion, ranking

opcion = -1

while opcion != 3:
    score = 0

    mostrar_menu()
    opcion = int(input("¿Cúal es tu opción?\n"))
    nick_name = usuario()
    print(nick_name)
    if opcion == 1:
        print("Valiente... Y bien, de que quieres el test")
        print("Preguntas del colegio")
        print("Pokemon")
        print("Fútbol")
        test_elegido = input("¿Por cual te decides?\n")
        if test_elegido == "Colegio":
            cargar_test(test_elegido)
            calificacion =test_colegio()

        elif test_elegido == "Pokemon":
            cargar_test(test_elegido)
            calificacion = test_pokemon()
        elif test_elegido == "Futbol":
            cargar_test(test_elegido)
            calificacion = test_futbol()

        print(f"Tu número total de aciertos es de: {calificacion} sobre 10 preguntas")
        porcentaje = (calificacion / 10)*100
        print(f"Tu porcentaje de aciertos es del {porcentaje:.2f}%")
        if calificacion < 5:
            print("Vas de máquina y suspendes")
        elif calificacion > 5 and calificacion< 7:
            print("Vas bien pero estudia más")
        elif calificacion > 7:
            print("Estás a un paso de la matricula de honor! ¡Adelante!")
        elif calificacion == 10:
            print("Matricula de honor, ¡enhorabuena!")

        clasificacion[nick_name] = calificacion

    elif opcion == 2:
        ranking()



