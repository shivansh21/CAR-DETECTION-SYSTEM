#SOURCE CODE

import smtplib
import io
import time
import os
import image
from google.cloud import vision
from google.cloud.vision import types
import exifread
import Tkinter as tk
import webbrowser
p = []
def detect_properties(path):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    maxx = -1
    for color in props.dominant_colors.colors:
        fraction = float(color.pixel_fraction)
        red = float(color.color.red)
        green = color.color.green
        blue = color.color.blue
        if (fraction>maxx):
           maxx = fraction
           del p[:]
           p.append(fraction)
           p.append(red)
           p.append(green)
           p.append(blue)

        time.sleep(1)
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
vision_client = vision.Client()

file_names = 'number-plates-ireland.jpg.2'

with io.open(file_names,'rb') as image_file:
   content = image_file.read()
   image = vision_client.image(content=content)

labels = image.detect_labels()
web  = image.detect_web()

c=0
print("\n\n----------------------------------------------- CAR LABELS -----------------------------------------------------\n\n")
for label in labels:
   c = c+1
   z = c
   z = str(z)
   time.sleep(0.8)
   print("            LABEL "+ z + ": "+ str((label.description).title()) + "              MATCH: " + str((label.score)*100)+"% ...\n")

print("\n\n---------------------------------------------- WEB ENTITIES -----------------------------------------------------\n\n")

d=0
for entity in web.web_entities:
   d = d+1
   e = d
   e = str(e)
   time.sleep(0.8)
   print ("            ENTITY "+ e + ": "+ str((entity.description).title()) + "           MATCH: " + str((entity.score)*100)+"% ...\n")

print("\n\n--------------------------------------------- CAR'S NUMBER PLATE --------------------------------------------------\n\n")
for text in image.detect_text():
   time.sleep(1)
   print("\n            STRING FOUND: "+ str(text.description) + "                                       MATCH: " + str((text.score)*100) +"% ...\n")

print("\n\n--------------------------------------------- COLOR PROPERTIES -----------------------------------------------------\n\n")
detect_properties(file_names)

text_file = open("Data.txt","w")
text_file.write("\n--------------------------------------------------------- COMPUTER VISION: CAR DETECTION SYSTEM ----------------------------------------------------$
text_file.write("\n\n* DOCUMENTATION:")
text_file.write("\n\nCAR DETECTION SYSTEM IS AN APPLICATION BASED ON COMPUTER VISION WHICH HAS THE POWER OF RECOGNISING THE IMAGE LABELS, WEB-ENTITIES AND VARIOUS\n")
text_file.write("OTHER PROPERTIES ALSO WHICH INCLUDES IN IT. WE HAVE USED GOOGLE VISION API'S AND SOME OTHER FRAMEWORKS TO MAKE ITSELF TRAINED FOR ANY EVALUATION DATA\$
text_file.write("\n\n------ HOW WE PERFORMED.. -------\n\n")
text_file.write("WE HAVE USED GOOGLE CLOUD PLATFORM AND IN IT WE INSTALLED  UBUNTU 16.04 OS AND ENABELLED GOOGLE VISION API. IT REQUIRES SERVER CONNECTION WHICH\n")
text_file.write("INTEGRATES PYTHON 2.X AND AFTER DOING SO WE HAVE INTALLED ALL THE REQUIRED PACKAGES IN THE DIRECTORY NAMED 'gcloudstuff'. \n")
text_file.write("\n\n------ HOW IT WORKS ---------\n\n")
text_file.write("WE TAKE THE LINK OF CAR(FORMAT IS NOT AN ISSUE) AND PROCESS IT WITH OUR ALGORITHM, AFTER PROPER ANALYSING, IT IS ABLE TO SHOW CAR MAKE, MODEL NAME\n")
text_file.write("COLOR CODE, NUMBER PLATE, AND MANY MORE ATTRIBUTES.")

text_file.write("\n\n\n------ LABELS ---------\n\n")
for label in labels :
   text_file.write("\nLABEL: {}".format(label.description))
   text_file.write(", MATCH: {}".format(label.score))

text_file.write("\n\n------- WEB - ENTITIES --------\n\n")
for entity in web.web_entities :
   text_file.write("\nENTITY: {}".format(entity.description))
   text_file.write(", MATCH: {}".format(entity.score))

text_file.write("\n\n------- NUMBER PLATE --------\n\n")
for text in image.detect_text():
   text_file.write("\nReg Number:%s "%(text.description))
   break

text_file.write("\n\n------- COLOR PROPERTY --------\n\n")
text_file.write("\nfraction: %f"%(p[0]))
text_file.write("\nRed: %f"%(p[1]))
text_file.write("\nGreen: %f"%(p[2]))
text_file.write("\nBlue: %f"%(p[3]))

text_file.close()
