# PW Crack 2
**Challenge Source:** [pico-ctf](https://play.picoctf.org/practice/challenge/246?page=1&tag=6)
### Step 1
I first run the file in vscode but it indicated that it couldn’t find the file anywhere. Since there are no other factors to consider, and upon looking at the code, I came to a conclusion that VSCode is preventing the python script from accessing the enc file.
Enc Tool info: https://pypi.org/project/enc-tool/ 
### Step 2
I searched the net of other ways to run python script and learned that u can run python script in terminal by opening the file using nano.(same as the PW Crack 1 problem)
### Step 3
After opening it using nano and then saving it, I run the script file and it asked me for a password. This time, the password was not given straightforwardly. 
```
user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
```
### Step 4
The 0x format reminded me of ASCII hence I searched for a ascii converter table and converted the ascii code to symbol.
### Step 5
The symbols I gathered were the password for the script, hence, I got the flag.
