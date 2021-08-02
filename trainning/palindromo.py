#escrever uma string no teclado e escrevê-la de trás pra frente

name=input("me dê uma palavra e irei escrevê-la de trás para frente: ")

if name.upper()==name.upper()[::-1]: #na frente dos dois pontos é o início da string, entre os dois pontos é o fim, e o -1 é o passo a ser dado.
    print(f'a palavra {name.title()} é um palíndromo!')
else:
    print(f'a palavra {name.title()} não é um palíndromo!')