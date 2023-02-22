from tkinter import Button, Frame, Label, PhotoImage

from behind import button_color

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master,bg='#EEEEEE', height=600, width=1200 )
        self.pack

        #title
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        label = Label(self, image=image_image_1)
        label.place(x=0, y=0)
        label.image=image_image_1

        #MainMenu Frame
        image_image_2 = PhotoImage( file=relative_to_assets("image_2.png"))
        label1 = Label(self, image=image_image_2)
        label1.place(x=867, y=81)
        label1.image=image_image_2
        
        #Logout Button
        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
        button_1 = Button( self, image=button_image_1, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("LoginPage"), relief="flat" )
        button_1.place( x=905.0, y=476.0, width=229.0, height=71.0 )
        button_1.image = button_image_1

        #Logs Button
        button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
        button_2 = Button( self, image=button_image_2, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("LogsPage"), relief="flat" )
        button_2.place( x=905.0, y=375.0, width=229.0, height=71.0 )
        button_2.image = button_image_2

        #Unpark Button
        button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
        button_3 = Button( self, image=button_image_3, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("UnparkPage"), relief="flat" )
        button_3.place( x=905.0, y=273.0, width=229.0, height=71.0 )
        button_3.image = button_image_3

        #Park Button
        button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
        button_4 = Button( self, image=button_image_4, borderwidth=0, highlightthickness=0,
            command=lambda: master.switch_frame("ParkPage"), relief="flat" )
        button_4.place( x=905.0, y=172.0, width=229.0, height=72.0 )
        button_4.image = button_image_4

        lotnum_101 = Button(self, text='101', font= ('Arial 40'), background=button_color(101), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_101 clicked"), relief="flat" )
        lotnum_101.place( x=26.0, y=81.0, width=203.0, height=76.0 )

        lotnum_102 = Button(self, text='102', font= ('Arial 40'), background=button_color(102), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_102 clicked"), relief="flat" )
        lotnum_102.place( x=26.0, y=184.0, width=203.0, height=76.0 )

        lotnum_103 = Button(self, text='103', font= ('Arial 40'), background=button_color(103), activebackground= "#b0b0b0",
                borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_103 clicked"), relief="flat" )
        lotnum_103.place( x=26.0, y=288.0, width=203.0, height=76.0 )
                
        lotnum_104 = Button(self, text='104', font= ('Arial 40'), background=button_color(104), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_104 clicked"), relief="flat" )
        lotnum_104.place( x=26.0, y=392.0, width=203.0, height=76.0 )

        lotnum_105 = Button(self, text='105', font= ('Arial 40'), background=button_color(105), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_105 clicked"), relief="flat" )
        lotnum_105.place( x=26.0, y=495.0, width=203.0, height=76.0 )

        lotnum_201 = Button(self, text='201', font= ('Arial 40'), background=button_color(201), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_201 clicked"), relief="flat" )
        lotnum_201.place( x=326.0, y=81.0, width=203.0, height=76.0 )
                
        lotnum_202 = Button(self, text='202', font= ('Arial 40'), background=button_color(202), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_202 clicked"), relief="flat" )
        lotnum_202.place( x=326.0, y=184.0, width=203.0, height=76.0 )

        lotnum_203 = Button(self, text='203', font= ('Arial 40'), background=button_color(203), activebackground= "#b0b0b0",
            highlightthickness=0, command=lambda: print("lotnum_203 clicked"), relief="flat" )
        lotnum_203.place( x=326.0, y=288.0, width=203.0, height=76.0 )

        lotnum_204 = Button(self, text='204', font= ('Arial 40'), background=button_color(204), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_204 clicked"), relief="flat" )
        lotnum_204.place( x=326.0, y=392.0, width=203.0, height=76.0 )

        lotnum_205 = Button(self, text='205', font= ('Arial 40'), background=button_color(205), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_205 clicked"), relief="flat" )
        lotnum_205.place( x=326.0, y=495.0, width=203.0, height=76.0 )

        lotnum_301 = Button(self, text='301', font= ('Arial 40'), background=button_color(301), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_302 clicked"), relief="flat" )
        lotnum_301.place( x=627.0, y=81.0, width=203.0, height=76.0 )

        lotnum_302 = Button(self, text='302', font= ('Arial 40'), background=button_color(302), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_302 clicked"), relief="flat" )
        lotnum_302.place( x=627.0, y=184.0, width=203.0, height=76.0 )

        lotnum_303 = Button( self, text='303', font= ('Arial 40'), background=button_color(303), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_303 clicked"), relief="flat" )
        lotnum_303.place( x=627.0, y=288.0, width=203.0, height=76.0 )

        lotnum_304 = Button( self, text='304', font= ('Arial 40'), background=button_color(304), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_304 clicked"), relief="flat")
        lotnum_304.place( x=627.0, y=392.0, width=203.0, height=76.0 )
            
        lotnum_305 = Button( self, text='305', font= ('Arial 40'), background=button_color(305), activebackground= "#b0b0b0",
            borderwidth=0, highlightthickness=0, command=lambda: print("lotnum_305 clicked"), relief="flat" )
        lotnum_305.place( x=627.0, y=495.0, width=203.0, height=76.0 )

        

if __name__ == "__main__":
    app = HomePage()
    app.mainloop()
        