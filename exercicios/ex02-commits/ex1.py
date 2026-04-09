#Questão 5 - Lista 1
#Ted Mosby e a Teoria do Guarda-Chuva Amarelo

ted_x1 = int(input())
ted_y1 = int(input())

guardaChuva_x2 = int(input())
guardaChuva_y2 = int(input())

amigo = input()

distancia = ((guardaChuva_x2 - ted_x1)**2 + (guardaChuva_y2 - ted_y1)**2) ** 0.5

#p/ Barney, a distância final é a distância calculada + 10
if amigo == "Barney":
    distanciaFinal = distancia+10
    print(f"Pelos meus cálculos a distância final encontrada foi {round(distanciaFinal)}!")
    if distanciaFinal <= 50:
        print("Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário"
            " que eu poderia até ter pego ele pra mim! Desafio aceito!")
    elif distanciaFinal > 50: 
        print("Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho "
              "para uma noite lendária! Challenge accepted, vista seu terno!")

#p/ Marshall, a distância final é a distância calculada - 5
elif amigo == "Marshall":
    distanciaFinal = distancia-5
    print(f"Pelos meus cálculos a distância final encontrada foi {round(distanciaFinal)}!")
    if distanciaFinal <= 50:
        print("Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar "
            "com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
    elif distanciaFinal > 50:
        print("Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa."
            " Vamos tentar de novo amanhã.")

#p/ Lily, a distância final é a distância calculada - 10
elif amigo == "Lily":
    distanciaFinal = distancia-10
    print(f"Pelos meus cálculos a distância final encontrada foi {round(distanciaFinal)}!")
    if distanciaFinal <= 50:
        print("Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. "
            "O guarda-chuva está aqui, e nem nos cansamos muito!")
    elif distanciaFinal > 50:
        print("Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! "
            "Fiquei com fome de tanta caminhada.")

#p/ Robin, a distância final é a distância calculada + 5
elif amigo == "Robin":
    distanciaFinal = distancia+5
    print(f"Pelos meus cálculos a distância final encontrada foi {round(distanciaFinal)}!")
    if distanciaFinal <= 50:
        print("Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. "
            "O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
    elif distanciaFinal > 50:
        print("Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")