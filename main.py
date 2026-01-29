#import everything for GUI creation
from tkinter import *

#PIL -> image processing
#Image -> to open images
#ImageTk -> converts images to a format so that Tkinter can display
from PIL import Image, ImageTk

#helps in listing all images from a folder
import os

#to loop through images infinitely
import itertools


#-------MAIN WINDOW-------

#creates the main window
screen = Tk()

#title
screen.title('IMAGE SLIDESHOW')

#size
screen.geometry('1000x1000')

#path of images folder
folder = 'images'

#empty list to store all loaded images
list = []


#this is a for loop that goes through every item in the folder one by one
for image in os.listdir(folder):

    #only include image files
    #outer parentheses -> for the function call
    #inner parentheses -> create a tuple of multiple suffixes
    if image.endswith(('.jpg', '.png', '.gif', 'jpeg')):

        #to get the full path of the image
        image_location = os.path.join(folder, image)

        #open the image using pillow
        img_ = Image.open(image_location)

        #size of the window
        img_ = img_.resize((1000,1000))

        #converts the pillow image into tkinter suitable image
        list.append(ImageTk.PhotoImage(img_))


#creating an infinite image cycle
images = itertools.cycle(list)

#creates a tkinter label widget to display images
label = Label(screen)

#place the label in window
label.pack()

#defines a function to show the next image
def upcoming_image():

    #gets the next image
    img_ = next(images)

    #updates the label to show the new image
    label.config(image = img_)

    #will show next image after 3000milliseconds
    screen.after(3000, upcoming_image)


#starts the slideshow
upcoming_image()

#starts the tkinter event loop
screen.mainloop()    



