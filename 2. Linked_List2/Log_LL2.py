import Linked_List2

# Логи

print('Step_1. Создание и вывод на экран пустого списка:', )
d_list = Linked_List2.LinkedList2()
print(d_list.print_first())

print('Step_2. Заполнение и вывод на экран значений узлов списка.')
d_list.add_in_tail(Linked_List2.n1)
d_list.add_in_tail(Linked_List2.n2)
d_list.add_in_tail(Linked_List2.Node2(1))
d_list.add_in_tail(Linked_List2.Node2(2))
d_list.add_in_tail(Linked_List2.Node2(3))
d_list.add_in_tail(Linked_List2.Node2(4))
d_list.add_in_tail(Linked_List2.Node2(5))
print('От начало и до конца: ', d_list.print_first())
print('В обратном направлении: ', d_list.print_end())

print('Step_3. Поиск заданного элемента.')
n = int(input('Введите целое число для поиска: '))
if d_list.find_first(n) is not None:
    print('В списке найденно заданное число:', d_list.find_first(n).value)
else:
    print('Заданного значения', n, 'в списке не найдено')

print('Step_4. Метод удаления одного узла по его значению.')
d = int(input('Введите целое число для удаления из списка: '))
d_list.del_first(d)
print('Результат удаления: ', d_list.print_first())
print('Результат удаления в обратном направлении: ', d_list.print_end())

print('Step_5. Метод добавления в список после заданного узла.')
node = d_list.get_node(int(input('Введите целое число для поиска узла по значению: ')))
new_node = Linked_List2.Node2(input('Введите любые данные для создания нового списка: '))
d_list.insert_next(node, new_node)
print('Результат добавления: ', d_list.print_first())
print('Результат добавления в обратном направлении: ', d_list.print_end())

print('Step_6. Метод добавления самого первого узла.')
fn = int(input('Введите значение для добавление в начало списка: '))
d_list.insert_first(fn)
print('Результат добавления: ', d_list.print_first())
print('Результат добавления в обратном направлении: ', d_list.print_end())
