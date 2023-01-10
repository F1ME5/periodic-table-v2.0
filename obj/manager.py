# Copyright 2023 Néstor Nahuatlato
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
This module creates the main window that contains the full periodic table.
It also puts text labels for title, periods, groups and other stuff.
'''

# Project modules
from obj.element import Element
from util.dimensions import groups_positions, periods_positions, X_BEGIN
from util.constants import C_1

# Python modules
from tkinter import Tk, Label
from tkinter.font import Font
from json import load

# Main window important values.
WIDTH  = 1350
HEIGHT = 980
TITLE  = "Periodic Table v2.0"

# JSON file where elements data is fixed.
DATA_PATH = "./data/fixed.json"

# Main window labels values.
TITLE_TEXT  = "PERIODIC TABLE"
TITLE_FONT_FAMILY  = "Lexend"
TITLE_FONT_SIZE    = 20
PERIOD_FONT_FAMILY = "Courier New"
PERIOD_FONT_SIZE   = 12
GROUP_FONT_FAMILY  = "Courier New"
GROUP_FONT_SIZE    = 12
AUX_FONT_FAMILY    = "Arial Black"
AUX_FONT_SIZE      = 15

# Some labels X and Y positions
LANTHANOID_MARK = "*"
ACTINOID_MARK   = "**"
TITLE_X  = 540
PERIOD_X = 25
GROUP_X_FIX = X_BEGIN - 15
GROUP_Y_FIX = 18 - X_BEGIN
LANTHANOID_X = 213
LANTHANOID_Y1 = 520 + X_BEGIN
LANTHANOID_Y2 = 742 + X_BEGIN
ACTINOID_X = 206
ACTINOID_Y1 = 616 + X_BEGIN
ACTINOID_Y2 = 838 + X_BEGIN

class Manager:
    def __init__(self): # Class constructor.
        self.mw = Tk() # Main window creation.
        self.set_mw() # Setting main window.
        self.set_periodic_table() # Setting periodic table.
        self.set_mw_labels() # Setting main window labels.

    def set_mw(self): # Main window setter.
        self.mw.geometry(f"{WIDTH}x{HEIGHT}") # Main window size in pixels: "width x height".
        self.mw.title(TITLE) # Main window title.
        self.mw.resizable(False, False) # Main window size change cancelation.

    def set_periodic_table(self): # Periodic table setter.
        #Getting elements data.
        with open (DATA_PATH) as file: # Opening JSON file.
            elements = load(file) # Loading fixed data from JSON file.
            file.close() # Closing JSON file.

        #Creating and configuring periodic table.
        for element in elements: # Iterating JSON data.
            e = Element(self.mw, element) # Object creation.

    def set_mw_labels(self): # Main window labels setter.
        # Local variables.
        title_font = Font(family=TITLE_FONT_FAMILY, size=TITLE_FONT_SIZE) # Title label font.
        period_font = Font(family=PERIOD_FONT_FAMILY, size=PERIOD_FONT_SIZE) # Period labels font.
        group_font = Font(family=GROUP_FONT_FAMILY, size=GROUP_FONT_SIZE) # Group labels font.
        aux_font = Font(family=AUX_FONT_FAMILY, size=AUX_FONT_SIZE) # Auxiliar labels font.

        # Title label creation.
        Label(self.mw, text=TITLE_TEXT, font=title_font).place(x=TITLE_X, y=X_BEGIN)

        # Periods labels creation.
        i = C_1
        for y in periods_positions:
            Label(self.mw, text=i, font=period_font).place(x=PERIOD_X, y=y + X_BEGIN)
            i += C_1

        # Groups labels creation.
        i = C_1
        for x, y in groups_positions.items():
            Label(self.mw, text=i, font=group_font).place(x=x + GROUP_X_FIX, y=y + GROUP_Y_FIX)
            i += C_1

        # Lanthanoid and actinoid labels creation. Next x and y values are hardcoded.
        Label(self.mw, text=LANTHANOID_MARK, font=aux_font).place(x=LANTHANOID_X, y=LANTHANOID_Y1)
        Label(self.mw, text=ACTINOID_MARK, font=aux_font).place(x=ACTINOID_X, y=ACTINOID_Y1)
        Label(self.mw, text=LANTHANOID_MARK, font=aux_font).place(x=LANTHANOID_X, y=LANTHANOID_Y2)
        Label(self.mw, text=ACTINOID_MARK, font=aux_font).place(x=ACTINOID_X, y=ACTINOID_Y2)

    def work(self): # Main window runner.
        self.mw.mainloop() # Main window run.
