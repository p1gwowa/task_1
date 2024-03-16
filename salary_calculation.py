def total_salary(path) -> tuple:
    try:
        with open("salary.txt", 'r') as file:
            text = file.readlines()
            worker_salary = [el.strip() for el in text]
            name_salary = [el.split(',') for el in worker_salary]
            return name_salary
            # print(name_salary)
            # print(type(name_salary))
    except FileNotFoundError:
        return print('File not found')

print(total_salary("path/to/salary.txt"))

