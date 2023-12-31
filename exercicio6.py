import math

#Em acústica: Para o cálculo do volume sonoro de um ambiente é adotada uma unidade chamada de Bell.
#Como o Bell é uma unidade muito grande adota-se o decibel. O ouvido humano não responde linearmente
#às intensidades sonoras, mas ao logaritmo desta intensidade sonora. A natureza assim construiu o ouvido
#de modo que ele possa detectar o ruído de uma simples folha caindo ao chão e suportar a explosão de uma
#bomba a poucos metros. Se a resposta fosse linear ao estímulo o ouvido seria destruído, como a resposta é
#logarítmica o ouvido suporta essa intensidade sonora muito maior.
#Assim podemos calcular estas relações através do conhecimento dos logaritmos. A fórmula que traduz a
#relação entre duas potencias sonoras, é dada na relação: Db = 10 log P2/P1, Sendo P2 e P1 (variação de
#potência, por exemplo em um alto-falante de 2 vezes. (Ex. P1 = 10 W, P2=20 W). Verificar quantos Db são
#necessários para dobrar a potência

# Potência inicial e potência final (dobrada)
P1 = 10  # Potência inicial em watts
P2 = 20  # Potência final em watts (dobrada)

# Cálculo dos decibéis
Db = 10 * math.log10(P2 / P1)

print(f"São necessários {Db:.2f} dB para dobrar a potência.")
