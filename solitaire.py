text = input("Write your text: ")

text = text.upper()
text = text.replace(" ", "")

alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W','X', 'Y', 'Z']

import random

card = random.randint(1, 28)
key = []

# deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
deck_of_cards = []

for i in range(1, 29):
    deck_of_cards.append(i)

random.shuffle(deck_of_cards)
l = deck_of_cards[len(deck_of_cards) - 1]
while deck_of_cards[0] == 27 or deck_of_cards[0] == 28 or l == 27 or l == 28:
    random.shuffle(deck_of_cards)
print(deck_of_cards)

for r in range(0, len(text)):
    for i in range(0, len(deck_of_cards)):
        if deck_of_cards[i] == 27:
            x = deck_of_cards.pop(i)
            deck_of_cards = deck_of_cards[:i + 1] + [x] + deck_of_cards[i + 1:]
            break

    print(deck_of_cards)

    for i in range(0, len(deck_of_cards)):
        if deck_of_cards[i] == 28:
            x = deck_of_cards.pop(i)
            deck_of_cards = deck_of_cards[:i + 2] + [x] + deck_of_cards[i + 2:]
            break

    print(deck_of_cards)

    d1 = 0
    d2 = 0
    for i in range(0, len(deck_of_cards)):
        if deck_of_cards[i] == 27:
            d1 = i
        if deck_of_cards[i] == 28:
            d2 = i

    if d2 > d1:
        deck_of_cards = deck_of_cards[d2 + 1:] + deck_of_cards[d1:d2 + 1] + deck_of_cards[:d1]
    else:
        deck_of_cards = deck_of_cards[d1 + 1:] + deck_of_cards[d2:d1 + 1] + deck_of_cards[:d2]

    last_card = deck_of_cards[len(deck_of_cards) - 1]

    if last_card == 27 or last_card == 28:
        last_card = 27

    taken_part = deck_of_cards[:last_card]

    print(taken_part)

    x = deck_of_cards.pop(27)
    deck_of_cards = deck_of_cards[last_card:] + taken_part + [x]
    print(deck_of_cards)

    first_card = deck_of_cards[0] % 28

    key.append(deck_of_cards[first_card])

    print("key:", key)

text = text.upper()

print(len(text))
print(len(alfabet))


def txt_to_code():
    txt1 = []
    for j in range(0, len(text)):
        for i in range(0, len(alfabet)):
            if text[j] == alfabet[i]:
                txt1.append(i)
    return txt1


print(txt_to_code())


def encryption():
    code = []
    txt2 = []
    for i in range(0, len(key)):
        code.append((txt_to_code()[i] + key[i]) % 26)

    for h in range(0, len(code)):
        txt2.append(alfabet[code[h]])
    return txt2

print("Do you want to encrypt the text? (Print 'yes' or 'no')")

answer = input()

while answer not in ["yes", 'no']:
    answer = input("Write your answer correctly")
if answer == "yes":
    print("Text encrypted: ", str(encryption()))
elif answer == "no":
    input()



def encryption_to_code():
    txt1 = []
    encryption_text = encryption()
    for j in range(0, len(encryption_text)):
        for i in range(0, len(alfabet)):
            if encryption_text[j] == alfabet[i]:
                txt1.append(i)
    return txt1


def decryption():
    code = []
    txt2 = []
    encryption_code = encryption_to_code()
    for i in range(0, len(key)):
        code.append((encryption_code[i] - key[i]) % 26)

    for h in range(0, len(code)):
        txt2.append(alfabet[code[h]])
    return txt2


print("Do you want to de encrypt the text? (Print 'yes' or 'no')")

answer_d = input()

while answer_d not in ["yes", 'no']:
    answer_d = input("Write your answer correctly")
if answer_d == "yes":
    print("Deencrypted text: ",
          str(decryption()))
elif answer_d == "no":
    input()

input()

