#!/usr/bin/env python3
import queue 
import speech_recognition as sr
import time
import sys
import board
import neopixel
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont

# recognize speech using Google Cloud Speech
#Put your key here. It starts like this
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
{
  "type": "service_account",
}
"""

text = queue.Queue()

def callback(recognizer, audio):                            
# this is called from the background thread
    try:
        youSaid = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        print("Google: " + youSaid)
        text.put(youSaid)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

def getIndex(x, y):
    x = display_width-x-1
    return (x*8)+y

pixel_pin = board.D18
num_pixels = 256
display_width = 32
display_height = 8
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

font = ImageFont.truetype("5x7.ttf", 8)

def scrollText(text):    
# Measure the size of the text
    text_width, text_height = font.getsize(text)


# Create a new PIL image big enough to fit the text
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
    image.save("img.png", "PNG")

# Draw the text into the image
    draw.text((display_width, -1), text, font=font, fill=255)
    image.save("img2", "PNG")

    offset_x = 0
    
    while True:
	    #scroll the image across the mask
        for x in range(display_width):
            for y in range(display_height):
			
			    #rainbow! 
                hue = (time.time() / 10.0) + (x / float(display_width * 2))
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

                pixel = image.getpixel((x + offset_x, y))
    
                if image.getpixel((x + offset_x, y)) == 255:
                    pixels[getIndex(x,y)] = (r, g, b)
                else:
                    pixels[getIndex(x,y)] = (0, 0, 0)
        
        offset_x += 1
		#if we've reached the end of the mask, break the while loop
        if offset_x + display_width > image.size[0]:
            offset_x = 0
            break
    
        pixels.show()
        time.sleep(0.03)
    
pixels.fill((0,0,0))
pixels.show()

#setup the speech recogniser, and listen in the background
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)
while True: 
    scrollText(text.get()) 