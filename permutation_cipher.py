
def fibo(index):
    a = 1
    b = 1
    if index in [0,1]:
        return a
    for i in range(index-1):
        a,b = b, a+b
    return b

def fibo_serie(plain_text):
    serie = []
    for i in range(len(plain_text)):
        serie.append(fibo(i)) 
    return serie

def general_serie(plain_text):
    serie = []
    seed = 1
    distance = 2
    n = len(plain_text)
    for i in range(len(plain_text)):
        serie.append(seed+(i-1)*distance)
    return serie


def serie_permutation(plain_text):
    # serie = fibo_serie(plain_text)
    serie = general_serie(plain_text)
    cipher_text = list(plain_text)
    n = len(plain_text)    
    for i in range(len(plain_text)):
        cipher_text[i],cipher_text[(i+serie[i])%n] = cipher_text[(i+serie[i])%n],cipher_text[i]
    return "".join(cipher_text)

def decrypt_permutation(encrypt_text):
    # serie = fibo_serie(encrypt_text)
    serie = general_serie(encrypt_text)
    decryp_text = list(encrypt_text)
    n = len(encrypt_text)
    for i in range(-1,-1*len(decryp_text)-1,-1):
        decryp_text[i],decryp_text[(i+serie[i])%n] = decryp_text[(i+serie[i])%n],decryp_text[i]
    return "".join(decryp_text)

if __name__ == "__main__":
    decript = decrypt_permutation("HLAO")
    print(decript)
    # encript = serie_permutation("HOLA")
    # print(encript)
















# def permutacion_por_series(mensaje, clave):
#     mensaje_cifrado = ""
#     n = len(clave)
#     bloques = [mensaje[i:i+n] for i in range(0, len(mensaje), n)]
#     for bloque in bloques:
#         mensaje_cifrado += "".join([bloque[i-1] for i in clave])
#     return mensaje_cifrado

# clave = [2, 4, 1, 3] # Clave de permutación
# mensaje = "HOLAMUNDO" # Mensaje de texto plano
# mensaje_cifrado = permutacion_por_series(mensaje, clave) # Cifrar mensaje
# print(mensaje_cifrado) # Imprimir mensaje cifrado

