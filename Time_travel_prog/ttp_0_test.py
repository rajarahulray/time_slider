# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from tkinter import Tk, PhotoImage, ttk, Canvas
from pyautogui import size
import os
from PIL import Image

def pr(v):
    print(v, type(v)) ;
    i = int(float((v)));
    print(im_names[i]);
    im = Image.open(r"D:/time_travel_prog_images/{}".format(im_names[i]));
    im.resize((100,200), Image.ANTIALIAS);
    img = PhotoImage(im);
    
    #print('image', img);
    can.delete("all")
    can.create_image(10, 10, image = img, anchor = 'nw');
    can.image = im;
   



im_names = os.listdir("D:/time_travel_prog_images");
x, y = size();
    
r = Tk();
im = PhotoImage(file = r"D:/time_travel_prog_images/scene00001.png");

can = Canvas();
can.pack(side = 'top', fill = 'both', expand = 'yes')
can.create_image(10, 10, image = im, anchor = 'nw');

s = ttk.Scale(r, orient = 'horizontal', length = x, from_ = 0, to = len(os.listdir("D:/time_travel_prog_images")) - 1, command = pr).pack();#working without passing any value from command....interesting..

r.mainloop();


