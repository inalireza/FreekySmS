# Usage:

>>>>`python3 StartSendSms.py`



FreekySmS Iran Used
 The server sent in this program is on a specific server that works only with Iranian numbers in Iran

 To use, you must replace the link you get from the site with the following link in the program code

   urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

 And we have to move the command sent to the link, which we again received from the desired site, with the following data

     mydata = {"cellphone": "+98" + phoneNumber}
 


# Requirements:

1. Python 3
2. Pip
3. TQDM Python module (`pip3 install tqdm`)




# Downsides

Messages are all sent from 1 number. So by blocking this 1 number you block all spam.

# Example Usage:

![](/pic/test.jpg)





