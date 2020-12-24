# Usage:

>>>>`python3 StartSendSms.py`



FreekySmS Iran Used
 The server sent in this program is on a specific server that works only with Iranian numbers in Iran

 ### To use, you must replace the link you get from the site with the following link in the program code

    urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

### And we have to move the command sent to the link, which we again received from the desired site, with the following data

     mydata = {"cellphone": "+98" + phoneNumber}
 


# Requirements:

1. Python 3
2. Pip
3. TQDM Python module (`pip3 install tqdm`)

 #### If for any reason you can not use pip, you can use the following command Linux (Ubuntu)
 
        sudo apt-get install python3-tqdm
        

        



# Downsides

Messages are all sent from 1 number. So by blocking this 1 number you block all spam.

# Example Usage:

![](/pic/test.jpg)


# Farsi Help

## برای استفاده باید لایبری های زیر وپایتون رو نصب کنید 

1. Python 3
2. Pip
3. TQDM Python module (`pip3 install tqdm`)



 سرور ارسالی در این برنامه بر روی سرور مشخصی که فقط در ایران با شماره های ایران کار میکنه 

برای استفاذه شما باید لینکی که از سایت مورد نظر به دست میارید رو با لینک زیر در کد برنامه جایگزین کنید

## در اینجا ما یرور های اسنپ رو استفاده کردیم 

    urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

## و باید دستور ارسالی به لینک رو که باز هم از سایت مورد نظر به دست اوردیم با داده زیر جابه جا کنیم 

     mydata = {"cellphone": "+98" + phoneNumber}
     
     
     
## اگه به هر دلیلی از pip  نمیتونید استفاده کنید از دستور زیر تر لینوکس (اوبنتو) میتونید استفاده کنید

          sudo apt-get install python3-tqdm

