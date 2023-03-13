book = []

with open('cookbook.txt', 'rt') as file:
    for l in file:
        cook_name = l.strip()
        book_ = {'name': cook_name, 'emp':[] }
        emp_count = file.readline()
        for i in range(int(emp_count)):
            emp_ = file.readline()
            ingredient_name, quantity, measure = emp_.split(' | ')
            book_['emp'].append({'ingredient_name':ingredient_name,
                                 'quantity':quantity,
                                 'measure':measure})
        black_line = file.readline()
        book.append(book_)

print(book)