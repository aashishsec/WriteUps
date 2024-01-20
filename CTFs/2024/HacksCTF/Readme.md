# HacksCTF My Approach Notes

## Cryptography

## MISC

### magik-magik 

there are some changes that we need to do

- there is a file file_challeange.cad.
- I did file command to see what it was. It was tar compressed file.
- I extracted it
- Got a file flag.iso
- I tried to decrypt the contents of it and Got the Flag.
```bash

 [/mnt/c/Users/aashi/Downloads/HackCTF/Completed]
 ✘  jaisriram  file file_challenge.cad
file_challenge.cad: XZ compressed data, checksum CRC64

 [/mnt/c/Users/aashi/Downloads/HackCTF/Completed]
 jaisriram  tar -xJvf file_challenge.cad
./
./file_challenge/
./file_challenge/flag.iso

 [/mnt/c/Users/aashi/Downloads/HackCTF/Completed]
 jaisriram  cd file_challenge 

 [/mnt/c/Users/aashi/Downloads/HackCTF/Completed/file_challenge]
 jaisriram  cat flag.iso 
<+ohcAo(mg+DGm>3Zr*E@r$.49f$lVA3k;a?Ys4h+`MQP@8pqjDLD%            
```
- the flag was encrypted using ASCII85. I used dcode.fr to decrypt it.
  ```bash
  The flag is : hacks{M3t@dAt&_man!pu(aTi*n}
  ```
## OSINT

## Forensics

## Reverse

## Pwn

### jarrrrrr
An ancient fortress of binary secrets stands before you, guarded by a formidable registration system. To breach its defenses, you must find a way to bypass its seemingly impenetrable code validation. But beware, for even the most secure systems have their weaknesses . Always Go With The Flow. Caution: Respect The Sanctum.

- I used jadx to open the jar file.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/2856a520-43ed-4379-a360-c7b7300d49cb)
```bash
hacks{1nt3g3rs_G0ne_Wr0ng}
```

### quickmath
Really fast maths
connect using netcat on the below server
0.cloud.chals.io:33312

- This challange is all about how fast we are at solving the math.
- So i used this python program to connect and solve the challange.
```python
  import re
import socket

def extract_and_solve(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return expression

# Connect to the server using nc
host = "0.cloud.chals.io"
port = 33312

with socket.create_connection((host, port)) as s:
    while True:
        # Receive data from the server
        data = s.recv(1024).decode()

        if not data:
            # Connection terminated
            break

        # Print the input received from the server
        print("Received from server:", data)

        # Extract values, solve, and send back the result
        match = re.search(r"Solve:\s*([\d\s+\-*/]+)", data)
        if match:
            result = extract_and_solve(match.group(1))
            print("Result after 'Solve:':", result)
            s.send(result.encode())
        else:
            print("No 'Solve:' pattern found in the received message.")

  ```
  output:
  
 ```bash
Received from server: Solve: 54 * 4

Result after 'Solve:': 216
Received from server: Correct!

Traceback (most recent call last):
  File "c:\Users\aashi\Downloads\quickmath.py", line 28, in <module>
    result = extract_and_solve(re.search(r"Solve:\s*([\d\s+\-*/]+)", data).group(1))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'group'
PS C:\Users\aashi\Downloads> & C:/Users/aashi/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/aashi/Downloads/quickmath.py
Received from server: Solve: 5829 / 67

Result after 'Solve:': 87.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 70 * 21

Result after 'Solve:': 1470
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 76 + 54

Result after 'Solve:': 130
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 5940 / 60

Result after 'Solve:': 99.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 74 * 84

Result after 'Solve:': 6216
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 1358 / 14

Result after 'Solve:': 97.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 42 + 77

Result after 'Solve:': 119
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 32 + 86

Result after 'Solve:': 118
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 2784 / 32

Result after 'Solve:': 87.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 21 - 42

Result after 'Solve:': -21
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 7980 / 95

Result after 'Solve:': 84.0
Received from server: Correct!
Solve: 74 - 40

Result after 'Solve:': 34
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 37 + 43

Result after 'Solve:': 80
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 95 * 99

Result after 'Solve:': 9405
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 768 / 8

Result after 'Solve:': 96.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 56 * 86

Result after 'Solve:': 4816
Received from server: Correct!
Solve: 99 - 95

Result after 'Solve:': 4
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 594 / 6

Result after 'Solve:': 99.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 1 + 84

Result after 'Solve:': 85
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 81 * 28

Result after 'Solve:': 2268
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 75 - 78

Result after 'Solve:': -3
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 66 * 73

Result after 'Solve:': 4818
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 90 * 42

Result after 'Solve:': 3780
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 7 * 33

Result after 'Solve:': 231
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 88 * 37

Result after 'Solve:': 3256
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 47 + 10

Result after 'Solve:': 57
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 760 / 40

Result after 'Solve:': 19.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 91 - 97

Result after 'Solve:': -6
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 35 - 43

Result after 'Solve:': -8
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 2928 / 48

Result after 'Solve:': 61.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 74 - 58

Result after 'Solve:': 16
Received from server: Correct!
Solve: 59 + 22

Result after 'Solve:': 81
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 3744 / 48

Result after 'Solve:': 78.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 504 / 14

Result after 'Solve:': 36.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 46 + 68

Result after 'Solve:': 114
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 43 * 77

Result after 'Solve:': 3311
Received from server: Correct!
Solve: 27 + 41

Result after 'Solve:': 68
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 726 / 11

Result after 'Solve:': 66.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 84 + 64

Result after 'Solve:': 148
Received from server: Correct!
Solve: 14 + 25

Result after 'Solve:': 39
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 26 - 46

Result after 'Solve:': -20
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 2 - 67

Result after 'Solve:': -65
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 6256 / 68

Result after 'Solve:': 92.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 22 + 45

Result after 'Solve:': 67
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 70 * 32

Result after 'Solve:': 2240
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 66 * 52

Result after 'Solve:': 3432
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 2170 / 35

Result after 'Solve:': 62.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 75 - 58

Result after 'Solve:': 17
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 2925 / 65

Result after 'Solve:': 45.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 45 * 31

Result after 'Solve:': 1395
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 1218 / 87

Result after 'Solve:': 14.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 18 + 14

Result after 'Solve:': 32
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 33 + 75

Result after 'Solve:': 108
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 138 / 3

Result after 'Solve:': 46.0
Received from server: Correct!
Solve: 59 + 32

Result after 'Solve:': 91
Received from server: Correct!
Solve: 672 / 28

Result after 'Solve:': 24.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 51 + 60

Result after 'Solve:': 111
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 6696 / 93

Result after 'Solve:': 72.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 52 + 47

Result after 'Solve:': 99
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 36 + 100

Result after 'Solve:': 136
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 99 + 97

Result after 'Solve:': 196
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 52 * 9

Result after 'Solve:': 468
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 67 + 17

Result after 'Solve:': 84
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 55 - 96

Result after 'Solve:': -41
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 55 * 46

Result after 'Solve:': 2530
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 71 + 74

Result after 'Solve:': 145
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 69 + 48

Result after 'Solve:': 117
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 1872 / 52

Result after 'Solve:': 36.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 10 - 40

Result after 'Solve:': -30
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 64 - 4

Result after 'Solve:': 60
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 1540 / 20

Result after 'Solve:': 77.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 8811 / 99

Result after 'Solve:': 89.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 98 - 12

Result after 'Solve:': 86
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 71 + 80

Result after 'Solve:': 151
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 760 / 95

Result after 'Solve:': 8.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 87 * 87

Result after 'Solve:': 7569
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 75 + 22

Result after 'Solve:': 97
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 69 + 75

Result after 'Solve:': 144
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 40 - 93

Result after 'Solve:': -53
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 12 - 96

Result after 'Solve:': -84
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 377 / 13

Result after 'Solve:': 29.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 62 + 79

Result after 'Solve:': 141
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 95 + 32

Result after 'Solve:': 127
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 11 - 85

Result after 'Solve:': -74
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 98 * 54

Result after 'Solve:': 5292
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 6555 / 69

Result after 'Solve:': 95.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 44 - 9

Result after 'Solve:': 35
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 5525 / 85

Result after 'Solve:': 65.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 93 * 35

Result after 'Solve:': 3255
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 52 + 35

Result after 'Solve:': 87
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 7238 / 94

Result after 'Solve:': 77.0
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 72 * 21

Result after 'Solve:': 1512
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 7371 / 81

Result after 'Solve:': 91.0
Received from server: Correct!
Solve: 7 + 68

Result after 'Solve:': 75
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 12 * 32

Result after 'Solve:': 384
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 43 * 89

Result after 'Solve:': 3827
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 40 * 18

Result after 'Solve:': 720
Received from server: Correct!
Solve: 64 + 40

Result after 'Solve:': 104
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 11 - 79

Result after 'Solve:': -68
Received from server: Correct!

No 'Solve:' pattern found in the received message.
Received from server: Solve: 53 - 44

Result after 'Solve:': 9
Received from server: !!! FLAG GET: hacksctf{m1nus_0ne_tha7s_free} !!!
Great job! You're well on your way to becoming a Math champion.

No 'Solve:' pattern found in the received message.
  ```

