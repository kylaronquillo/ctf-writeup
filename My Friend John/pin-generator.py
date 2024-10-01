from itertools import product

# Generate PINs with lengths 4 to 6
with open('pin_wordlist.txt', 'w') as f:
    for length in range(4, 7):
        for pin in product('0123456789', repeat=length):
            f.write(''.join(pin) + '\n')
