from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter.colorchooser import askcolor
from supp_file import Classes,ClassDescriptions, Class_images,Races, RaceDescriptions,Race_images

HairColor = "#000000"
EyeColor = "#000000"
hairstyles = ["Короткая", "Длинная", "Ирокез", "Лысая"]
selected_class = ""
selected_race = ""
selected_hair = ""

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

        for F in (MainMenu,CharacterCreation,GenerateImage,Settings):
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
            style="DnD.TButton",
            command=lambda: controller.show_frame(GenerateImage)
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
    global HairColor
    global selected_class
    global selected_race
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
        ).place(relx=0.65,rely=0.9)

        ttk.Button(
            self,
            text="Выберите расу",
            command= self.choose_race
        ).place(relx=0.01,rely=0.1)

        ttk.Button(
            self,
            text="Выберите класс",
            command= self.choose_class
        ).place(relx=0.01,rely=0.2)

        ttk.Button(
            self,
            text="Редактировать внешность",
            command= self.appearance
        ).place(relx=0.8,rely=0.1)


    def choose_race(self):
        global selected_race
        db_window = Toplevel(self)
        db_window.title("Race selection")
        db_window.geometry("1000x700")
        db_window.configure(bg="#252525")

        control_frame = Frame(db_window, bg="#252525")
        control_frame.pack(fill=X, padx=10, pady=10)
        
        Label(control_frame, 
              text="Выберите расу персонажа:", 
              bg="#252525", 
              fg="white").pack(side=LEFT, padx=5)
        
        RaceMenu = ttk.Combobox(control_frame, values=Races, state="readonly")
        RaceMenu.pack(side=LEFT, padx=5)
        RaceMenu.set("Выберите расу...")
        
        text_frame = Frame(db_window, bg="#252525")
        text_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0,10))
        
        text_scroll = Scrollbar(text_frame)
        text_scroll.pack(side=RIGHT, fill=Y)
        
        text_output = Text(
            text_frame,
            bg="#1e1e1e",
            fg="white",
            font=("Consolas", 12),
            wrap=WORD,
            width=80,
            height=30,
            yscrollcommand=text_scroll.set,
            padx=10,
            pady=10
        )
        text_output.pack(fill=BOTH, expand=True)
        text_scroll.config(command=text_output.yview)

        def on_race_selected(event):
            global selected_race
            selected_race = RaceMenu.get()
            text_output.delete(1.0, END)  
            
            if selected_race in RaceDescriptions:
                
                text_output.insert(END, RaceDescriptions[selected_race])
                if selected_race in Race_images:
                    try:
                        img_path = Race_images[selected_race]
                        pil_img = Image.open(img_path)
                        pil_img.thumbnail((300, 300))
                
                        self.race_img = ImageTk.PhotoImage(pil_img)
        
                        text_output.image_create(END, image=self.race_img, padx=10, pady=10)
                    except Exception as e:
                        print(f"Ошибка загрузки изображения: {e}")

                text_output.tag_configure("quote", foreground="#a0a0a0", font=("Consolas", 10, "italic"))
                text_output.tag_add("quote", "end-3l", "end")
                text_output.see(END)
        
        RaceMenu.bind("<<ComboboxSelected>>", on_race_selected)

    def choose_class(self):
        global selected_class
        db_window = Toplevel(self)
        db_window.title("Class selection")
        db_window.geometry("1000x700")
        db_window.configure(bg="#252525")

        control_frame = Frame(db_window, bg="#252525")
        control_frame.pack(fill=X, padx=10, pady=10)
        
        Label(control_frame, 
              text="Выберите класс персонажа:", 
              bg="#252525", 
              fg="white").pack(side=LEFT, padx=5)
        
        ClassesMenu = ttk.Combobox(control_frame, values=Classes, state="readonly")
        ClassesMenu.pack(side=LEFT, padx=5)
        ClassesMenu.set("Выберите класс...")
        
        text_frame = Frame(db_window, bg="#252525")
        text_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0,10))
        
        text_scroll = Scrollbar(text_frame)
        text_scroll.pack(side=RIGHT, fill=Y)
        
        text_output = Text(
            text_frame,
            bg="#1e1e1e",
            fg="white",
            font=("Consolas", 12),
            wrap=WORD,
            width=80,
            height=30,
            yscrollcommand=text_scroll.set,
            padx=10,
            pady=10
        )
        text_output.pack(fill=BOTH, expand=True)
        text_scroll.config(command=text_output.yview)

        def on_class_selected(event):
            global selected_class
            selected_class = ClassesMenu.get()
            text_output.delete(1.0, END)  
            
            if selected_class in ClassDescriptions:
                
                text_output.insert(END, ClassDescriptions[selected_class])
                if selected_class in Class_images:
                    try:
                        img_path = Class_images[selected_class]
                        pil_img = Image.open(img_path)
                        pil_img.thumbnail((300, 300))
                
                        self.class_img = ImageTk.PhotoImage(pil_img)
        
                        text_output.image_create(END, image=self.class_img, padx=10, pady=10)
                    except Exception as e:
                        print(f"Ошибка загрузки изображения: {e}")

                text_output.tag_configure("quote", foreground="#a0a0a0", font=("Consolas", 10, "italic"))
                text_output.tag_add("quote", "end-3l", "end")
                text_output.see(END)
        
        ClassesMenu.bind("<<ComboboxSelected>>", on_class_selected)
    def appearance(self):
        db_window = Toplevel(self)
        db_window.title("Class selection")
        db_window.geometry("1000x700")
        db_window.configure(bg="#252525")

        control_frame = Frame(db_window, bg="#252525")
        control_frame.pack(fill=X, padx=10, pady=10)
        HairMenu = ttk.Combobox(db_window, values=hairstyles, state="readonly")
        HairMenu.place(relx=0.01, rely=0.1)
        HairMenu.set("Стиль прически...")
        Label(control_frame, 
              text="Внешность:", 
              bg="#252525", 
              fg="white").pack(side=LEFT, padx=5)
        
        def hair_color():
            global HairColor
            color = askcolor(title="Выберите цвет")  # Возвращает кортеж ((R, G, B), "#rrggbb")
            if color[1]:  # Если цвет выбран (не None)
                HairColor = color[0]
                print("Выбранный цвет (RGB):", color[0])
                print("HEX-код:", color[1])
        def eye_color():
            global EyeColor
            color = askcolor(title="Выберите цвет")  # Возвращает кортеж ((R, G, B), "#rrggbb")
            if color[1]:  # Если цвет выбран (не None)
                EyeColor = color[0]
                print("Выбранный цвет (RGB):", color[0])
                print("HEX-код:", color[1])
        def on_hair_selected(event):
             global selected_hair
             selected_hair = HairMenu.get()
             print(selected_hair)
        HairMenu.bind("<<ComboboxSelected>>", on_hair_selected)     
        ttk.Button(db_window, text="Цвет прически", command=hair_color).place(relx=0.01,rely=0.2)
        ttk.Button(db_window, text="Цвет глаз", command=eye_color).place(relx=0.01,rely=0.3)
        
class GenerateImage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#121212")

        Label(self, text = "D&D Character Creator",
              font = ("Arial",20,"bold"),
              bg="#121212",
              fg = "#e0e0e0"
              ).pack(anchor="center")
        ttk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: controller.show_frame(MainMenu),
            style="DnD.TButton"
        ).place(relx=0.65,rely=0.9)

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
   
