from delete_script import DeleteScript
from manage_excel import ManageExcel
from user_interface import UserInterface

class Main:

    def __init__(self):
        self.users_deleted = 0
        self.m_excel = ManageExcel()

        self.total_users = self.m_excel.get_total_users()
        UserInterface.message_box("Usuarios encontrados", "Usuarios del Excel: " + str(self.total_users), 0)

        self.d_script = DeleteScript()
        self.delete_all_users()
        UserInterface.message_box("Usuarios borrados", "Se borraron " + str(self.users_deleted) + " usuarios.", 0)
        self.d_script.close_driver()

    def get_user_info(self):
        self.name = self.m_excel.get_name()
        self.email = self.m_excel.get_email()
        print(str(self.name) + ", " + str(self.email))

    def delete_all_users(self):
        for x in range(0, self.total_users):
            self.get_user_info()
            self.delete_user()
            self.m_excel.next_user()

    def delete_user(self):
        if self.d_script.search_user(self.name, self.email):
            if self.d_script.delete_user():
                self.d_script.uncheck_combobox()
                self.d_script.press_delete_button()
                self.d_script.check_correct_delete(self.name, self.email)
                self.users_deleted +=1
        else:
            #UserInterface.message_box("Usuarios no encontrado", "No se encontro el usuario:\n" + self.name + "\n" + self.email, 2)
            self.m_excel.set_unfound_user()

if __name__ == '__main__':
    main = Main()
