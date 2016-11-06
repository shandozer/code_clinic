#!/usr/bin/env python
"""
__author__ = Shannon B., 10/19/16
"""

import calendar
import datetime
from os import path
from tkinter import *
from tkinter import ttk

from lake_pend_oreille import statsDB

__verion__ = '0.1.0'


class WeatherScraperApp:
    """
    Main module for running weather scaper GUI
    """
    def __init__(self, master):
        self.master = master
        self._createGUI()
        self.database = statsDB.StatsDB()
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close)

    def _createGUI(self):

        # bg color
        bg_color = '#CCCCFF'

        self.master.configure(background=bg_color)
        self.master.title('Lake Pend Oreille (pohn-doh-RAY)')
        self.master.resizable(False, False)

        # More Styles to Config!
        self.style = ttk.Style()
        self.style.configure('TFrame', background=bg_color)
        self.style.configure('TButton', background=bg_color, font=('Times', 10, 'bold'))
        self.style.configure('TLabel', background=bg_color, font=('Times', 10, 'bold'))
        self.style.configure('Status.TLabel', background=bg_color, font=('Times', 10))
        self.style.configure('Result.TLabel', background=bg_color, font=('Courier', 10))

        # Create and Display header frame with logo image?
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side=TOP)
        self.logo = PhotoImage(file=path.join(path.dirname(sys.argv[0]), 'assets', 'lpo_logo.gif'))
        ttk.Label(self.frame_header, image=self.logo).pack()

        # create and display frame to hold user input widgets
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side=TOP)

        ttk.Label(self.frame_input, text='Start Date:').grid(row=0, column=1, columnspan=3)
        ttk.Label(self.frame_input, text='End Date:').grid(row=0, column=5, columnspan=3)

        # Setup User Input Vars
        self.start_day = StringVar()
        self.start_month = StringVar()
        self.start_year = StringVar()
        self.end_day = StringVar()
        self.end_month = StringVar()
        self.end_year = StringVar()
        self.months = tuple(calendar.month_abbr[i] for i in range(1, 13))

        Spinbox(self.frame_input, from_=1, to=31,
                textvariable = self.start_day, width=2,
                font='Courier 12').grid(row=1, column=1)

        Spinbox(self.frame_input, values = self.months,
                textvariable = self.start_month, width=3,
                font='Courier 12').grid(row=1, column=2)

        Spinbox(self.frame_input, from_=2000, to = datetime.date.today().year,
                textvariable=self.start_year, width=4,
                font='Courier 12').grid(row=1, column=3)

        Spinbox(self.frame_input, from_=1, to=31,
                textvariable=self.end_day, width=2,
                font='Courier 12').grid(row=1, column=5)

        Spinbox(self.frame_input, values=self.months,
                textvariable=self.end_month, width=3,
                font='Courier 12').grid(row=1, column=6)

        Spinbox(self.frame_input, from_=2000, to=datetime.date.today().year,
                textvariable=self.end_year, width=4,
                font='Courier 12').grid(row=1, column=7)

        # set default values to today
        self.start_day.set(datetime.date.today().day)
        self.start_month.set(self.months[datetime.date.today().month-1])
        self.start_year.set(datetime.date.today().year)
        self.end_month.set(self.months[datetime.date.today().month - 1])
        self.end_day.set(datetime.date.today().day)
        self.end_year.set(datetime.date.today().year)

        # padding labels
        ttk.Label(self.frame_input).grid(row=1, column=0, padx=5)
        ttk.Label(self.frame_input).grid(row=1, column=4, padx=5)
        ttk.Label(self.frame_input).grid(row=1, column=8, padx=5)

        ttk.Button(self.frame_input, text='Submit',
                   command=self._submit_callback).grid(row=2, column=0, columnspan=9, padx=5)

        # Now create frame to display results, but keep hidden until we validate -> similar to above

        self.frame_result = ttk.Frame(self.master)

        # Label the result headers (static)
        ttk.Label(self.frame_result, text='Mean:').grid(row=1, column=0, padx=5)
        ttk.Label(self.frame_result, text='Median:').grid(row=2, column=0, padx=5)

        ttk.Label(self.frame_result, text='Air\nTemp:',
                  justify=CENTER).grid(row=0, column=2, sticky='e', padx=5)
        ttk.Label(self.frame_result, text='Barometric\nPressure:',
                  justify=CENTER).grid(row=0, column=3, sticky='e', padx=5)
        ttk.Label(self.frame_result, text='Wind\nSpeed:',
                  justify=CENTER).grid(row=0, column=1, sticky='e', padx=5)

        self.air_temp_mean = StringVar()
        self.air_temp_median = StringVar()
        self.barotemtric_pressure_mean = StringVar()
        self.barotemtric_pressure_median = StringVar()
        self.wind_speed_mean = StringVar()
        self.wind_speed_median = StringVar()

        ttk.Label(self.frame_result, textvariable=self.air_temp_mean,
                  style='Result.TLabel').grid(row=1, column=2)
        ttk.Label(self.frame_result, textvariable=self.air_temp_median,
                  style='Result.TLabel').grid(row=2, column=2)
        ttk.Label(self.frame_result, textvariable=self.barotemtric_pressure_mean,
                  style='Result.TLabel').grid(row=1, column=3)
        ttk.Label(self.frame_result, textvariable=self.barotemtric_pressure_median,
                  style='Result.TLabel').grid(row=2, column=2)
        ttk.Label(self.frame_result, textvariable=self.wind_speed_mean,
                  style='Result.TLabel').grid(row=1, column=1)
        ttk.Label(self.frame_result, textvariable=self.wind_speed_median,
                  style='Result.TLabel').grid(row=2, column=1)

    def _submit_callback(self):
        pass

    def _safe_close(self):
        pass


def main():
    root = Tk()
    app = WeatherScraperApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
