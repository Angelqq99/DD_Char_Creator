from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk

class DnDApp(Tk):
    def __init__ (self):
        super().__init__()

        self.title("D&D Creator")
        self.geometry("800x700")
        self.configure(bg="#121212")
        self.iconbitmap("D:\Programming\Projects\DD_Char_Creator\items\icon.ico")
        self.resizable(False,False)
        self.container = Frame(self, bg="#121212")
        self.container.pack(fill="both", expand=True,)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        self.big_btn_style = ttk.Style()
        self.big_btn_style.configure("DnD.TButton",
            font=("system", 14),
            padding=(30, 15),
            width  = 25,
            foreground="#000000",
            background="#000000")

        for F in (MainMenu,CharacterCreation,Settings):
            frame = F(self.container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#121212")
        
        
        
        Label(self, text = "D&D Character Creator",
              font = ("Arial",20,"bold"),
              bg="#121212",
              fg = "#e0e0e0"
              ).pack(anchor="center")
        
        ttk.Button(
            self,
            text="START DESIGNING",
            style="DnD.TButton"
        ).place(relx=0.01,rely=0.1)

        ttk.Button(
            self,
            text="CREATE NEW CHARACTER",
            style="DnD.TButton",
            command=lambda: controller.show_frame(CharacterCreation)
        ).place(relx=0.01,rely=0.2)

        self.settings_img = ImageTk.PhotoImage(file="D:\Programming\Projects\DD_Char_Creator\items\settings.png")
        settings_btn = ttk.Button(
            self,
            image=self.settings_img,
            command=lambda: controller.show_frame(Settings),
            #style="DnD.TButton"
        ).place(relx=0.9, rely=0.89)
        self.settings_btn = settings_btn  

        

class CharacterCreation(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#121212")
        Label(self, text = "Character Creation",
              font = ("Arial",20,"bold"),
              bg="#121212",
              fg = "#e0e0e0"
              ).pack(anchor="center")
        
        ttk.Button(
        self,
        text="Back to Main Menu",
        command=lambda: controller.show_frame(MainMenu),
        style="DnD.TButton"
        ).pack(pady=30)

class Settings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#121212")

        Label(self, text = "Settings",
              font = ("Arial",20,"bold"),
              bg="#121212",
              fg = "#e0e0e0"
              ).pack(anchor="center")
        
        ttk.Button(
        self,
        text="Back to Main Menu",
        command=lambda: controller.show_frame(MainMenu),
        style="DnD.TButton"
        ).pack(pady=30)  
if __name__ == "__main__":
    app = DnDApp()
    app.mainloop()