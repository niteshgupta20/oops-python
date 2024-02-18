from item import Item
from phone import Phone

# phone1 = Phone("blackberry1", 100, 8, 1)
Item.instantiate_from_csv()
# phone1.broken_phone = 1
# print(phone1.calculate_total_price())
# phone1 = Phone("blackberry2", 76, 20)
# phone1.broken_phone = 1
print(Item.all)
# print(Phone.all)


"""

# Item.instantiate_from_csv()
#
# print(Item.all)
print(Item.is_integer("11"))


item1 = Item("Phone", 100, 4)
# item1.apply_discount()
# print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
item2.has_numpad = False
item3 = Item("Mouse", 200, 9)

# for item in Item.all:
#     print(item.name)
print(Item.all)
"""


"""
print(Item.pay_rate)
print(Item.__dict__)
print(item1.__dict__)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
"""


