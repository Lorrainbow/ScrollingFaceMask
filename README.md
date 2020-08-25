# ScrollingFaceMask

This code compliments the Element14 Presents video (link to be added)

The project is split into two

## Raspberry Pi + Google Speech-to-Text API
- takes audio in from a USB microphone attached to a raspberry pi
- transcribes the audio using Google Speech-To-Text service
- scrolls the transcribed text across an RGB LED matrix attached to the raspberry pi

In each file, check out the function getIndex and getIndex2. The main code calls getIndex but which one you use depends on the layout of your grid

**TestFont** scrolls text across the grid

**microphoneTest** uses the free GoogleAPI to test the microphone. Prints what it thinks you said to the screen

**microphoneTestWithLights** uses the free GoogleAPI to test the microphone. Prints what it thinks you said to the screen and scrolls across the facemask. 

**GoogleCloudWorkingFromMic** uses the paid for GoogleAPI. You will need a key to get this working. Setup your own key using the Google Cloud platform.


## Wemos LOLIN32 + Dragon Naturally Speaking
- takes audio in from a microphone attached to your PC
- the PC uses Dragon Naturally Speaking software to transcribe your speech to text
- the PC sends this text via Bluetooth to a Wemos LOLIN32 using a program called Putty
- the Wemos LOLIN32 scrolls the text across the RGB LED matrix inside your facemask 

**sketch_aug19a** is the main file

> speeds up the scrolling
< slows the scrolling down
\] increases the brightness
\[ decreases the brightness
