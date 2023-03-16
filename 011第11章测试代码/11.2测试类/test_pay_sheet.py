import unittest
import pay_sheet


class TestPaySheet(unittest.TestCase):
    """测试pay_sheet模块"""
    def setUp(self):
        self.num = 10000
        self.my_sheet = pay_sheet.Employee('T', 'om', self.num)

    def test_give_default_raise(self):
        """测试在默认情况下加薪多少"""
        self.num += 5000
        money = self.my_sheet.give_raise()
        self.assertEqual(money, self.num)

    def test_give_custom_raise(self):
        """测试指定加薪金额后加薪多少"""
        custom_num = 8000
        money = self.my_sheet.give_raise(custom_num)
        self.assertEqual(money, self.num + custom_num)
        self.my_sheet.get_full_info()