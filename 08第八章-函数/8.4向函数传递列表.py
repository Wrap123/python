def greet_users(names):
    """向列表中的每一个用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['john', 'mari', 'tom']
greet_users(usernames)

# 在函数中修改列表


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其转移到列表completed_models中
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"\nPrinting model: {current_designs}")
        completed_models.append(current_designs)
    print(un_print_designs)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models hava been printed:")
    for completed_model in completed_models:
        print(completed_model)
    # print(un_print_designs)


# 调用函数
un_print_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []
print_models(un_print_designs[:], complete_models)
show_completed_models(complete_models)

# 为了避免函数修改列表，可以使用function_name(list_name[:])的方式来使用列表的副本完成传递列表给函数的操作

# 动手试一试
# 练习8-9 消息


def show_messages(messages):
    """打印消息内容"""
    for message in messages:
        print(f"The message is {message}")


mess = ['I', 'love', 'you']
show_messages(mess)

# 练习8-10 发送消息


def send_messages(wait_messages, sent_messages):
    """将发送过的消息放在一个新列表内"""
    # wait_messages_2 = wait_messages[:]
    while wait_messages:
        complete_message = wait_messages.pop()
        print(f"\nCompleted message: {complete_message}")
        sent_messages.append(complete_message)
        sent_messages.reverse()
    print(f"wait_message: {wait_message}")
    print(f"wait_messages: {wait_messages}")
    print(f"sent_messages: {sent_messages}")


wait_message = ['I', 'love', 'you']
sent_messages = []
send_messages(wait_message[:], sent_messages)

# 练习8-11 消息归档
# 在上一个函数中修改
