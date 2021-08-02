#Given a word, compute the scrabble score for that word

#Letter                           Value
#A, E, I, O, U, L, N, R, S, T       1
#D, G                               2
#B, C, M, P                         3
#F, H, V, W, Y                      4
#K                                  5
#J, X                               8
#Q, Z                               10

tabela_l = []
tabela_letters = ['aeioulnrst', 'dg', 'bcmp', 'fhvwy', 'k', 'jx', 'qz']
tabela_scores = [1, 2, 3, 4, 5, 8, 10]
word = input("give me a name and I will tell you its value: ")
palavra =[] 

def split(word):
    palavra = [char for char in word]
    return palavra
    
def valuation(tabela_l):
    print(f'The letters has the following values: \n {tabela_scores} for the respective letters: {tabela_letters}')
    for words in tabela_letters:
        tabela_l.append(split(words))
    result = 0
    valores = tabela_l[:]
    palavra = split(word)      
    for c in range(int(len(valores))):
        for letters in palavra:
            if letters in valores[c]:
                print(f'the letter {letters} has the value of: {tabela_scores[c]}')
                result = tabela_scores[c] + result
    print(f'the word chosen values: {result}')

    
valuation(tabela_l)  
