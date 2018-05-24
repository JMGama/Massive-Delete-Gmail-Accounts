from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class UserInterface:

    @staticmethod
    def select_file():
        """
        Show a window where you select the
        Excel file with the users and emails to delete.
        """

        Tk().withdraw()
        file_direction = askopenfilename(filetypes=(("Todos los archivos de Excel","*.xls"),("Todos los archivos de Excel","*.xlsx")), title='Abrir archivo')
        return file_direction

    @staticmethod
    def message_box(title, message, type):
        """
        Show a standard window with the message passed.
        """
        if type == 0:
            messagebox.showinfo(title, message)
        elif type == 1:
            messagebox.showerror(title, message)
        elif type == 2:
            messagebox.showwarning(title, message)
