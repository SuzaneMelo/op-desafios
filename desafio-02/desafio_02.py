#lista inicial
lista_numeros = [x for x in range(10000)]

#lista que recebe os numeros primos da lista inicial
lista_primos = list()

#lista de divisores, exceto 0
lista_divisores = [x for x in lista_numeros if x != 0]

#iteracaode cada item da lista de divisores
for number in lista_numeros:

	#lsta de variavel que recebe a quantidade de divisores dps numeros, se valor = 2, numero é primo
    soma_divisores = 0
    
	#realização das divisões
	for divisor in lista_divisores:
        
		#condicional para verificação se o resto da divisao é divisors de 0
		if number % divisor == 0:

			#incremento da qquantidade de divisores
            soma_divisores += 1

		#condição de parada para quando divisor for maior que dividendo	
        elif number < divisor:
            break
    #final das iterações, se a soma dos divisores for 2 o numero é primo
	if soma_divisores == 2:
        lista_primos.append(number)
print(lista_primos)