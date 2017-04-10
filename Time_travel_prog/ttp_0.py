# -*- coding: utf-8 -*-

from tkinter import Tk, PhotoImage, ttk, Canvas
from pyautogui import size
import os

def pr(v):
    print(v, type(v)) ;
    i = int(float((v)));
    print(im_names[i]);
    im = PhotoImage(file = r"<location of image files>"/{}".format(im_names[i]));
                
    print('image', im);
    can.delete("all")
    can.create_image(10, 10, image = im, anchor = 'nw');
    can.image = im;
   



im_names = os.listdir("<location of image files>");
x, y = size();
    
r = Tk();
im = PhotoImage(file = r"<location of image files>/<any pic from location>");

can = Canvas();
can.pack(side = 'top', fill = 'both', expand = 'yes')
can.create_image(10, 10, image = im, anchor = 'nw');

s = ttk.Scale(r, orient = 'horizontal', length = x, from_ = 0, to = len(os.listdir("<location of image files>")) - 1, command = pr).pack();#working without passing any value from command....interesting..

r.mainloop();
