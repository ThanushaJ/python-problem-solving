'''from pycipher import Caesar


s = input("select shift   ")
print((Caesar(30).encipher('ABCD abcd abcd', keep_punct=True)))'''


Need = 'yes'
ret = ''
dec = ''

while Need == 'yes':
    S = input("input String:  ")
    key = int(input("Input Key:  "))
    op = int(input("Select operation:\n1.Encrypt\n2.Decrypt\n"))
    if op == 1:
        for x in S:
            ret += chr(ord(x) + 1)
        print(ret)
    if op == 2:
        for y in ret:
            dec += chr((ord(y) - key))
        print(dec)
    Need = input("Do you want to continue (yes/no):   ")
