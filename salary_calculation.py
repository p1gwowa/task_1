def total_salary(path) -> tuple:
    try:
        with open("salary_file.txt", 'r') as file:
            text = file.readlines()
            worker_salary = [el.strip() for el in text]
            name_salary = [el.split(',') for el in worker_salary]
            name_salary_list = [el for element in name_salary for el in element]
            salary_number_list = []
            for el in name_salary_list:
                try:
                    salary_number = int(el)
                    salary_number_list.append(salary_number)
                except ValueError:
                    pass
            total = sum(salary_number_list)
            average_salary = total//len(salary_number_list)
        return print(f'Total sum of salary: {total}\nAverage salary: {average_salary}')
    except FileNotFoundError:
        return print('File not found')

total_salary("path/to/salary.txt")