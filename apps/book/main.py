from sqlalchemy import create_engine
import tkinter as tk
<<<<<<< Updated upstream
import menu
=======
from PIL import Image, ImageTk
import menu
from variables import *
>>>>>>> Stashed changes

#USER = 'sashimitrash'
#PASSWORD = ''
#HOST = '127.0.0.1'
#PORT = 3306
#DATABASE = 'Library'

#engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}[:{3}]/{4}'.format(USER, PASSWORD, HOST, PORT, DATABASE))
#cursor = engine.connect()

<<<<<<< Updated upstream
root = tk.Tk()
root.title("Book Menu")

canvas = tk.Canvas(root, width = 600, height = 400)
canvas.grid(columnspan = 3)

#instructions
instructions = tk.Label(root, text = "Select one of the Options below", font = "Arial")
instructions.grid(columnspan = 3, column = 0, row = 0)

#acquisition button
aquisition_txt = tk.StringVar()
aquisition_btn = tk.Button(root, command = lambda:menu.book(), textvariable = aquisition_txt, bg = "cyan", fg = "white", height = 4, width = 30)
aquisition_txt.set("Book Acquisition")
aquisition_btn.grid(columnspan = 2, column = 3, row = 1)

#withdrawal button
withdraw_txt = tk.StringVar()
withdraw_btn = tk.Button(root, textvariable = withdraw_txt, bg = "cyan", fg = "white", height = 4, width = 30)
withdraw_txt.set("Book Withdrawal")
withdraw_btn.grid(columnspan = 2, column = 3, row = 2)

#main menu button
home_txt = tk.StringVar()
home_btn = tk.Button(root, textvariable = home_txt, bg = "black", fg = "white", height = 4, width = 30)
home_txt.set("Back to Main Menu")
home_btn.grid(column = 0, row = 3)

canvas = tk.Canvas(root, width = 600, height = 250)
canvas.grid(columnspan = 3)
=======
class BookLandingPage:
    def __init__(self, root):
        self.root = root
        root.title("Book Menu")

        def getroot(self):
            return self.root

        # container window, everything will be added to this container
        self.container = tk.Frame(root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.container.grid()

        #instructions
        instructions = tk.Label(self.container, text='Select one of the options below:', fg='black', bg='#c5e3e5',
                           relief='raised', width=60, height=3)
        instructions.config(font=(FONT, FONT_SIZE, STYLE))
        instructions.place(relx=0.5, rely=0.09, anchor="center")

        #acquisition button
        aquisition_btn = tk.Button(self.container, command = lambda:menu.bookinsert(tk.Tk()),
                                   text="Book Acquisition", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        aquisition_btn.config(font=(FONT, FONT_SIZE, STYLE))
        aquisition_btn.place(relx=0.7, rely=0.3, anchor='center')

        #withdrawal button
        withdraw_btn = tk.Button(self.container, command = lambda:menu.bookinsert(root),
                                   text="Book Withdrawal", bg='#c5e3e5', width=50, height=4, relief='raised', borderwidth=5)
        withdraw_btn.config(font=(FONT, FONT_SIZE, STYLE))
        withdraw_btn.place(relx=0.7, rely=0.5, anchor='center')
        
        #main menu button
        home_btn = tk.Button(self.container, text='Back to Main Menu', command=self.return_to_main_menu,
                                 bg='#c5e3e5', width=60, height=1, relief='raised', borderwidth=5)
        home_btn.config(font=(FONT, FONT_SIZE, STYLE))
        home_btn.place(relx=0.5, rely=0.7, anchor="center")  # return_btn is always mid align

    def return_to_main_menu(self):
        print("a")

root = tk.Tk()
book_landing_page = BookLandingPage(root)
root.mainloop()
>>>>>>> Stashed changes
