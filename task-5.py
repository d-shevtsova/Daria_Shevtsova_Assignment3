# Завдання 5
# У вас є "плаский" список даних про продажі товарів в інтернет-магазині. Кожен
# елемент — це один проданий товар. Вам потрібно перетворити ці дані на
# згрупований звіт, щоб проаналізувати ефективність продажів по кожній
# категорії товарів.
sales_data = [
{"product": "Смартфон", "category": "Електроніка",
"quantity": 1, "price": 15000},
{"product": "Книга 'Python для всіх'", "category":
"Книги", "quantity": 2, "price": 700},
{"product": "Навушники", "category": "Електроніка",
"quantity": 2, "price": 2500},
{"product": "Чайник", "category": "Побутова техніка",
"quantity": 1, "price": 1200},
{"product": "Книга 'Алгоритми'", "category": "Книги",
"quantity": 1, "price": 900},
{"product": "Ноутбук", "category": "Електроніка",
"quantity": 1, "price": 32000}
]
# 1. Створіть новий порожній словник під назвою category_report.
category_report = {}

# 2. Напишіть цикл, що проходить по списку sales_data. Для кожного
# продажу:
for item in sales_data:
    category = item["category"]

    if category not in category_report:
        category_report[category] = {
            "total_rev": 0,
            "total_sold":0
        }
    # ○ Оновіть дані для цієї категорії:
    # ■ Збільште загальний дохід (total_revenue) на вартість цієї транзакції (quantity * price).
    # ■ Збільште загальну кількість проданих одиниць
    # (total_items_sold) на кількість товарів у цій транзакції (quantity).
    category_report[category]["total_rev"] += item["quantity"]*item["price"]
    category_report[category]["total_sold"] += item["quantity"]



# 3. Виведіть фінальний словник category_report у зручному для читання форматі.
# Очікуваний результат (структура та значення):
# {
# 'Електроніка': {
# 'total_revenue': 52000,
# 'total_items_sold': 4
# },
# 'Книги': {
# 'total_revenue': 2300,
# 'total_items_sold': 3
# },
# 'Побутова техніка': {
# 'total_revenue': 1200,
# 'total_items_sold': 1
# }
# }


