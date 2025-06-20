import time
from colorama import Fore, Style

class IndiceInvalido(Exception): # Define una clase de excepción personalizada para manejar índices fuera de rango

    pass


def usuario(): # Pide al usuario que escriba su nickname
    nick_name = input("¿Cual es tu nickname? 💥\n")
    return nick_name # Devuelve el nickname introducido

def mostrar_test(nickname): # Muestra las opciones de test disponibles
    print(f"Eres valiente {nickname}... Y bien, de que quieres el test  😄")
    time.sleep(0.5)
    print("1- Preguntas del colegio 😱")
    time.sleep(0.5)
    print("2- Pokemon 🤓")
    time.sleep(0.5)
    print("3- Fútbol 🤪")

def mostrar_resultado(calificacion): # Muestra los resultados del test con mensajes según el rendimiento
    time.sleep(0.5)
    print(f"Tu número total de aciertos es de: {calificacion} sobre 10 preguntas ✅")
    porcentaje = (calificacion / 10) * 100 # Calcula el porcentaje de aciertos
    time.sleep(0.5)
    print(f"Tu porcentaje de aciertos es del {porcentaje:.2f}% 💥")
    time.sleep(0.5)
    if calificacion < 5: # Mensajes personalizados según la puntuación
        print(Fore.RED +"Vas de máquina y suspendes ⛔", Style.RESET_ALL)
    elif 5 <= calificacion < 7:
        print(Fore.YELLOW +"Vas bien pero estudia más 🉑", Style.RESET_ALL)
    elif 7 <= calificacion < 10:
        print("Estás a un paso de la matricula de honor! ¡Adelante! ✅")
    elif calificacion == 10:
        print("Matricula de honor, ¡enhorabuena! 💯")


def mostrar_menu(): # Muestra el menú principal del programa
    print(Fore.BLUE + "Hola! Bienvenid@  al test más random que puedas ver! ✨")
    time.sleep(0.3)
    print("🎈🎈🎈 MENÚ 🎈🎈🎈")
    time.sleep(0.3)
    print("Marca un número para realizar esa opción ✅" ,Style.RESET_ALL)
    time.sleep(0.3)
    print("1️ - Test random!")
    time.sleep(0.3)
    print("2️⃣ - Ranking!")
    time.sleep(0.3)
    print("3️⃣ - Apagar!")

def cargar_test(opcion): # Muestra un mensaje dependiendo del test seleccionado
    if opcion == 1:
        print("🙄 Has elegido el test de nivel parbulario! Eres un machote! 🤐")
    elif opcion == 2:
        print("👻 Wow! Ahora me vas a demostrar tus conocimientos de Pokemon! 🤯")
    elif opcion == 3:
        print("⚽ Me lo esperaba, a quien no le gusta el fútbol! 😎")
    else:
        print(Fore.RED +"❌ Test no encontrado ❌", Style.RESET_ALL)

def test_colegio(): # Función para hacer el test de preguntas del colegio
        score = 0 # Contador de respuestas correctas
        print(Fore.BLUE+"Vamos con las preguntas❗", Style.RESET_ALL)
        time.sleep(0.5)
        for numero, datos in preguntas_colegio.items(): # Itera sobre las preguntas del diccionario
            print(f"Pregunta número {numero} 💫") # Muestra el número de pregunta
            print(datos['pregunta']) # Muestra el texto de la pregunta
            for indice, valor in enumerate(datos['opciones'], 1): # Muestra las opciones enumeradas desde 1
                time.sleep(0.5)
                print(f"{indice}. {valor}") # Imprime cada opción
            try:
                time.sleep(0.5)
                respuesta_usuario = int(input("Dime el indice de tu respuesta! 📵\n"))
                if respuesta_usuario not in [1, 2, 3, 4]: # Verifica si el índice es válido
                    raise IndiceInvalido # Lanza excepción personalizada si no es válido
            except ValueError: # Captura si el input no es un número
                print(Fore.RED +" ❌ Por favor, introduce un numero del 1 al 4. ❌", Style.RESET_ALL)
                break
            except IndiceInvalido:
                print(Fore.RED +"❌ Error de índice. ❌", Style.RESET_ALL)
                break

            respuesta_posicion = datos['opciones'][respuesta_usuario - 1]# Obtiene el texto de la respuesta elegida
            if respuesta_posicion == datos['respuesta_correcta']: # Compara con la correcta
                print(Fore.GREEN +"✅ ¡Correcto! ✅", Style.RESET_ALL)
                score += 1 # Aumenta el marcador
                time.sleep(0.5)
            else:
                print(Fore.RED +"❌ ¡Incorrecto! ❌", Style.RESET_ALL)
                time.sleep(0.5)
        return score  # Devuelve el total de respuestas correctas


