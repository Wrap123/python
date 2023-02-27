"""
这篇全是理论概念，慢慢看
模块概念：
函数可以保存在一个.py的文件内，这种叫做一个模块，文件名也可以叫做模块名
然后在同级目录下的.py文件中通过“import 模块名”的格式来调用，相当于把模块的代码复制到这个文件里来了，但是你看不到
    调用格式（句点表示法）：module_name.function_name()
"""
# 这里创建一个test_module的模块来测试（即test_module.py文件）
import test_module
# 或者导入指定模块下的指定函数，但是注意使用这种方式时，
#       导入格式为：from module_name import function_0, function_1,...
#       调用格式为：function_name(),把模块名省略了
from test_module import car_info, build_profile

car = test_module.car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8.6.3/4 可以用as给导入的模块或者函数指定别名，就和Linux中的alias命令一样
# 比如
import test_module as t_m
my_info = t_m.build_profile('Bao', 'Yao', age='18', money='none')
print(f"\nmy_info")

# !! 要注意的是，import语句一般要放在所在文件的最上面，这里放中间只是为了演示和学习练习!!

# 8.6.5 导入模块所有的函数
# 使用下边这种方式导入模块函数时，调用时因为是直接导入的函数，所以不用以句点表示法来使用。
# 但是这种最好是自己写的模块，不然如果和当前项目内的函数名相同，那就完犊子了
# 一般来说，要么只导入需要使用的函数，要么导入整个模块，用句点表示法来使用
from test_module import *
car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8.7 动手试一试
import test_module
un_print_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []
test_module.print_models(un_print_designs[:], complete_models)
test_module.show_completed_models(complete_models)

# 自己随便练习一下


def aa(test, test2):
    print(test)
    # for te in test:
    while test:
        ttt = test.pop()
        test2.append(ttt)
        print(test2)
    for t in test2:
        print(t)


bbb = ['1', '2']
ccc = []
aa(bbb, ccc)
