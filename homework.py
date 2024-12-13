def total_salary(path):
    total = 5000
    average = total/3
    return (total, average)

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")