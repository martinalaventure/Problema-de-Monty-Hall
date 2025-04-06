import random

def MontyHall ( estrategia_elegida: bool):
    puertas=[1,2,3]
    puerta_auto= random.randint(1,3)
    puertas_para_abrir_Monty = []

    puerta_elegida_concursante= int(input("Elige una puerta del 1 al 3: "))


    while puerta_elegida_concursante not in puertas:
        puerta_elegida_concursante = int(input("Elige un numero entre 1 y 3"))
    
    for puerta in puertas:
        if puerta != puerta_auto and puerta != puerta_elegida_concursante:
            puertas_para_abrir_Monty.append(puerta)

    abrir_puerta_Monty = random.choice(puertas_para_abrir_Monty)

    print(f"Monty ha abierto la puerta {abrir_puerta_Monty}... ¡ES UNA CABRA!")

    puertas.remove(abrir_puerta_Monty)

    if estrategia_elegida:
        puertas.remove(puerta_elegida_concursante)
        eleccion_final = puertas[0]                     #Como el participante va a cambiar de puerta, entonces eliminamos la que ya eligió, por ende solo queda un valor posible
        print(f"Su nueva puerta es {eleccion_final}")
    else:
        eleccion_final = puerta_elegida_concursante
        print (f"Su puerta continúa siendo {eleccion_final}")
    
    if eleccion_final == puerta_auto:
        print("¡Felicidades has ganado un auto 🚗!")
        
    else: 
        print("Perdiste 😢, es una cabra 🐐")


    print("-----------------")
    print(f"Puerta elegida por el participante: {puerta_elegida_concursante}")
    print(f"Puerta donde está el auto: {puerta_auto}")
    print(f"Puerta abierta por el presentador: {abrir_puerta_Monty}")
    if estrategia_elegida:
        print(f"Su puerta cambió a: {eleccion_final}")
    if eleccion_final == puerta_auto:
        print("El participante ha ganado un auto 🚗")
        return True
    else: 
        print("El participante ha perdido, escogió una cabra 🐐")


def MontyHall_SinPrints ( estrategia_elegida: bool):
    puertas=[1,2,3]
    puerta_auto= random.randint(1,3)
    puertas_para_abrir_Monty = []

    puerta_elegida_concursante= random.randint(1,3)
    
    for puerta in puertas:
        if puerta != puerta_auto and puerta != puerta_elegida_concursante:
            puertas_para_abrir_Monty.append(puerta)

    abrir_puerta_Monty = random.choice(puertas_para_abrir_Monty)
    puertas.remove(abrir_puerta_Monty)

    if estrategia_elegida:
        puertas.remove(puerta_elegida_concursante)
        eleccion_final = puertas[0]
    else:
        eleccion_final = puerta_elegida_concursante
    
    if eleccion_final == puerta_auto:
        return True



def jugadas (n: int, estrategia_elegida: bool):
    juego_ganado = 0
    juego_perdido = 0
    n_original = n

    while n > 0:
        n -= 1
        if MontyHall_SinPrints(estrategia_elegida):
            juego_ganado +=1
        else: 
            juego_perdido +=1
    
    prob_ganado = juego_ganado / n_original
    prob_perdido = juego_perdido / n_original
    
    print(f"--------------------- {n_original} JUGADAS CON RESULTADOS ---------------------")
    
    print(f"Se han ganado {juego_ganado} veces, con una probabilidad de {prob_ganado}, siendo la estrategia de cambio {estrategia_elegida}")
    print(f"Se han perdido {juego_perdido} veces, con una probabilidad de {prob_perdido}, siendo la estrategia de cambio {estrategia_elegida}\n")

jugadas(1000, True)
jugadas(10000, True)
jugadas(100000, True)

jugadas(1000, False)
jugadas(10000, False)
jugadas(100000, False)




