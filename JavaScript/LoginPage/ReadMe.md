# Heaven Login Page 2.0
---
## Objective
Modify an HTML/CSS login page I made to meet the following requirements using Javascript and jQuery:

1. Submit the username and password for verification.
2. If the username submitted is a@bc.com and password is hello, then show a message saying "Login Successful." otherwise, flash a message showing "Incorrect Username/Password".
3. If the username is not an email prevent the user from pressing login.

## Steps Taken

1. Made a copy of my HTML/CSS [login page] folder.
2. Added a submit function that alerts messages given the conditions in 2 above.
3. Added email validation functions that disable the login button if the email is not valid.
4. An email validation function also manually changes and disables some of the CSS styling of the button so that it looks inactive.

## Results

* The page works as expected.
* I learned there are different formats for validating emails.
* I also learned that it is not straightforward to disable CSS functionality such as hover. This had to be done indirectly by adding and removing html classes.
* All files can be downloaded in loginPage.zip. The html file is loginStyled.html.

[login page]: https://github.com/rebeccapizano/Portfolio/tree/master/HTML-CSS/LoginPage
