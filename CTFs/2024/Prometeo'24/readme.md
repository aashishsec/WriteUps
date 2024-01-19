# Prometeo'24
---
## General
0. Welcome Flag
   
- Solution

```bash

Welcome to the event, here take this CTF{w3lc0me_t0_th3_e4ent}

```

### Kittey
   
![catdog](https://github.com/aashishsec/WriteUps/assets/65489287/44abafdf-4fe5-4c37-a25b-98e445922c32)

- solution
```bash
strings catdog.jpeg | grep "CTF"

CTF{cut3_pupp13_@nd_k1tt3n}
```
## Web
## Crypto
## Reverse 
### C for yourself
```bash
#include <stdio.h>
#include <string.h>

int main(void){
    char buff[64];
    int pass = 0;
    printf("\n Enter the password : \n");
    gets(buff);

    if (strcmp(buff, "yesitishereforyou")){
        printf("\n Wrong Password \n");
    }
    else{
        printf("\n Correct Password \n");
        pass = 1;
    }
    if (pass){
        /* Overflowed*/
        printf(" \n CTF{i_t0ld_u_it_w@s_her3}");
    }
}

```
A source code file contain flag

```bash
CTF{i_t0ld_u_it_w@s_her3}
```

### pyRev

- Give two file one python code use to encrypt the flag and other is encrypted flag
  Encrypted Py Program
 ```bash
  def process_flag(flag):
    ns = ''
    for i in flag:
        if ord(i) < 99:
            n = "0" + str(ord(i))
        else:
            n = str(ord(i))
        if int(n[0] + n[-1:0:-1]) > 0:
            n = n[0] + n[-1:0:-1]
        ns += chr(int(n))
    return ns

def save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)

def main():
    flag = ''
    processed_data = process_flag(flag)
    save_to_file(processed_data, "log.txt")

if __name__ == "__main__":
    main()

  ```
  Decrypt Py Program
  ```bash
  def reverse_process(data):
    original_flag = ''
    for i in data:
        n = str(ord(i))
        if len(n) == 2:
            n = "0" + n
        original_flag += chr(int(n[0] + n[-1:0:-1]))
    return original_flag

def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def main():
    filename = "log.txt"
    processed_data = read_from_file(filename)
    original_flag = reverse_process(processed_data)
    print("Original Flag:", original_flag)

if __name__ == "__main__":
    main()

  ```
  solution
  ```bash
  Original Flag: ctf{13@rning_h3ll0_w0r1d}
  ```
