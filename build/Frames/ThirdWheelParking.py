import tkinter as tk
from f1_Login import LoginPage
from f2_Home import HomePage
from f3_Logs import LogsPage
from f4_Park import ParkPage
from f5_Unpark import UnparkPage
from f6_Graph import GraphPage


pages = {
    "LoginPage": LoginPage,
    "HomePage": HomePage,
    "LogsPage" : LogsPage,
    "ParkPage" : ParkPage,
    "UnparkPage" : UnparkPage,
    "GraphPage" : GraphPage
}

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1200x600")
        self.title("Third Wheel Parking Lot")
        self.configure(bg='grey')

        ico = tk.PhotoImage( file= r"C:\Users\alama\OneDrive\Desktop\Parking Lot System\build\Frames\CSV files\toico.png")
        self.iconphoto(False, ico)

        self._frame = None
        self.switch_frame("GraphPage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master = self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()