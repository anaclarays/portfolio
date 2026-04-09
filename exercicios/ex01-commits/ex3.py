#Questão 7 - Lista 1
#O desafio da calcualdora na Dunfer Mifflin (deve ser realizado em três linhas de código)

x,operador,y=int(input()),input(),int(input())
d={'+':x+y,'-':x-y,'*':x*y,'/':x//y}
print(d[operador] if operador in d and d[operador] is not None else "Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa.")