def test_pokemon():
    score = 0 # Contador de respuestas correctas
    print(Fore.BLUE+"Vamos con las preguntas❗", Style.RESET_ALL)
    time.sleep(0.5)
    for numero, datos in preguntas_pokemon.items(): # Itera sobre las preguntas del diccionario
        print(f"Pregunta número {numero} 💫") # Muestra el número de pregunta
        print(datos['pregunta']) # Muestra el texto de la pregunta
        for indice, valor in enumerate(datos['opciones'], 1): # Muestra las opciones enumeradas desde 1
            time.sleep(0.5)
            print(f"{indice}. {valor}") # Imprime cada opción
        try:
            time.sleep(0.5)
            respuesta_usuario = int(input("Dime el indice de tu respuesta! 📵\n"))
            if respuesta_usuario not in [1, 2, 3, 4]: # Verifica si el índice es válido
                raise IndiceInvalido # Lanza excepción personalizada si no es válido
        except ValueError: # Captura si el input no es un número
            print(Fore.RED +"❌ Por favor, introduce un numero del 1 al 4 ❌", Style.RESET_ALL)
            break
        except IndiceInvalido:
            print(Fore.RED +"❌ Error de índice ❌", Style.RESET_ALL)
            break

        respuesta_posicion = datos['opciones'][respuesta_usuario - 1] # Obtiene el texto de la respuesta elegida
        if respuesta_posicion == datos['respuesta_correcta']: # Compara con la correcta
            time.sleep(0.5)
            print(Fore.GREEN +"✅ ¡Correcto! ✅", Style.RESET_ALL)
            score += 1 # Aumenta el marcador
        else:
            time.sleep(0.5)
            print(Fore.RED +"❌ ¡Incorrecto! ❌", Style.RESET_ALL)
    return score  # Devuelve el total de respuestas correctas

def test_futbol():
    score = 0 # Contador de respuestas correctas
    print(Fore.BLUE+"Vamos con las preguntas❗", Style.RESET_ALL)
    time.sleep(0.5)
    for numero, datos in preguntas_futbol.items(): # Itera sobre las preguntas del diccionario
        print(f"Pregunta número {numero} 💫") # Muestra el número de pregunta
        print(datos['pregunta']) # Muestra el texto de la pregunta
        for indice, valor in enumerate(datos['opciones'], 1): # Muestra las opciones enumeradas desde 1
            time.sleep(0.5)
            print(f"{indice}. {valor}") # Imprime cada opción
        try:
            time.sleep(0.5)
            respuesta_usuario = int(input("Dime el indice de tu respuesta! 📵\n"))
            if respuesta_usuario not in [1, 2, 3, 4]: # Verifica si el índice es válido
                raise IndiceInvalido # Lanza excepción personalizada si no es válido
        except ValueError: # Captura si el input no es un número
            print(Fore.RED +"❌ Por favor, introduce un numero del 1 al 4 ❌", Style.RESET_ALL)
            break
        except IndiceInvalido:
            print(Fore.RED +"❌ Error de índice ❌", Style.RESET_ALL)
            break

        respuesta_posicion = datos['opciones'][respuesta_usuario - 1] # Obtiene el texto de la respuesta elegida
        if respuesta_posicion == datos['respuesta_correcta']: # Compara con la correcta
            time.sleep(0.5)
            print(Fore.GREEN +"✅ ¡Correcto! ✅", Style.RESET_ALL)
            score += 1 # Aumenta el marcador
        else:
            time.sleep(0.5)
            print(Fore.RED +"❌ ¡Incorrecto! ❌", Style.RESET_ALL)
    return score  # Devuelve el total de respuestas correctas

