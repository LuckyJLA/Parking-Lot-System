from tkinter import Entry, Button, Frame, Label,PhotoImage, messagebox

from behind import login

from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master,bg='#EEEEEE', height=600, width=1200)
        self.pack()

        #title image
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        label = Label(self, image=image_image_2)
        label.place(x=0, y=0)
        label.image=image_image_2
        
        #template image
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        label1 = Label(self, image=image_image_1)
        label1.place(x=270, y=81)
        label1.image=image_image_1

        #Username Image
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        label2 = Label(self, image=entry_image_1)
        label2.place(x=415, y=400, height=35, width=370)
        label2.image=entry_image_1

        #Username entry
        entry_2 = Entry( self, bd=0, bg="#EEEEEE", fg="#000716", highlightthickness=0, font="Arial 16" )
        entry_2.place( x=430.0, y=405, width=340.0, height=25.0 )

        #Password Image
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        label3 = Label(self, image=entry_image_1)
        label3.place(x=415, y=465, height=35, width=370)
        label3.image=entry_image_1

        #Password entry
        entry_1 = Entry( self, bd=0, bg="#EEEEEE", fg="#000716", highlightthickness=0, font="Arial 16", show= "*" )
        entry_1.place( x=430.0, y=470, width=340.0, height=25.0)

        #checks if credentials are right and calls HomePage
        def check(u, p):
            if (login(u,p) == True):
                master.switch_frame("HomePage")
            
        #Login Button
        button_image_1 = PhotoImage( file=relative_to_assets("button_1.png") )
        button_1 = Button( self, image=button_image_1, borderwidth=0, highlightthickness=0, background="white",
            command=lambda: check(entry_2.get(), entry_1.get()), relief="flat" )
        button_1.place( x=670.0, y=506.0, width=109.15969848632812, height=39.3572998046875)
        button_1.image = button_image_1

        

        
        
        

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
        