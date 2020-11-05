def sum_of_odd_nums(n):
    b=sum([1+i*2 for i in range(n)])
    return b

def caesar_cipher(message, key):
    msg = [chr(ord(c)+key) for c in message]
        
    return ''.join(msg)
def fizzbuff(num):
    if num % 3 == 0 and not num % 5 == 0:
        return "fizz"
    if num %  5 == 0 and not num % 3 ==0:
        return "buzz"
    if num % 5==0 and num % 3 == 0:
        return "fizzbuzz"
    if not num % 5 == 0 and not num % 3 == 0:
        return num
def fizzbuzz(n):
    fb = [fizzbuff(i) for i in range(n)]
    return fb
def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(10):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "_^wfkd^"
    print(caesar_cipher(ciphertext, 3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()