def ranking ():

    print(Fore.MAGENTA+"Bienvenido a nuestro top 5! 🏆", Style.RESET_ALL)

    for clave in clasificacion:
        time.sleep(0.5)
        print(Fore.YELLOW + f"{clave}: {clasificacion.get(clave)} aciertos!✅", Style.RESET_ALL)



clasificacion = {}

preguntas_colegio = {
        1:{
            "pregunta" : "¿Cúal es el rio más largo del mundo?",
            "opciones" : ["Nilo", "Amazonas", "Segura", "Ebro"],
            "respuesta_correcta" : "Amazonas"
        },
        2: {
            "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
            "opciones": ["Miguel de Cervantes", "Pablo Neruda", "ElRubiusOMG", "Willyrex"],
            "respuesta_correcta": "Miguel de Cervantes"
        },
        3: {
            "pregunta": "¿Cuál es la capital de Francia?",
            "opciones": ["Londres", "Madrid", "Roma", "París"],
            "respuesta_correcta": "París"
        },
        4: {
            "pregunta": "¿Qué órgano del cuerpo humano bombea la sangre?",
            "opciones": ["Pulmones", "Cerebro", "Corazón", "Hígado"],
            "respuesta_correcta": "Corazón"
        },
        5: {
            "pregunta": "¿Cuál es el resultado de 7 x 8?",
            "opciones": ["56", "48", "54", "64"],
            "respuesta_correcta": "56"
        },
        6: {
            "pregunta": "¿¿Cuál es el océano más grande del mundo?",
            "opciones": ["Atlántico", "Índico", "Ártico", "Pacífico"],
            "respuesta_correcta": "Pacífico"
        },
        7: {
            "pregunta": "¿Qué número romano representa al 10?",
            "opciones": ["V", "X", "L", "C"],
            "respuesta_correcta": "X"
        },
        8:{
            "pregunta": "¿Cuántos planetas hay en el sistema solar?",
            "opciones": ["7", "8", "9", "10"],
            "respuesta_correcta": "8"
        },
        9: {
            "pregunta": "¿Cuántos continentes hay en la Tierra?",
            "opciones": ["5", "6", "7", "8"],
            "respuesta_correcta": "7"
        },
        10: {
            "pregunta": "¿Qué gas respiramos que es esencial para vivir?",
            "opciones": ["Oxígeno", "Dióxido de carbono", "Nitrógeno", "Hidrógeno"],
            "respuesta_correcta": "Oxígeno"
        }
    }

