#! /usr/bin/env python
#
# Support module generated by PAGE version 4.7
# In conjunction with Tcl version 8.6
#    Mar 15, 2016 11:08:51 AM


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    print 'destroying windows'
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import balanza_conector
    balanza_conector.vp_start_gui()


