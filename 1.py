import json
with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
products = data['products']
for product in products:
    print(f'Название: {product["name"]}')
    print(f'Цена: {product["price"]}')
    print(f'Вес: {product["weight"]}')
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

    print()