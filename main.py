class AuthSystem:
    def __init__(self):
        self.users = {}

    def register(self, login, password):
        if login not in self.users:
            self.users[login] = password
            print("Ro'yxatdan o'tish muvaffaqiyatli bajarildi")
        else:
            print("Bunday login allaqachon mavjud")

    def login(self, login, password):
        if login in self.users and self.users[login] == password:
            print("Siz tizimga muvaffaqiyatli kirishdingiz")
        else:
            print("Login yoki parol noto'g'ri")

    def change_password(self, login, old_password, new_password):
        if login in self.users and self.users[login] == old_password:
            self.users[login] = new_password
            print("Parol muvaffaqiyatli o'zgartirildi")
        else:
            print("Login yoki parol noto'g'ri")

    def delete_user(self, login, password):
        if login in self.users and self.users[login] == password:
            del self.users[login]
            print("Foydalanuvchi muvaffaqiyatli o'chirildi")
        else:
            print("Login yoki parol noto'g'ri")

def main():
    auth = AuthSystem()
    while True:
        print("1. Ro'yxatdan o'tish")
        print("2. Tizimga kirish")
        print("3. Parolni o'zgartirish")
        print("4. Foydalanuvchini ochirish")
        print("5. Chiqish")
        choice = input("Buyruqni tanlang: ")
        if choice == "1":
            login = input("Login ni kiriting: ")
            password = input("Parol ni kiriting: ")
            auth.register(login, password)
        elif choice == "2":
            login = input("Login ni kiriting: ")
            password = input("Parol ni kiriting: ")
            auth.login(login, password)
        elif choice == "3":
            login = input("Login ni kiriting: ")
            old_password = input("Eski parol ni kiriting: ")
            new_password = input("Yangi parol ni kiriting: ")
            auth.change_password(login, old_password, new_password)
        elif choice == "4":
            login = input("Login ni kiriting: ")
            password = input("Parol ni kiriting: ")
            auth.delete_user(login, password)
        elif choice == "5":
            break
        else:
            print("Noto'g'ri buyruq")

if __name__ == "__main__":
    main()