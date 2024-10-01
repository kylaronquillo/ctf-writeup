# My Friend John
This is a cryptography challenge wherein you have to crack the passwords of the zip files using tools. In this one, I used John the Ripper.

### Step 1
Crack the password for **use-rockyou.zip**
```
cd C:\JOHN\run
zip2john "..\MyFriendJohn\use-rockyou.zip" > hash.txt
john hash.txt --wordlist="..\rockyou.txt"
john --show hash.txt
```
### Step 2
Crack the password for **custom-list.zip**
```
cd C:\JOHN\run
zip2john "..\custom-list.zip" > hash.txt
john hash1.txt --wordlist="..\custom-list.txt"
john --show hash.txt
```
### Step 3
Crack the password for **brute-force-pin.zip**

I coded a python file that generates all possible 4 to 6 digit PINs using the digits 0-9. It writes each PIN to a file called pin_wordlist.txt.
```
from itertools import product

# Generate PINs with lengths 4 to 6
with open('pin_wordlist.txt', 'w') as f:
    for length in range(4, 7):
        for pin in product('0123456789', repeat=length):
            f.write(''.join(pin) + '\n')
```
Then proceed to use the pin_wordlist.txt to crack the password of the zip file.
```
cd C:\JOHN\run
zip2john "..\brute-force-pin.zip" > hash2.txt
john hash2.txt --wordlist="..\pin_wordlist.txt"
john --show hash.txt
```
### Step 4
Open the **flag.txt** and copy the flag. 
