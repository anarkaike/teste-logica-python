# coding: utf-8
# Crie uma função que retorna todas as palavras de uma string na ordem inversa da frase original:
# Exemplo: fn("A frase inteira deve ser invertida") -> "revertida ser deve inteira frase as"
def reverse_sentence_words(string):
    arr_words = string.split()
    arr_len = len(arr_words)
    new_string = ''
    for i in range(arr_len-1, -1, -1):
        new_string = new_string + ' ' + arr_words[i]
    return new_string

print(reverse_sentence_words('A Frase inteira deve ser invertida'))