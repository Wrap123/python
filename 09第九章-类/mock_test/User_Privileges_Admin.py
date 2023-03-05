"""动手试一试，练习9-10"""
# 创建模块，在Import_Test.py中进行导入测试


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "ca delete post", "can ban user"]

    def show_privileges(self):
        print(f"The man's privileges is:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"This person's name is {self.first_name}{self.last_name}.")


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        # self.privileges = ["can add post", "ca delete post", "can ban user"]
        print(f"His name is {first_name}{last_name}.")
        self.privileges = Privileges()