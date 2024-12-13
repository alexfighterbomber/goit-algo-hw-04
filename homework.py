def total_salary(path) -> tuple:
    total = 0
    count = 0
    try:
        with open(path, 'r',encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines() if el.strip()]
    except FileNotFoundError:
        return (0,0)
    except IOError:
        return (0,0)

    for line in lines:
        developer = line.split(',')
        if len(developer) == 2:
            total += int(developer[1])
            count += 1
    
    average = total/count
    return (total, average)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")