def mostrar_menu():
    print("Hola! Bienvenid@  al test más random que puedas ver!")
    print("### MENÚ ###")
    print("Marca un número para realizar esa opción")
    print("1 - Empezar test random!")
    print("2 - Ranking")
    print("3 - Apagar!")

def cargar_test(opcion):
    if opcion == "Colegio":
        print("Has elegido el test de nivel parbulario! Eres un machote!")
    elif opcion =="Pokemon":
        print("Wow! Ahora me vas a demostrar tus conocimientos de Pokemon!")
    elif opcion == "Futbol":
        print("Me lo esperaba, a quien no le gusta el fútbol!")
    else:
        print("Test no encontrado")

def test_colegio():
        score = 0
        print("Vamos con las preguntas!")
        for numero, datos in preguntas_colegio.items():
            print(f"Pregunta número {numero}")
            print(datos['pregunta'])
            for indice, valor in enumerate(datos['opciones'], 1):
                print(f"{indice}. {valor}")
            respuesta_usuario = int(input("Dime el indice de tu respuesta!\n"))
            respuesta_posicion = datos['opciones'][respuesta_usuario - 1]
            if respuesta_posicion == datos['respuesta_correcta']:
                print("¡Correcto!")
                score += 1
            else:
                print("Incorrecto!")
        return score


def test_pokemon():
    score = 0
    print("Vamos con las preguntas!")
    for numero, datos in preguntas_pokemon.items():
        print(f"Pregunta número {numero}")
        print(datos['pregunta'])
        for indice, valor in enumerate(datos['opciones'], 1):
            print(f"{indice}. {valor}")
        respuesta_usuario = int(input("Dime el indice de tu respuesta!\n"))
        respuesta_posicion = datos['opciones'][respuesta_usuario - 1]
        if respuesta_posicion == datos['respuesta_correcta']:
            print("¡Correcto!")
            score += 1
        else:
            print("Incorrecto!")
    return score

def test_futbol():
    score = 0
    print("Vamos con las preguntas!")
    for numero, datos in preguntas_futbol.items():
        print(f"Pregunta número {numero}")
        print(datos['pregunta'])
        for indice, valor in enumerate(datos['opciones'], 1):
            print(f"{indice}. {valor}")
        respuesta_usuario = int(input("Dime el indice de tu respuesta!\n"))
        respuesta_posicion = datos['opciones'][respuesta_usuario - 1]
        if respuesta_posicion == datos['respuesta_correcta']:
            print("¡Correcto!")
            score += 1
        else:
            print("Incorrecto!")
    return score


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

def get_respuesta():
    respuesta = input("Es tu momento! Elige bien!\n")
    return respuesta







