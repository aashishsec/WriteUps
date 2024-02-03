# SecurityBoat CTF WriteUp - Feb 2024

Link for CTF: [http://ctf.securityboat.net/](http://ctf.securityboat.net/)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/1f43ddbe-0f5e-48c4-8731-c3782b0a33fe)

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
   ![image](https://github.com/aashishsec/WriteUps/assets/65489287/b5f8527c-c481-4a44-a868-d2ad21aaefd9)
5. Register into the website and check the inner functionality.
6. After registration, log in and proxy all HTTP traffic to Burp.
7. Explore profile features, including user details and order information.
   ![image](https://github.com/aashishsec/WriteUps/assets/65489287/4d97230b-1c63-46be-bcc4-2ee5c26c07d0)
9. Check the profile feature, containing name, email, contact, and address to update.
    ![image](https://github.com/aashishsec/WriteUps/assets/65489287/9da8a8bb-9ac7-4805-afa3-abe56cfa0dfd)
11. Make an Attack surface of this website.
    ![image](https://github.com/aashishsec/WriteUps/assets/65489287/61ac9569-5efc-4d47-bcba-ef0d8a9e9356)
13. Conduct directory brute-forcing to find sensitive files, discover admin, and locate asset files.
### Directories Found:
- Assets Directory
![image](https://github.com/aashishsec/WriteUps/assets/65489287/dec53478-9d17-46d2-8b54-bd0669825a5b)
- Admin Directory
![image](https://github.com/aashishsec/WriteUps/assets/65489287/af0fb46a-4f8d-49f7-ba7e-ac9ef523857d)
10. Attempt to access those pages.
11. Gain admin access but not the flag.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/b43cc56a-3fe6-4fff-8632-3a70d51c8a7b)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/2a5f4b79-dc9f-4dfb-991f-0cecb11d27c1)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/14662ee7-53da-49be-ae41-ad1c4f7dd6a2)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/0f2f73f3-ae31-4d62-8044-63e146330507)
13. Encountered an error during some actions, indicating it might not be true admin access.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/08b8a0f1-27fa-490d-be5d-3ea9dbe4f0fa)
15. In the edit product page, found a file upload feature.
16. No success, only error.

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
![image](https://github.com/aashishsec/WriteUps/assets/65489287/efee67a6-234c-4837-aa63-29b33e9d2d49)

### IDOR's:

#### 1st IDOR:

- Didn't close the browser after accessing the admin panel.
- Change the user details and got the flag.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/7892a814-b8cb-42e5-b1f3-4f609d2e3070)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/993e3e7e-0423-44c2-baf5-1423b3c8c038)

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
![image](https://github.com/aashishsec/WriteUps/assets/65489287/3293066b-5e63-405a-8f36-27fef95f2db8)
![image](https://github.com/aashishsec/WriteUps/assets/65489287/8dd3df9f-2ce1-4012-a359-612573cd035f)


**Response:**
```http
<script>alert('User updated by another account!! Your Flag {!DOR_!S_FUN}');location.href='../';</script>
```

4. Further exploited to check the application response, removed both userID and token, got another SQL error.
![image](https://github.com/aashishsec/WriteUps/assets/65489287/1a1b8818-bded-43fe-87ac-5e6dec00983c)

Flag is: `{!DOR_!S_FUN}`

5. Concluded the writeup.

I hope you enjoyed my writeup!
