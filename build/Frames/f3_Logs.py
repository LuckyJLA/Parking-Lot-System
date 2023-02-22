from tkinter import Button, Frame, Label, PhotoImage
from tkinter import *
import tkinter.ttk as ttk
import csv


from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LogsPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master,bg='#EEEEEE', height=600, width=1200 )
        self.pack

        
        place = Frame(self, bg='#EEEEEE', height=440, width=780)
        place.place(x=75, y=119)

        table_scroll = Scrollbar(place)
        table_scroll.pack(side=RIGHT, fill=Y)

        table = ttk.Treeview(place)
        table.config(height="10", selectmode="browse")
        table.pack(fill=BOTH, expand=True)

        # config scroll bar
        table_scroll.config(command=table.yview)
        table.config(yscrollcommand=table_scroll.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial 16'))
        style.configure("Treeview", font=('Arial 16'))
        style.configure("Treeview", background='White', rowheight=50)

        # defining table colums
        table['columns'] = ("Timestamp", "Lot Number", "Parking", "Counter")
        table.column('#0', minwidth=0, width=0)
        table.column('Timestamp', minwidth=0, width=380, anchor=W)
        table.column('Lot Number', minwidth=0, width=150, anchor=CENTER)
        table.column('Parking', minwidth=0, width=100, anchor=CENTER)
        table.column('Counter', minwidth=0, width=100, anchor=CENTER)

        # Create headings
        table.heading('Timestamp', text="Time Stamp", anchor=W)
        table.heading('Lot Number', text="Lot Number", anchor=CENTER)
        table.heading('Parking', text="Parking", anchor=CENTER)
        table.heading('Counter', text="Counter", anchor=CENTER)

        with open(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\ParkingLog.csv") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                timestamp = row['timestamp']
                lot_num = row['lot_num']
                in_out = row['in_out']
                parked_counter = row['parked_counter']
                table.insert("", 0, values=(timestamp, lot_num, in_out, parked_counter))

        #title
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        label = Label(self, image=image_image_2)
        label.place(x=0, y=0)
        label.image=image_image_2

        #Table Button
        button_image_5 = PhotoImage( file=relative_to_assets("button_5.png"))
        button_5 = Button( self, image=button_image_5, borderwidth=0, highlightthickness=0,
            command=lambda: print("button_5 clicked"), relief="flat" )
        button_5.place( x=48.0, y=81.0, width=390.0, height=31.0 )
        button_5.image = button_image_5

        #Bar Graph Button
        button_image_6 = PhotoImage( file=relative_to_assets("button_6.png"))
        button_6 = Button( self, image=button_image_6, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("GraphPage"), relief="flat" )
        button_6.place( x=447.0, y=81.0, width=390.0, height=31.0 )
        button_6.image = button_image_6

        #Menu Frame
        image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
        label1 = Label(self, image=image_image_1)
        label1.place(x=867, y=81)
        label1.image=image_image_1

        #Log Out Button
        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
        button_1 = Button( self, image=button_image_1, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("LoginPage"), relief="flat" )
        button_1.place( x=905.0, y=476.0, width=229.0, height=71.0 )
        button_1.image = button_image_1

        #Unpark Button
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button( self, image=button_image_2, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("UnparkPage"), relief="flat" )
        button_2.place( x=905.0, y=375.0, width=229.0, height=71.0 )
        button_2.image = button_image_2

        #Park Button
        button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
        button_3 = Button( self, image=button_image_3, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("ParkPage"), relief="flat")
        button_3.place( x=905.0, y=273.0, width=229.0, height=73.0 )
        button_3.image = button_image_3

        #Home Button
        button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
        button_4 = Button( self, image=button_image_4, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("HomePage"), relief="flat" )
        button_4.place( x=905.0, y=172.0, width=229.0, height=71.0 )
        button_4.image = button_image_4

        


if __name__ == "__main__":
    app = LogsPage()
    app.mainloop()

