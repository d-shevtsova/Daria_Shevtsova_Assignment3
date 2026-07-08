# Завдання 2
# Ви працюєте з даними про банківський вклад. Вам потрібно оновити баланс
# після нарахування відсотків та змінити статус вкладу.
deposit_account = {
"client_id": "C1025",
"balance": 5000.0,
"currency": "UAH",
"interest_rate": 0.08, # 8% річних
"is_active": True
}
# 1. Обчисліть суму нарахованих відсотків за рік (сума = баланс *
# відсоткова_ставка).
sum = deposit_account["balance"] * deposit_account["interest_rate"]
print(sum)

# 2. Оновіть значення ключа "balance", додавши до нього нараховані
# відсотки.
deposit_account["balance"] +=sum
print(deposit_account["balance"])

# 3. Додайте до словника новий ключ "last_update_type" зі значенням
# "interest accrual".


# 4. Змініть значення ключа "is_active" на False, ніби клієнт закрив рахунок.


# 5. Виведіть на екран фінальний оновлений словник.

