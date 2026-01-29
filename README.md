Overview:

This project is a simple image slideshow built with Python, Tkinter, and Pillow(PIL). It automatically cycles through all images in a folder and displays them in a GUI window.

The project uses itertools.cycle to loop infinitely through images and root.after() to change images at regular intervals.



Features:
- Automatic image slideshow
- Supports multiple image formats: .png, .jpg, .jpeg, .gif
- Resizes images to fit the window
- Infinite looping using itertools.cycle



Requirements:

- Python 3.x
- Libraries:
Tkinter (comes built-in with Python)
Pillow (install with pip install pillow)