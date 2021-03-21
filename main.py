number = input()
number_1 = list(number)


def size_correctness(number_1):
    '''
    Function detect correct size of card
    '''
    if 13 <= len(number_1) <= 16:
        return True
    else:
        return False


def opredelenie_kreditnoy_karti(number_1):
    '''
    Function detect company-owner of this card
    '''
    if number_1[0] == str(4):
        print("Карта - Visa")
        return True
    elif number_1[0] == str(5):
        print("Кредитная карта MasterCard")
        return True
    elif number_1[:2] == str(35):
        print("Карта - American Express")
        return True
    elif number_1[0] == str(2):
        print("Карта - Мир")
        return True
    else:
        print("ERROR")
        return False


def gans_lun(number_1):
    '''
    Function doing Gans Lun algorithm
    '''
    for i in range(0, len(number_1), 2):
        if int(number_1[i]) * 2 > 9:
            number_1[i] = str((int(number_1[i]) * 2 % 10) + (int(number_1[i]) * 2 // 10))
        else:
            number_1[i] = str(int(number_1[i]) * 2)
    card_sum = 0
    for i in number_1:
        card_sum += int(i)
    if card_sum % 10 == 0:
        return True
    else:
        return False
def check_card(number_1):
    if size_correctness(number_1) and \
    opredelenie_kreditnoy_karti(number_1) and \
    gans_lun(number_1):
        return True
    else :
        return False
print(check_card(number_1))