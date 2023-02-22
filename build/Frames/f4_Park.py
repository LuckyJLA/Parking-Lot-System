from tkinter import Button, Frame, Label, PhotoImage, Entry
import datetime as dt
from behind import button_color, go_park, lotcheck

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ParkPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master,bg='#EEEEEE', height=600, width=1200 )
        self.pack

        #Title
        image_image_2 = PhotoImage( file=relative_to_assets("image_2.png"))
        label = Label(self, image=image_image_2)
        label.place(x=0, y=0)
        label.image=image_image_2

        #Frame for Entries
        image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
        label1 = Label(self, image=image_image_1)
        label1.place(x=867, y=81)
        label1.image=image_image_1

        #Parking Lot Number Entry Box
        entry_image_1 = PhotoImage( file=relative_to_assets("entry_1.png"))
        label2 = Label(self, image=entry_image_1)
        label2.place(x=888, y=280)
        label2.image=entry_image_1
        parklotnum = Entry( self, bd=0, bg="#EBEBEB", fg="green", highlightthickness=0,
            font="Arial 16" , justify="center")
        parklotnum.place( x=895.0, y=285.0, width=260.0, height=40.0 )

        #TimeStamp Entry Box
        entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
        label3 = Label(self, image=entry_image_2)
        label3.place(x=888, y=372)
        label3.image=entry_image_2
        timenow = Entry( self, bd=0, bg="#EBEBEB", fg="blue", highlightthickness=0,
            font="Arial 16" , justify="center" )
        timenow.place( x=895.0, y=380.0, width=260.0, height=40.0 )

        #inserts new info in the entry space
        def new_info(new_lot):
            if lotcheck(new_lot, "Park") == True:
                new_time = dt.datetime.now().strftime('%m/%d/%Y %I:%M %p')
                parklotnum.delete(0, 'end')
                timenow.delete(0, 'end')
                timenow.insert(0, new_time)
                parklotnum.insert(0, new_lot)

        #confirms the transactions
        def confirm_transaction():
            if go_park(parklotnum.get(), timenow.get()) == True:
                master.switch_frame("HomePage")

        #Park Button
        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
        button_1 = Button( self, image=button_image_1, borderwidth=0, highlightthickness=0,
            command=lambda: confirm_transaction(), relief="flat" )
        button_1.place( x=961.0, y=462.0, width=122.0, height=50.0 )
        button_1.image = button_image_1

        #Cancel Button
        button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
        button_2 = Button( self, image=button_image_2, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("HomePage"), relief="flat" )
        button_2.place( x=961.0, y=531.0, width=122.0, height=50.0 )
        button_2.image = button_image_2

        lotnum_101 = Button(self, text='101', font= ('Arial 40'), background=button_color(101), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(101), relief="flat" )
        lotnum_101.place( x=26.0, y=81.0, width=203.0, height=76.0 )

        lotnum_102 = Button(self, text='102', font= ('Arial 40'), background=button_color(102), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(102), relief="flat" )
        lotnum_102.place( x=26.0, y=184.0, width=203.0, height=76.0 )

        lotnum_103 = Button(self, text='103', font= ('Arial 40'), background=button_color(103), activebackground= "#b0b0b0",
                borderwidth=0, highlightthickness=0, command=lambda: new_info(103), relief="flat" )
        lotnum_103.place( x=26.0, y=288.0, width=203.0, height=76.0 )
                
        lotnum_104 = Button(self, text='104', font= ('Arial 40'), background=button_color(104), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(104), relief="flat" )
        lotnum_104.place( x=26.0, y=392.0, width=203.0, height=76.0 )

        lotnum_105 = Button(self, text='105', font= ('Arial 40'), background=button_color(105), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(105), relief="flat" )
        lotnum_105.place( x=26.0, y=495.0, width=203.0, height=76.0 )

        lotnum_201 = Button(self, text='201', font= ('Arial 40'), background=button_color(201), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(201), relief="flat" )
        lotnum_201.place( x=326.0, y=81.0, width=203.0, height=76.0 )
                
        lotnum_202 = Button(self, text='202', font= ('Arial 40'), background=button_color(202), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(202), relief="flat" )
        lotnum_202.place( x=326.0, y=184.0, width=203.0, height=76.0 )

        lotnum_203 = Button(self, text='203', font= ('Arial 40'), background=button_color(203), activebackground= "#b0b0b0",
            highlightthickness=0, command=lambda: new_info(203), relief="flat" )
        lotnum_203.place( x=326.0, y=288.0, width=203.0, height=76.0 )

        lotnum_204 = Button(self, text='204', font= ('Arial 40'), background=button_color(204), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(204), relief="flat" )
        lotnum_204.place( x=326.0, y=392.0, width=203.0, height=76.0 )

        lotnum_205 = Button(self, text='205', font= ('Arial 40'), background=button_color(205), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(205), relief="flat" )
        lotnum_205.place( x=326.0, y=495.0, width=203.0, height=76.0 )

        lotnum_301 = Button(self, text='301', font= ('Arial 40'), background=button_color(301), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(301), relief="flat" )
        lotnum_301.place( x=627.0, y=81.0, width=203.0, height=76.0 )

        lotnum_302 = Button(self, text='302', font= ('Arial 40'), background=button_color(302), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(302), relief="flat" )
        lotnum_302.place( x=627.0, y=184.0, width=203.0, height=76.0 )

        lotnum_303 = Button( self, text='303', font= ('Arial 40'), background=button_color(303), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(303), relief="flat" )
        lotnum_303.place( x=627.0, y=288.0, width=203.0, height=76.0 )

        lotnum_304 = Button( self, text='304', font= ('Arial 40'), background=button_color(304), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(304), relief="flat")
        lotnum_304.place( x=627.0, y=392.0, width=203.0, height=76.0 )
            
        lotnum_305 = Button( self, text='305', font= ('Arial 40'), background=button_color(305), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: new_info(305), relief="flat" )
        lotnum_305.place( x=627.0, y=495.0, width=203.0, height=76.0 )

if __name__ == "__main__":
    app = ParkPage()
    app.mainloop
