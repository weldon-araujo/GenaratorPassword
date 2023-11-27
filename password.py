from string import ascii_letters, punctuation
from generator_class import Generate_Password
import re
import pyperclip


def answer_size():
    print('[\033[1;31mError\033[0;0m] Minium size of 8 characters and maximum of 40:')

def answer_letter():
    print('[\033[1;31mError\033[0;0m] No letters, symbols or blank spaces allowed:]\033[0;0m   ')


def option():
    while True:
        answer = input('''
            \033[1;31mPassword strength options:\033[0;0m
            
                    
            [  1 ] ABC + abc + 123 
            [  2 ] ABC + abc + #$&
            [  3 ] ABC + abc
            [  4 ] ABC  
            [  5 ] 123 + #$& + ABC
            [  6 ] 123 + #$& + abc
            [  7 ] 123 + #$&
            [  8 ] 123 + ABC
            [  9 ] 123 + abc
            [ 10 ] 123           
            [ 11 ] #$& + ABC
            [ 12 ] #$& + abc
            [ 13 ] #$&
            [ 14 ] ABC + abc + 123 + #$& 
            
                        
    ''')

        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= 14:
                return answer
    

size = 0
numbers = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26','27', '28', '29', '30','31','32','33','34','35','36','37','38','39','40',8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


while not size in numbers:
    size = input('Password length: ')
    if size in ascii_letters or size in punctuation:
        answer_letter()
    elif size not in numbers:
        answer_size()
    else:
        size = int(size)


instance = option()


esc_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def end(): 
    if type(size) is int and size >= 8 and size <= 40:
        if instance in esc_number:
            arg = instance
            tam_ger = Generate_Password(size, arg)
            return tam_ger.full()            


def verify8():

    if re.search(r'\d{8,9}',current_pass):
        print(f'[\033[1;31mWeak\033[0;0m] {current_pass}')
    elif re.search(r'[`;!@#\$%\^&*(),.?":{}|<>a-zA-Z0123456789]', current_pass):
        print(f'[\033[33mAverage\033[0;0m] {current_pass}')


def verify10():

    if re.search(r'\d{10,11}',current_pass):
        print((f'[\033[33mAverage\033[0;0m] {current_pass}'))
    elif re.search(r'[`;!@#\$%\^&*(),.?":{}|<>a-zA-Z0123456789]', current_pass):
        print(f'[\033[32mStrong\033[0;0m] {current_pass}')


def verify12():

    if re.search(r'\d{12,13}',current_pass):
        print((f'[\033[32mStrong\033[0;0m] {current_pass}'))
    elif re.search(r'[`;!@#\$%\^&*(),.?":{}|<>a-zA-Z0123456789]', current_pass):
        print(f'[\033[34mVery strong\033[0;0m] {current_pass}')


def verify13plus():

    if re.search(r'[`;!@#\$%\^&*(),.?":{}|<>a-zA-Z0123456789]', current_pass):
        print(f'[\033[34mVery strong\033[0;0m] {current_pass}')
    

current_pass = end()


if len(current_pass) in range(8,11):
    verify8()

elif len(current_pass) in range(10,12):
    verify10()

elif len(current_pass) in range(12,14):
    verify12()

elif len(current_pass) in range(14, 41):
    verify13plus()

issue = input('Do you want to copy password to transfer area ? digit [y] if yes ').lower()

if issue == 'y':

    pyperclip.copy(current_pass)
    print('Password copied')