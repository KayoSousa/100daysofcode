## day16 - Palindrome String

# 1. write a function to check if a given string is a palindrome.

def eh_palindromo(texto):
    """
    Verifica se uma string é um palíndromo, ignorando maiúsculas/minúsculas,
    espaços e pontuações.

    Args:
        texto (str): A string a ser verificada.

    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    # Passo 1: Limpar a string
    # Converter toda a string para minúsculas
    texto_limpo = texto.lower()

    # Remover caracteres não alfanuméricos (como espaços, pontuações, etc.)
    # O método .isalnum() retorna True se o caractere é uma letra ou um número.
    texto_filtrado = ""
    for caractere in texto_limpo:
        if caractere.isalnum():
            texto_filtrado += caractere

    # Passo 2: Inverter a string filtrada
    # O fatiamento [::-1] é uma forma concisa de inverter uma string em Python.
    texto_invertido = texto_filtrado[::-1]

    # Passo 3: Comparar a string filtrada original com a invertida
    # Se forem iguais, é um palíndromo; caso contrário, não é.
    return texto_filtrado == texto_invertido

# --- Exemplos de uso da função ---

# Testes com palavras e frases
print(f"'ovo' é palíndromo? {eh_palindromo('ovo')}") # Saída esperada: True
print(f"'arara' é palíndromo? {eh_palindromo('arara')}") # Saída esperada: True
print(f"'Python' é palíndromo? {eh_palindromo('Python')}") # Saída esperada: False
print(f"'Radar' é palíndromo? {eh_palindromo('Radar')}") # Saída esperada: True (ignora maiúsculas/minúsculas)
print(f"'A sacada da casa' é palíndromo? {eh_palindromo('A sacada da casa')}") # Saída esperada: True
print(f"'A torre da derrota' é palíndromo? {eh_palindromo('A torre da derrota')}") # Saída esperada: True
print(f"'Socorram-me, subi no ônibus em Marrocos' é palíndromo? {eh_palindromo('Socorram-me, subi no ônibus em Marrocos')}") # Saída esperada: True
print(f"'Hello World' é palíndromo? {eh_palindromo('Hello World')}") # Saída esperada: False
print(f"'121' é palíndromo? {eh_palindromo('121')}") # Saída esperada: True (funciona com números como strings)
print(f"'No lemon, no melon.' é palíndromo? {eh_palindromo('No lemon, no melon.')}") # Saída esperada: True

# --- Interação com o usuário ---
print("\n--- Verificador de Palíndromos Interativo ---")
while True:
    entrada_usuario = input("Digite uma palavra ou frase (ou 'sair' para encerrar): ")
    if entrada_usuario.lower() == 'sair':
        break
    
    if eh_palindromo(entrada_usuario):
        print(f"'{entrada_usuario}' É um palíndromo (considerando apenas letras/números)!")
    else:
        print(f"'{entrada_usuario}' NÃO é um palíndromo (considerando apenas letras/números)!")
    print("-" * 30) # Linha divisória para clareza

print("Programa encerrado. Até mais!")

