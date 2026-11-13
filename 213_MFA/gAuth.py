# Adapted from this code by dwaipayan_bandyopadhyay :
# https://www.geeksforgeeks.org/python/two-factor-authentication-using-google-authenticator-in-python/

import pyotp
import qrcode
import hashlib
import base64

key = "TotallyNewRandomPasswordNoOneCanGuessNumber51"

#Hash any length secret key to exactly 20-bytes (standard for TOTP)
digest = hashlib.sha1(key.strip().encode("utf-8")).digest()
# Encode as 32-character (Base32) string using only A-Z and 2-7
key = base64.b32encode(digest).decode("utf-8")

uri = pyotp.totp.TOTP(key).provisioning_uri(name='CSP',issuer_name='MrPoling')
print(uri)

makeQR = input("\nCreate a new QR code?  y/n \n(Do just once per uri) ")
if (makeQR == "y"):
    qrcode.make(uri).save("qr.png") # Qr code generation step
    
print("\n Please use the QR code image file qr.png to add this acccount to Google Authenticator \n(Install the app first if you haven't)\n")

"""Verifying stage starts"""
totp = pyotp.TOTP(key)

#TODO: Create an infinite loop which:
#      1) asks the user to enter the code (from the Google Authenticator app)
#         You should either tell the user not to include spaces, OR remove them before the verification step

#      2) verifies that entered value is true or false, and prints out the result
#         To verify, use this method:  totp.verify(user_entered_code) 
#         (where user_entered_code is the user's input)
