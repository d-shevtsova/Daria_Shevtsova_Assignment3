# Завдання 4

employees = [
{"name": "Олена", "department": "Marketing", "salary":
25000},
{"name": "Ігор", "department": "IT", "salary": 55000},
{"name": "Наталія", "department": "Marketing", "salary":
28000},
{"name": "Олег", "department": "HR", "salary": 22000},
{"name": "Андрій", "department": "IT", "salary": 48000},
{"name": "Марія", "department": "IT", "salary": 52000},
]

def get_department_stats(employee_list, target_dept):
    # основний код:
    # фильтр
    # avr salary
    # best emp


    # 3. Функція має повертати (return) словник такого вигляду:
    return {
        "department": target_dept,
        "average_salary": avr_salary,
        "top_earner": best,
        # "count": |??
    }

# 4. Викличте функцію для відділів "IT" та "Marketing" і виведіть результат.
print(get_department_stats(employees,"IT"))
print(get_department_stats(employees,"Marketing"))