# unittest模块
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试 name_function"""
    def test_first_last_name(self):
        """能够正确的处理像 Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像 Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# 被测试框架调用时，__name__不等于__main__，所以这里是不等于，会执行unittest的测试语句
# unittest的main的函数是开始测试
if __name__ == '__main__':
    unittest.main()

"""
拓展拓展：
__name__是python内置的系统定义的名字
两种使用方式：
    1、直接在命令行print(__name__)时，那么输出为__main__，因为在python内部__name__ = __main__
    2、被测试框架unittest调用时，__name__就是当前文件的名字（名字不包含后缀.py）
"""

