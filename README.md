# My-PyPort_OTP
Developer sample project: One-Time-Password

```
version 1.0.1

import string 
import random

def generate_otp():

    #generate alphabet dynamically
    alphaChar = string.ascii_lowercase
    puncList = string.punctuation
    numList = string.digits

    #shuffle the lists to return a different value
    shuffledAlpha = random.sample(alphaChar, len(alphaChar))
    shuffledNums = random.sample(numList, len(numList))
    shuffledPunc = random.sample(puncList, len(puncList))

    #retrieve seven letters and three number
    otp = shuffledAlpha[0:3] + shuffledNums[0:2]  + shuffledPunc[0:2]  
    otp_shuffle = random.sample(otp, len(otp))
    
    print(f"You're one time password is: {otp_shuffle}")
    
    #if __name__ == "__main__":

    #create an instance of the function
generate_otp()

```


```
version 1.0.0

#import library for qrcode
import qrcode

#create variable and source - url
img = qrcode.make('https://github.com/Born-A-Bot/My-PyPort-QRCode')

#save the image and assign a name to the file
img.save("git_py.png")

#generate message when task complete, qrcode generated and saved
print('image saved')

```
