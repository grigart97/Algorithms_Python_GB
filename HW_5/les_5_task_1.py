# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


def years_mean(arr):
    return sum(arr) / len(arr)


incomes = ['name', 'q1', 'q2', 'q3', 'q4', 'm_income']
new_company = namedtuple('new_company', incomes, defaults=[0, ])
companies_quantity = int(input('Введите количество компаний: '))
s = []
for i in range(companies_quantity):
    stats = [input(f'Название {i + 1}-ой компании: ')] + \
            (lst := [int(input(f'Введите прибыль за {j + 1}-ый квартал: ')) for j in range(4)]) + [years_mean(lst)]
    s.append(new_company._make(stats))
# print(s)
mean_income = sum([comp.m_income for comp in s]) / companies_quantity
print(f'Средняя прибыль компаний - {mean_income}')
for comp in s:
    print(f'Прибыль компании "{comp.name}" ниже среднего' if comp.m_income < mean_income else f'Прибыль компании "{comp.name}" выше среднего')
