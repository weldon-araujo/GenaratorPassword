from string import ascii_letters, punctuation, digits, ascii_lowercase, ascii_uppercase
from random import choice

class Generate_Password:
    def __init__(self, tam, arg):
        self.tam = tam
        self.arg = arg
        self.l = 0
        

    def full(self):
        self.l = list()    
        self.liste = []

        if self.arg == 1:
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + digits)
                self.liste.append(self.l)
            return ''.join(self.liste)
                
                
        elif self.arg == 2:
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + punctuation)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 3:
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 4:
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 5:
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_uppercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 6:
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_lowercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 7:
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 8:
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_uppercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 9:
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_lowercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 10:
            for i in range(0, self.tam):
                self.l = choice(digits)
                self.liste.append(self.l)
            return ''.join(self.liste)
        
        elif self.arg == 11:
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_uppercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 12:
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_lowercase)
                self.liste.append(self.l)
            return ''.join(self.liste)

        elif self.arg == 13:
            for i in range(0, self.tam):
                self.l = choice(punctuation)
                self.liste.append(self.l)
            return ''.join(self.liste)
        
        elif self.arg == 14:
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + punctuation + digits)
                self.liste.append(self.l)
            return ''.join(self.liste)   
            