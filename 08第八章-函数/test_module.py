def build_profile(first, last, **user_info):
    """创建一个空字典（**userinfo），其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def car_info(manufacturers, model, **other_info):
    other_info['manufacturer'] = manufacturers
    other_info['model_number'] = model
    return other_info


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其转移到列表completed_models中
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"\nPrinting model: {current_designs}")
        completed_models.append(current_designs)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models hava been printed:")
    for completed_model in completed_models:
        print(completed_model)