preguntas_pokemon = {
        1: {
            "pregunta": "¿Cuál es el Pokémon número 25 en la Pokédex nacional?",
            "opciones": ["Charmander", "Squirtle", "Pikachu", "Bulbasaur"],
            "respuesta_correcta": "Pikachu"
        },
        2: {
            "pregunta": "¿Qué tipo es Charizard?",
            "opciones": ["Fuego", "Fuego/Volador", "Dragón", "Volador"],
            "respuesta_correcta": "Fuego/Volador"
        },
        3: {
            "pregunta": "¿Quién es el rival de Ash en la serie original?",
            "opciones": ["James", "Gary", "Brock", "Tracey"],
            "respuesta_correcta": "Gary"
        },
        4: {
            "pregunta": "¿Qué Pokémon puede evolucionar en Vaporeon, Jolteon o Flareon?",
            "opciones": ["Eevee", "Ditto", "Pikachu", "Meowth"],
            "respuesta_correcta": "Eevee"
        },
        5: {
            "pregunta": "¿Cuál es el tipo más fuerte contra el tipo Agua?",
            "opciones": ["Fuego", "Tierra", "Planta", "Bicho"],
            "respuesta_correcta": "Planta"
        },
        6: {
            "pregunta": "¿Qué Pokémon es conocido por decir solo su nombre?",
            "opciones": ["Snorlax", "Jigglypuff", "Pikachu", "Meowth"],
            "respuesta_correcta": "Pikachu"
        },
        7: {
            "pregunta": "¿Qué legendario forma parte del trío de aves junto a Articuno y Zapdos?",
            "opciones": ["Lugia", "Ho-Oh", "Moltres", "Mewtwo"],
            "respuesta_correcta": "Moltres"
        },
        8: {
            "pregunta": "¿Qué color es el cuerpo de Bulbasaur?",
            "opciones": ["Verde claro", "Azul", "Verde oscuro", "Gris"],
            "respuesta_correcta": "Verde claro"
        },
        9: {
            "pregunta": "¿Qué Pokémon tiene una pokebola en la cara?",
            "opciones": ["Electrode", "Voltorb", "Koffing", "Gengar"],
            "respuesta_correcta": "Voltorb"
        },
        10: {
            "pregunta": "¿Quién es el profesor Pokémon de la región Kanto?",
            "opciones": ["Profesor Elm", "Profesor Oak", "Profesor Birch", "Profesor Kukui"],
            "respuesta_correcta": "Profesor Oak"
        }
    }


preguntas_futbol = {
        1: {
            "pregunta": "¿Cuántos jugadores tiene un equipo de fútbol en el campo?",
            "opciones": ["9", "10", "11", "12"],
            "respuesta_correcta": "11"
        },
        2: {
            "pregunta": "¿En qué país nació Lionel Messi?",
            "opciones": ["Brasil", "España", "Argentina", "Uruguay"],
            "respuesta_correcta": "Argentina"
        },
        3: {
            "pregunta": "¿Qué jugador es apodado 'CR7'?",
            "opciones": ["Cristiano Ronaldo", "Carlos Rodríguez", "Carlos Reinoso", "Cristian Romero"],
            "respuesta_correcta": "Cristiano Ronaldo"
        },
        4: {
            "pregunta": "¿Qué selección ganó el Mundial de 2018?",
            "opciones": ["Argentina", "Brasil", "Francia", "Alemania"],
            "respuesta_correcta": "Francia"
        },
        5: {
            "pregunta": "¿Cuánto dura un partido de fútbol profesional?",
            "opciones": ["60 minutos", "75 minutos", "90 minutos", "105 minutos"],
            "respuesta_correcta": "90 minutos"
        },
        6: {
            "pregunta": "¿Qué jugador tiene más goles en la historia de los mundiales?",
            "opciones": ["Pelé", "Miroslav Klose", "Ronaldo Nazário", "Messi"],
            "respuesta_correcta": "Miroslav Klose"
        },
        7: {
            "pregunta": "¿Qué equipo tiene más Copas del Mundo ganadas?",
            "opciones": ["Italia", "Argentina", "Brasil", "Alemania"],
            "respuesta_correcta": "Brasil"
        },
        8: {
            "pregunta": "¿Cómo se llama el estadio del Real Madrid?",
            "opciones": ["Camp Nou", "Old Trafford", "Santiago Bernabéu", "Anfield"],
            "respuesta_correcta": "Santiago Bernabéu"
        },
        9: {
            "pregunta": "¿Qué posición juega el portero?",
            "opciones": ["Delantero", "Defensa", "Arquero", "Mediocampista"],
            "respuesta_correcta": "Arquero"
        },
        10: {
            "pregunta": "¿Qué país organizó la Copa Mundial de 2022?",
            "opciones": ["Rusia", "Qatar", "EE.UU.", "Alemania"],
            "respuesta_correcta": "Qatar"
        }
    }









