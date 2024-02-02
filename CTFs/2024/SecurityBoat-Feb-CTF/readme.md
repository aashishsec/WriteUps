# SecurityBoat CTF WriteUp - Feb 2024

Link for CTF: [http://ctf.securityboat.net/](http://ctf.securityboat.net/)

## Recon:

1. Let's check what the website does and decide the Attack surface of this website.
2. It is a shopping website `BrittleBasketStore` that contains the following options:
    - Home
    - Rules
    - Tickets
    - Vouchers
    - Merchandise
    - Stickers
    - Stationery
    - Goodies
    - Login

3. Finding the tech stack using Wappalyzer.
4. Register into the website and check the inner functionality.
5. After registration, log in and proxy all HTTP traffic to Burp.
6. Explore profile features, including user details and order information.
7. Check the profile feature, containing name, email, contact, and address to update.
8. Make an Attack surface of this website.
9. Conduct directory brute-forcing to find sensitive files, discover admin, and locate asset files.

### Directories Found:
- Assets Directory
- Admin Directory

10. Attempt to access those pages.
11. Gain admin access but not the flag.
12. Encountered an error during some actions, indicating it might not be true admin access.
13. In the edit product page, found a file upload feature.
14. No success, only error.

## Attack Surface:

- Try the following attacks on this website:
  - IDOR
  - CSRF
  - XSS in profile functionality
  - Rate Limit
  - SQLi on login

## Exploitation:

### SQLi:

- Intruder attack on the login page with SQLi payloads.
- No success.

### IDOR's:

#### 1st IDOR:

- Didn't close the browser after accessing the admin panel.
- Change the user details and got the flag.

**Request:**
```http
POST /server/user.php HTTP/1.1
Host: ctf.securityboat.net
Content-Length: 90
...
token=&username=&name=zcd&email=zccvzc&contact=zczxcxc&address=zczc+z&operation=updateUser
```

- Intercepted request, found no token while updating user profile, got the flag.

#### 2nd IDOR:

- Created another user to check IDOR.
- Tried changing the userID to 159, got an error.
- Removed the token and changed the userID to 159, got the flag again.

**Response:**
```http
<script>alert('User updated by another account!! Your Flag {!DOR_!S_FUN}');location.href='../';</script>
```

4. Further exploited to check the application response, removed both userID and token, got another SQL error.

Flag is: `{!DOR_!S_FUN}`

5. Concluded the writeup.

I hope you enjoyed my writeup!
