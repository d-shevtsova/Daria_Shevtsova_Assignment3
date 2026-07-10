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
    dep_emp=list(filter(lambda x: x["department"] == target_dept, employee_list))
    # avr salary
    total = sum(map(lambda x: x["salary"], dep_emp))
    avg = round(total / len(dep_emp),2)
    # best emp
    best = max(dep_emp, key=lambda x: x["salary"])

    # 3. Функція має повертати (return) словник такого вигляду:
    return {
        "department": target_dept,
        "average_salary": avg,
        "top_earner": best["name"],
        "count": len(dep_emp)
    }

# 4. Викличте функцію для відділів "IT" та "Marketing" і виведіть результат.
print(get_department_stats(employees,"IT"))
print(get_department_stats(employees,"Marketing"))