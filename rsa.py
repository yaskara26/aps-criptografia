import random
import math


# Encontra o máximo divisor comum entre dois números usando o algoritmo
# Euclidiano Estendido
def emdc(a: int, b: int) -> tuple:
    # Quando o resto for zero o código volta
    if a == 0:
        return (b, 0, 1)

    # Usando a recursividade para descobrir o mdc e os coeficientes de a e b
    m, y, x = emdc(b % a, a)
    # Retorna o mdc, o coeficiente de a e o coeficiente de b
    return (m, x - (b//a) * y, y)


# Checa se um número é primo
def e_primo(num) -> bool:
    if (num == 1 or num % 2 == 0):
        return False

    # Percorre todos os números ímpares até a raiz de num, se houve algum
    # divisor então num não é primo
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if (num % i == 0):
            return False
    return True


# Define o módulo multiplicativo
def modInverso(a, b) -> int:
    # Pegando o mdc e os coeficientes de a e b, porém o coeficiente y não é
    # importante
    mdc, x, _ = emdc(a, b)
    if mdc != 1:
        print("Não há modulo!")
        return 0

    # Retorna o módulo do coeficiente de a por b
    return x % b


# Gera um número aleatório ate que seja primo
def gerando_primos(minimo: int, maximo: int) -> int:
    primo = random.randint(minimo, maximo)
    # checa se um numero é primo se não for gera outro número e retorna à
    # verificação
    while (not e_primo(primo)):
        primo = random.randint(minimo, maximo)
    return primo


# gerando as chaves
def gerando_chaves() -> tuple:
    # gera dois números diferentes
    p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)
    p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)

    while p == q:
        p, q = gerando_primos(1000, 10000), gerando_primos(1000, 10000)

    # produto dos numeros primos
    n: int = p * q

    # totiente de n
    tot: int = (p-1)*(q-1)

    # escolhendo um numero 'e' que representa a primeira parte da public key |
    # 1 < e < tot e emdc(e, tot) = 1

    e: int = random.randint(2, tot-1)
    # checa se o emdc entre o totiente e o valor de e são co-primos
    while emdc(tot, e)[0] != 1:
        e = random.randint(2, tot-1)

    # encontrando o numero 'd' que representa a primeira parte da private key |
    # 'd' precisa ser um valor que torne | d*e mod tot = 1 | verdadeiro

    # Módulo inverso de e por tot
    d: int = modInverso(e, tot)

    # Retorna os valores das chaves públicas e privadas
    return (e, n), (d, n)

def gerar_chaves():
    chave_publica, chave_privada = gerando_chaves()

    print(f"Chave pública:\n {chave_publica[0]} {chave_publica[1]}\n")
    print(f"Chabe privada:\n {chave_privada[0]} {chave_privada[1]}\n")

def criptografar_mensagem():
    print('Digite uma mensagem de até 128 caractéres')
    mensagem_incorreta = True
    while mensagem_incorreta:
        message: str | list = input("Mensagem: ")

        mensagem_dentro_do_limite = len(message) <= 128
        if mensagem_dentro_do_limite:
            break
        print("mensagem muito comprida. Separe em duas mensagenss")

    print('Digite a chave no formato xxxx xxxx')

    while True:
        chave = input("Chave Pública -> ").strip().split(" ")
        if len(chave) == 2:
            break
        print('Digitou errado. Tente novamente no formato xxxx xxxx')

    e, n = int(chave[0]), int(chave[1])

    criptography: str = ''

    for char in message:
        encode: int = ord(char)
        c: str = str(pow(encode, e, n))
        criptography += c + ' '

    print(f"Texto criptografado:\n{criptography}\n")

def descriptografar_mensagem():
    message: str | list = input("Mensagem: ").split(' ')

    print('Digite a chave no formato xxxx xxxx')
    while True:
        chave = input("Chave Privada: ").split(" ")
        if len(chave) == 2:
            break
        print('Digitou errado. Tente novamente no formato xxxx xxxx')
    d, n = int(chave[0]), int(chave[1])

    descriptografado: str = ''

    for char in message:
        ch = pow(int(char), d, n)
        decode = chr(ch)
        descriptografado += decode

    print(f"Texto descriptografado:\n{descriptografado}\n")

while True:
    print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")

    opcao: str = input("> ").upper()

    while opcao not in "GCDS":
        print("Digite um valor válido")
        print("\nG -> Gerar chaves\nC -> Criptografia\nD -> Descriptografia\nS -> Sair")
        opcao = input("> ").upper()

    if (opcao == 'G'):
        gerar_chaves()

    elif (opcao == 'C'):
        criptografar_mensagem()

    elif (opcao == 'D'):
        descriptografar_mensagem()

    # Sair do programa
    elif (opcao == 'S'):
        print("Saindo...")
        break


