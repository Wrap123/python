# 模块之间相互调用，要用这种直接指定导入类的方式
# 否则在当前模块内的Admin子类使用方式要改为“class Admin(User.User)”
from User import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "ca delete post", "can ban user"]

    def show_privileges(self):
        print(f"The man's privileges is:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        # self.privileges = ["can add post", "ca delete post", "can ban user"]
        print(f"His name is {first_name}{last_name}.")
        self.privileges = Privileges()
