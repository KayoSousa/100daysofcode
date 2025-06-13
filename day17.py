## day17 - Number of vowels in a string

# 1. write a function to count the number of vowels in a string.

def cont_vogais(texto):
    #Conta o número de vogais (a, e, i, o, u) em uma string.
    #A função ignora a diferença entre maiúsculas e minúsculas.

    #Args:
        #texto (str): A string na qual as vogais serão contadas.

    #Returns:
        #int: O número total de vogais encontradas na string.

    # 1. Definir as vogais (apenas minúsculas, pois converteremos o texto)    
    vogais = "aeiou"

    # 2. Inicializar um contador para as vogais
    contador = 0

    # 3. Iterar por cada caractere no texto
    #    Para garantir que a contagem seja case-insensitive,
    #    convertemos o caractere para minúsculo antes de verificar.
    for caractere in texto:
        # 4. Verificar se o caractere atual é uma vogal
        #    Usamos 'in' para verificar se o caractere está na nossa string 'vogais'.
        if caractere.lower() in vogais:
            # 5. Se for uma vogal, incrementamos o contador
            contador += 1 # É o mesmo que contador = contador + 1

    # 6. Retornar a contagem final
    return contador

