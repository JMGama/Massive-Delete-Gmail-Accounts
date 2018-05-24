from delete_script import DeleteScript
from read_excel import ReadExcel
from user_interface import UserInterface

def main():
    r_excel = ReadExcel()
    name = r_excel.get_name()
    email = r_excel.get_email()
    print(r_excel.get_total_users())
    #delete_user(name, email)

def delete_user(name, email):
    print("si entro, con el usuario: " + name + " Correo: " + email)

    d_script = DeleteScript()
    if d_script.search_user(name, email):
        if d_script.delete_user():
            d_script.uncheck_combobox()
            d_script.press_delete_button()
            d_script.check_correct_delete()
    else:
        print('no coincide el usuario')

if __name__ == '__main__':
    main()
