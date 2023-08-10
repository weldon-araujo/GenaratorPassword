from string import ascii_letters, punctuation, digits, ascii_lowercase, ascii_uppercase
from random import choice

class Generate_Password:
    def __init__(self, tam, arg):
        self.tam = tam
        self.arg = arg
        self.l = 0

    def full(self):
        self.l = list
        if self.arg == '1':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + digits)
                #print(self.l, end='')
                return self.l
        elif self.arg == '2':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + punctuation)
                print(self.l, end='')
        elif self.arg == '3':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '4':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '5':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '6':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '7':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation)
                print(self.l, end='')
        elif self.arg == '8':
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '9':
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '10':
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '11':
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '12':
            for i in range(0, self.tam):
                self.l = choice(ascii_letters + punctuation + digits)
                print(self.l, end='')
        elif self.arg == '13':
            for i in range(0, self.tam):
                self.l = choice(punctuation)
                print(self.l, end='')
            