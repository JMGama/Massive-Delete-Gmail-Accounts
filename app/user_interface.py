from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

class UserInterface:

    def select_file(self):
        """
        Show a window where you select the
        Excel file with the users and emails to delete.
        """

        Tk().withdraw()
        file_direction = askopenfilename(filetypes=(("Todos los archivos de Excel","*.xls"),("Todos los archivos de Excel","*.xlsx")), title='Abrir archivo')
        return file_direction
