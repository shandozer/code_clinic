#!/usr/bin/env python
"""
__author__ = Shannon B., 10/19/16
"""

import os
import sys
from os import path
from tkinter import *
from tkinter import ttk, messagebox


__verion__ = '0.1.0'


# Customize
class ThisOleApp:
    """

    """
    def __init__(self, master):
        self.master = master
        self._createGUI()

        # Need to import a database to talk to?

        # Everyone needs closure
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close)

    def _createGUI(self):

        # Start configuring style

        # bg color
        bg_color = '#CCCCFF'
        self.master.configure(background=bg_color)

        # Title
        self.master.title('Title Here!')

        # Want to Resize? Nah
        self.master.resizable(False, False)

        # More Styles to Config?
        self.style = ttk.Style()

        # Create and Display header frame with logo image?
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side=TOP)
        self.logo = PhotoImage(file=path.join(path.dirname(sys.argv[0]), 'assets', 'lpo_logo.gif'))  # placeholder
        ttk.Label(self.frame_header, image=self.logo).pack()

        # create and display frame to hold user input widgets
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side=TOP)

    def _submit_callback(self):
        pass

    def _safe_close(self):
        pass


def main():
    root = Tk()

    # Customize
    app = ThisOleApp(root)

    root.mainloop()

if __name__ == '__main__':
    main()
