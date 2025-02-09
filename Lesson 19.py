
import function
from function import bubble_sort

subject = [["Математика", "Алгебра", 7],
           ["Фізика", "Механіка", 9],
           ["Математика", "Геометрія", 5],
           ["Хімія", "Органічна хімія", 10],
           ["Фізика", "Астрономія", 12]]

def print_subject(subject):
    width_pib = 0
    for st in subject:
        if len(st[1]) > width_pib:
            width_pib = len(st[1])
    width_pib += 3
    for st in subject:
        for i in range(0, len(st)):
            print(str(st[i]).ljust(width_pib), end=' | ')
        print()
print_subject(subject)


bubble_sort(subject, lambda a, b: a[2] < b[2])
print()
print_subject(subject)


