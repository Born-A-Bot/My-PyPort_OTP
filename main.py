import string 
import random

def generate_otp():

    #generate alphabet dynamically
    alphaChar = string.ascii_lowercase
    numList = ['0', '1', '2', '3','4','5','6','7','8','9']

    #shuffle the lists to return a different value
    shuffledAlpha = random.sample(alphaChar, len(alphaChar))
    shuffledNums = random.sample(numList, len(numList))

    #retrieve seven letters and three number
    otp = shuffledAlpha[0:3] + shuffledNums[0:2]    
    otp_shuffle = random.sample(otp, len(otp))
    
    print(f"You're one time password is: {otp_shuffle}")
    
    #if __name__ == "__main__":

    #create an instance of the function
generate_otp()











