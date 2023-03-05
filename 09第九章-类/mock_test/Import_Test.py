# 练习9-10
import Restaurant as Rant
# 练习9-11
from User_Privileges_Admin import Admin, Privileges

# 练习9-10
restaurant = Rant.Restaurant('DeShengKe', 'SanMenXia')
restaurant.describe_restaurant()

# 练习9-11
admin_1 = Admin('Ji', 'WaWa', 0)
admin_1.privileges.show_privileges()
