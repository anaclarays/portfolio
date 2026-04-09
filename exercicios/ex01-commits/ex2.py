#Questão 6 - Lista 1
# A auditoria do Comitê de Planejamento de Festas (CPF)

n = input()
valor = float(input())
r = input()
e = input()

# tratamento de variável
nome = n.lower()
responsavel = r.lower()
evento = e.lower()

if valor > 100:
    if responsavel == "angela":
        print("Compra Aprovada!")
        print("Apenas eu tenho discernimento para gastos desta magnitude.")
    else:
        print("Compra Reprovada!")
        print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")

elif valor <= 100:
    if responsavel == "angela":
        print("Compra Aprovada!")
        print("Compra feita por mim, obviamente dentro dos padrões de excelência.")

    # Regras Michael Scott
    elif responsavel == "michael":
        if nome == "mágica" or nome == "fantasia":
            print("Compra Reprovada!")
            print("O Comitê não financia frivolidades e palhaçadas, Michael.")
        elif valor > 60:
            print("Compra Aprovada com ressalvas!")
            if evento == "natal":
                print(
                    "O espírito natalino de Michael é... excessivo. A nota será conferida.")
            elif evento == "aniversário":
                print(
                    "Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
        elif valor <= 60:
            print("Compra Aprovada!")
            print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")

    # Regras tipo de evento
    elif evento == "halloween":
        if nome == "abóbora" and valor <= 30:
            print("Compra Aprovada!")
            print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
        elif nome == "abóbora" and valor > 30:
            print("Compra Aprovada com ressalvas!")
            print("Por que uma abóbora precisa ser tão cara? Extravagância.")
        else:
            print("Compra Aprovada com ressalvas!")
            print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")

    elif evento == "aniversário":
        if nome == "bolo" and valor <= 40:
            print("Compra Aprovada!")
            print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
        elif nome == "sorvete de menta com chocolate":
            print("Compra Reprovada!")
            print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
        else:
            print("Compra Aprovada!")
            print(
                "Itens de aniversário devem ser práticos, não uma distração do trabalho.")

    elif valor > 50:
        print("Compra Aprovada com ressalvas!")
        print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")
    elif valor <= 50:
        print("Compra Aprovada!")
        print("Esta compra não viola nenhum regulamento... por enquanto.")
