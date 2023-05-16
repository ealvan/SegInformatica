disk1 = "ABCDEFGHIJKLMNOPQRSTUVXYWZ "
disk2 = "usqomkhfdbacgeilnprtxz&y@ñ?"

def alberti_cipher(plain_text,increment,shift,cycle):
    #delete process
    text = plain_text

    # increment = 1
    # shift = 0
    # cycle = 4
    cipher_text = ""

    n_disk2 = len(disk2)

    edit_disk1 = list(disk1)

    # to_cipher = list(plain_text)
    for idx in range(len(text)):
        if( idx != 0 and idx%cycle == 0):
            shift+=increment

        new_index = edit_disk1.index(text[idx].upper())
        new_char = disk2[(new_index+shift)%n_disk2]
        cipher_text+=new_char
    return cipher_text

def alberti_decrypt(encrypt_text,increment,shift,cycle):
    # increment = 1
    # shift = 0
    # cycle = 4
    decrypt_text = ""
    edit_disk2 = list(disk2)
    edit_encr_text = list(encrypt_text)
    n_disk1 =len(disk1)
    for idx in range(len(encrypt_text)):
        if( idx != 0 and idx%cycle == 0):
            shift+=increment

        encr_index = edit_disk2.index(edit_encr_text[idx].lower())
        origin_idx = encr_index - shift
        try:
            origin_char = disk1[origin_idx % n_disk1]
        except:
            # print("origin_encr_char:",edit_encr_text[idx])
            print("encr_char=",encrypt_text[idx])
            print("encr_index=",encr_index,"shift=",shift)
            print(origin_idx)
            origin_char = '<>'
        decrypt_text += origin_char
    return decrypt_text

import random 
if __name__ == "__main__":
    increment = random.randint(1,5)#2 1 5 5/ 1
    shift = random.randint(1,5)     #5 1 1 5/ 1
    cycle = random.randint(1,5)     #1 1 2 2/ 1
    message = "MY NAME IS LAWRENCE AND estoy muy feliz"
    print("Parameters:\n","increment=",increment, "shift=",shift,"cycle=", cycle)
    encr = alberti_cipher(message, increment, shift, cycle)
    print(message)
    print(encr)
    decr = alberti_decrypt(encr, increment, shift, cycle)
    print(decr)
    # plain_text = "ola amigos"
    # encrypted = "USQO OMKU"#usqo qmku #cduuadfgp CDUUADFGP
    # encr = alberti_cipher(plain_text)
    # print(encr)