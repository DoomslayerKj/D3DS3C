
my_dict = {
        0: 'q', 1: 'e', 2: '5', 3: 't',
        4: 'u', 5: '4', 6: 'o', 7: 'a',
        8: '7', 9: 'd', 10: 'g', 11: '8',
        12: 'j', 13: 'l', 14: '6', 15: '9',
        16: 'z', 17: 'c', 18: 'b', 19: 'm',
        20: 'w', 21: '3', 22: 'r', 23: 'y',
        24: '1', 25: 'i', 26: 'p', 27: 's',
        28: 'f', 29: 'h', 30: 'k', 31: 'x',
        32: '2', 33: 'v', 34: 'n'
    }

nu = [22, 21, 33, 21, 22] #r3v3r


def fun3(c, your_dict): #fun3(password[8:13], my_dict)
    s1 = ''

    for i in nu:
        s1 += your_dict[i] #r3v3r

    if s1 == c:
        return True
    return False

if __name__ == '__main__':
	print(fun3('r3v3r',my_dict))