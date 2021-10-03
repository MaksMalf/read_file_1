from pprint import pprint


def get_data(file_name, encoding):
    cook_book = {}
    with open(file_name, encoding=encoding) as file:

        for line in file:
            name_recipe = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                name, total, unit = file.readline().split('|')
                temp_list.append({'ingredient_name': name, 'quantity': total, 'measure': unit})
            cook_book[name_recipe] = temp_list

            file.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, encoding):
    food_basket = {}
    temp_food_basket = {}

    for list in get_data('file_1.txt', 'utf-8').values():
        for dict in list:
            temp_food_basket_2 = {}
            temp_food_basket_2['measure'] = dict['measure']
            temp_food_basket_2['quantity'] = int(dict['quantity']) * person_count
            if dict['ingredient_name'] in food_basket.keys():
                temp_food_basket_2['quantity'] = int(temp_food_basket_2['quantity']) * 2
            food_basket[dict['ingredient_name']] = temp_food_basket_2

    return food_basket


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Запеченный картофель'], 6, 'utf-8'))


# pprint(get_data('file_1.txt', 'utf-8'))
