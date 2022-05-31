import re


def backon_dict():
    """
    For 26 letters it is enough to have 5-bits to code
    Let's assume that a=0, b=1,... z=25
    Let's convert them to binary
    Let's take LAST 5 bits
    Let's add leading zeros to total length of 5 (2 => '10', we need '00010')
    Let's code 0 as A and 1 as B

    a => 0 => 00000000 => 00000 => aaaaa
    b => 1 => 00000001 => 00001 => aaaab

    z => 25 => 00011001 => 11001 => bbaab

    Structure is {'aaaaa': 'A'}
    """

    bacon_dict = {}

    for i in range(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        # chr(65)='a', chr(66)='b',...
        bacon_dict[tmp] = chr(65 + i)

    return bacon_dict


def bacon_reverse_dict():
    """
    Structure is {'A': 'aaaaa'}
    """
    return {v: k for k, v in bacon_dict.items()}


def prepare_string_to_encode(s: str) -> str:
    """
    Only capital letters is allowed
    """
    s = s.upper()
    return re.sub(r'[^A-Z]+', '', s)


def prepare_string_to_decode(s: str) -> str:
    """
    Only lower letters is allowed
    """
    s = s.lower()
    return re.sub(r'[^a-z]+', '', s)


def encode(words):
    cipher = ''

    words = prepare_string_to_encode(words)

    for i in words:
        cipher += bacon_reverse_dict.get(i).upper()
    return cipher


def decode(words):
    cipher = ''
    words = prepare_string_to_decode(words)
    chunks = [words[i:i + 5] for i in range(0, len(words), 5)]
    for i in chunks:
        cipher += bacon_dict.get(i, ' ')
    return cipher


if __name__ == '__main__':
    text = input("Write your text: ")
    bacon_dict = backon_dict()
    bacon_reverse_dict = bacon_reverse_dict()
    print(bacon_dict)
    print(bacon_reverse_dict)

    ciphertext = encode(text)

    print('Text encrypted: ' + ciphertext)
    print('Text de encrypted: ' + decode(ciphertext))
