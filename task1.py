with open('./files/recepts_of_dishes.txt', encoding="utf-8") as file:
    cook_book = {}
    tmp = []
    for txt in file.read().split('\n\n'):
        name= txt.split('\n')
        tmp.append(name)
    for i in tmp:
        ingridient=[]
        for v in i[2:]:
            v=v.split(" | ")
            result={
            'ingredient_name': v[0],
            'quantity': v[1],
            'measure': v[2]
            }
            ingridient.append(result)
        cook_book[i[0]]=ingridient
# print(cook_book)
# Функция для 2-й таски
def get_shop_list_by_dishes(a, b):
    b=int(b)
    result_list={}
    for index in a:
        for i in cook_book[index]:
            for v in i:
                result_task2={
                    'measure' : i['measure'],
                    'quantity' : int(i['quantity'])*b
                }
            result_list[i['ingredient_name']]=result_task2
    return result_list    
# print(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 4))