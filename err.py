import os, glob, xlrd, datetime, time
import ctypes
import Tkinter
import tkMessageBox
import logging

pjoin = os.path.join
files = glob.glob(pjoin(dir, pattern))
print files