class Employee:
    """全体员工姓名和年薪"""
    def __init__(self, fist_name, last_name, salary):
        """员工姓名和年薪金额"""
        self.first_name = fist_name
        self.last_name = last_name
        self.salary = salary
        self.new_salary = int()

    def give_raise(self, custom_raise=''):
        """默认加薪5000美元"""
        if custom_raise:
            self.new_salary = self.salary + custom_raise
            return self.new_salary
        else:
            self.new_salary = self.salary + 5000
            return self.new_salary

    def get_full_info(self):
        if self.salary == self.new_salary:
            print(f"He was going for {self.salary},and now he's going for {self.new_salary}")
        else:
            print("Come on, you're the best.")
