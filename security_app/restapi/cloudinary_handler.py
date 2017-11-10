import cloudinary
import cloudinary.uploader
import cloudinary.api
import base64
import os

from restapi.config import *

cloudinary.config( 
  cloud_name = CLOUDINARY_NAME, 
  api_key = CLOUDINARY_API_KEY, 
  api_secret = CLOUDINARY_API_SECRET 
)


#functions here
def UploadImage(base64decode, user, comName, comUser):
    fh = open(os.getcwd() + "/imageUpload.jpg", "wb")
    fh.write(base64.b64decode(base64decode.replace(' ','+'))) #need replace space with + because space disappears over the internet because of x-wwwform-urlencoded
    fh.close()
    fr = open(os.getcwd() + "/imageUpload.jpg", "rb")
    results = cloudinary.uploader.upload(os.getcwd() + "/imageUpload.jpg", folder = comName + "/" + comUser + "/", tags = user + "," + comName + "," + comUser)
    os.remove(os.getcwd() + "/imageUpload.jpg")
    return results;
