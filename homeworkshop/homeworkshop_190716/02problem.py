# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# k = 0
# n = 0
# for i in basket_items.keys():
#     if i in fruits:
#         k+=basket_items.values()
#     else:
#         n+=basket_items.values()
# print(f'과일은 {k}개이고, {n}개는 과일이 아닙니다.')

phone_number = input()
k = ''
for i in range(0, 8):
    phone_number[i] = '*'
#    k = phone_number.replace(i, "*")
print(k)