def sum_of_odd_nums(n):
    odds=[]
    for i in range(1, n+1):
        odds.append(i*2+1)
    b=0
    for j in odds:
        b+=j
    return b

def caesar_cipher(message, key):
    msg = []
    for c in message:
        msg.append(ord(c)+key)
    msg2 = []
    for b in msg:
        msg2.append(chr(b))
        
    return msg2

def fizzbuzz(n):
    pass 

def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(10):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "bazinga"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()
