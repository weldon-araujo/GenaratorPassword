from string import ascii_letters, punctuation
from generator_class import Generate_Password


def answer_size():
    print('[\033[1;31mERROR\033[0;0m] MINIMUM SIZE OF 8 CHARACTERS AND MAXIMUM OF 40:')

def answer_letter():
    print('[\033[1;31mERROR\033[0;0m] NO LETTERS, SYMBOLS OR BLANK SPACES ALLOWED:]\033[0;0m   ')

def option():
    answer = input('''
    \033[1;31mPASSWORD STRENGTH OPTIONS:\033[0;0m
              
    [  1 ] CAPITAL LETTERS + SMALL LETTERS + NUMBERS 
    [  2 ] CAPITAL LETTERS + SMALL LETTERS + SYMBOLS
    [  3 ] CAPITAL LETTERS + SMALL LETTERS
    [  4 ] CAPITAL LETTERS  
    [  5 ] NUMBERS + SYMBOLS + CAPITAL LETTERS
    [  6 ] NUMBERS + SYMBOLS + SMALL LETTERS
    [  7 ] NUMBERS + SYMBOLS
    [  8 ] NUMEROS + CAPITL LETTERS
    [  9 ] NUMEROS + SMALL LETTERS
    [ 10 ] SYMBOLS + CAPITL LETTERS
    [ 11 ] SYMBOLS + SMALL LETTERS
    [ 12 ] ALL VALUES
    [ 13 ] SYMBOLS
    
    ''')

    return answer


size = 0
numbers = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26','27', '28', '29', '30','31','32','33','34','35','36','37','38','39','40',8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


while not size in numbers:
    size = input('PASSWORD LENGTH: ')
    if size in ascii_letters or size in punctuation:
        answer_letter()
    elif size not in numbers:
        answer_size()
    else:
        size = int(size)


instance = option()

esc_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

def end(): 
    if type(size) is int and size >= 8 and size <= 40:
        if instance in esc_number:
            arg = instance
            tam_ger = Generate_Password(size, arg)
            return tam_ger.full()

# with instance object "atual" of function end() i will to do a condition  
current_pass = end()

def strong_pass():
    pass
    
    