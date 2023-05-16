import unittest
from permutation_cipher import serie_permutation,decrypt_permutation
from alberti_decipher import alberti_cipher, alberti_decrypt
import random

class TestPermutationCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = serie_permutation
        self.decrypt = decrypt_permutation
    def test_alfanumeric(self):
        message = "HOLA"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)

    def test_greeting(self):
        message = "HOLA BEST FRIEND!"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)
    
    def test_special_characters(self):
        message = "HóLa Mejor ñiño!"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)
    
    def test_email(self):
        message = "correo12321_=??@gmail.com"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)
    
    def test_break_lines(self):
        message = "Pepe \n el mejor \t amigo del mundo"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)

    def test_emoticons(self):
        message = "🐍🐍😊😊🐍🐍😊😊🐍🐍"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)

    def test_unicode(self):
        message = "\U0001F929 \U0001F617 \U0001F911"
        encr = self.cipher(message)
        decr = self.decrypt(encr)
        self.assertEqual(message,decr)
#from alberti_decipher import alberti_cipher, alberti_decrypt
class TestAlbertiEncryption(unittest.TestCase):
    def setUp(self):
        self.cipher = alberti_cipher
        self.decryp = alberti_decrypt
        self.increment = 1
        self.cycle = 4
        self.shift = 0
    def test_simple(self):
        message = "HOLA AMIGOS"
        encr = self.cipher(message,self.increment,self.shift,self.cycle)
        decr = self.decryp(encr,self.increment,self.shift,self.cycle)
        self.assertEqual(message,decr)

    def test_large_text(self):
        message = "HELLO WORLD MY FRIEND"
        encr = self.cipher(message,self.increment,self.shift,self.cycle)
        decr = self.decryp(encr,self.increment,self.shift,self.cycle)
        self.assertEqual(message,decr)

    def test_different_parameters(self):
        self.increment = 2
        self.cycle = 3
        self.shift = 1
        message = "HELLO WORLD MY FRIEND"
        encr = self.cipher(message,self.increment,self.shift,self.cycle)
        decr = self.decryp(encr,self.increment,self.shift,self.cycle)
        self.assertEqual(message,decr)

    def test_different_parameters_hard(self):
        self.increment = 2
        self.cycle = 5
        self.shift = 2
        message = "MY NAME IS LAWRENCE AND estoy muy feliz"
        encr = self.cipher(message,self.increment,self.shift,self.cycle)
        decr = self.decryp(encr,self.increment,self.shift,self.cycle)
        self.assertEqual(message.lower(),decr.lower())
    def test_different_parameters_very_hard(self):
        self.increment = random.randint(1,5)
        self.cycle = random.randint(1,5)
        self.shift = random.randint(1,5)
        message = "MY NAME IS LAWRENCE AND estoy muy feliz"
        encr = self.cipher(message,self.increment,self.shift,self.cycle)
        decr = self.decryp(encr,self.increment,self.shift,self.cycle)
        self.assertEqual(message.lower(),decr.lower())

if __name__ == "__main__":
    unittest.main() 
    
        
