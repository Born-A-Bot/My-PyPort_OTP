#import library 
import qrcode
import requests

#create variable and source - url
url = 'https://github.com/Born-A-Bot/My-PyPort-QRCode' 

#create image
img = qrcode.make(url)

#save the image and assign a name to the file
img.save("C://Users/seren/Documents/scrooples/pyport/qr_code/git_py.png")

#generate message when task complete, qrcode generated and saved
print('image saved')

#cybersecurity - set redirect parameter to prevent user connection from being hijacked, redirected
response = requests.get(url, allow_redirects=False)

#display status of connection, response
print(f"Status Code: {response.status_code}")

#notification, no redirect
if "Location" in response.headers:
    print(f"Redirect Location: {response.headers['Location']}")
else:
    print("No redirect decteced.")



