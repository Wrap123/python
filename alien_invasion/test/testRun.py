from testInfo import TestInfo
from testUse import TestUse


class TestRun:
    def __init__(self):
        self.testInfo = TestInfo()      # 主python程序里边搞了这个，引用进来的py文件里也可以写这个，有点坑，对新手不友好

        self.testuse = TestUse(self)

    def new_run(self):
        print(self.testuse.testKey)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    test = TestRun()
    test.new_run()