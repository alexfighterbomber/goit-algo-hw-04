
def total_salary(path: str) -> tuple:
    total = 0
    count = 0
    try:
        with open(path, 'r',encoding='utf-8') as fh:    # відкриття файлу для читання
            lines = [el.strip() for el in fh.readlines() if el.strip()] # отримання списку рядків з очищенням від пробільних символів та пустих рядків
    except FileNotFoundError:
        return (None,None)
    except IOError:
        return (None,None)
    
    for line in lines:
        developer = line.split(',')     # розділення на елементи
        if len(developer) == 2 and developer[1].strip().isdigit():  # перевірка на коректність даних
            total += float(developer[1])        # підрахунок total
            count += 1
    average = total/count    # підрахунок average
    return (total, average)


def get_cats_info(path):
    try:
        with open(path, 'r',encoding='utf-8') as fh:    # відкриття файлу для читання
            lines = [el.strip() for el in fh.readlines() if el.strip()] # отримання списку рядків з очищенням від пробільних символів та пустих рядків
    except FileNotFoundError:
        return [None]
    except IOError:
        return [None]
    
    cats = list()
    for line in lines:
        cat = line.split(',')    # розділення на елементи
        if len(cat)==3: cats.append({"id":cat[0], "name":cat[1], "age":cat[2]}) # створення словників та заповнення списку 
    return cats


print('Task_1')
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
print('Task_2')
cats_info = get_cats_info("cats_file.txt")
print(cats_info)