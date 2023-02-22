from tkinter import Button, Frame, Label, PhotoImage
from tkinter import *
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GraphPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, bg='#EEEEEE', height=600, width=1200)
        self.pack()

        place = Frame(self, bg='#EEEEEE', height=450, width=780)
        place.place(x=65, y=119)

        # Load data from CSV file
        data = pd.read_csv(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\DailyCount.csv")

        # Convert the 'Date' column to datetime format
        data['Date'] = pd.to_datetime(data['Date'].tail(7))

        # Create a figure and a set of subplots
        fig, ax = plt.subplots(figsize=(7.5, 4.5))

        # Convert the x-axis values to matplotlib date format
        x = mdates.date2num(data['Date'])

        # Set the x-ticks to be every other day
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

        # Set the x-tick labels to be in a specific format
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

        # Set the x-axis label and the y-axis label
        ax.set_xlabel('Date')
        ax.set_ylabel('Number')

        # Plot the data as a bar chart
        ax.bar(x, data['Number'])

        canvas = FigureCanvasTkAgg(fig, master=place)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # title
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        label = Label(self, image=image_image_2)
        label.place(x=0, y=0)
        label.image = image_image_2

        # Table Button
        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        button_5 = Button(self, image=button_image_5, borderwidth=0, highlightthickness=0,
                          command=lambda: master.switch_frame("LogsPage"), relief="flat")
        button_5.place(x=48.0, y=81.0, width=390.0, height=31.0)
        button_5.image = button_image_5

        # Bar Graph Button
        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        button_6 = Button(self, image=button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: print("None"), relief="flat")
        button_6.place(x=447.0, y=81.0, width=390.0, height=31.0)
        button_6.image = button_image_6

        # Menu Frame
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        label1 = Label(self, image=image_image_1)
        label1.place(x=867, y=81)
        label1.image = image_image_1

        # Log Out Button
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(self, image=button_image_1, borderwidth=0, highlightthickness=0,
                          command=lambda: master.switch_frame("LoginPage"), relief="flat")
        button_1.place(x=905.0, y=476.0, width=229.0, height=71.0)
        button_1.image = button_image_1

        # Unpark Button
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(self, image=button_image_2, borderwidth=0, highlightthickness=0,
                          command=lambda: master.switch_frame("UnparkPage"), relief="flat")
        button_2.place(x=905.0, y=375.0, width=229.0, height=71.0)
        button_2.image = button_image_2

        # Park Button
        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(self, image=button_image_3, borderwidth=0, highlightthickness=0,
                          command=lambda: master.switch_frame("ParkPage"), relief="flat")
        button_3.place(x=905.0, y=273.0, width=229.0, height=73.0)
        button_3.image = button_image_3

        # Home Button
        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_4 = Button(self, image=button_image_4, borderwidth=0, highlightthickness=0,
                          command=lambda: master.switch_frame("HomePage"), relief="flat")
        button_4.place(x=905.0, y=172.0, width=229.0, height=71.0)
        button_4.image = button_image_4


if __name__ == "__main__":
    app = GraphPage()
    app.mainloop()