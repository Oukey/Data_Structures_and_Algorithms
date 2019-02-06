import Linked_list

print('Step_1. Сформированный список:')
Linked_list.s_list.print_all_nodes()  # Вывод на экран всего связанного списка

nf = Linked_list.s_list.find(11)  # создание объекта, который будет хранить результаты метода поиска класса LinkedList
if nf is not None:  # если результаты поиска не хранят None...
    print('Step_2. Результат поиска: ', nf.value)  # выведи данное(значение) узла
else:
    print('Step_2*. Результаты поиска: поиск не дал результатов.')

print('Step_3. Удаление всех узлов с найденным значением:')
Linked_list.s_list.del_ever_nod(1)
Linked_list.s_list.print_all_nodes()

print('Step_4. Удаление первого узла с найденным значением:')
Linked_list.s_list.del_nod(4)
Linked_list.s_list.print_all_nodes()

print('Step_5. Результаты поиска всех узлов по заданному значению:', Linked_list.s_list.find_all(4))

print('Step_6. Список состоит из {} узлов'.format(Linked_list.s_list.list_len()))

print('Step_7. После добавления узла список имеет следующий состав:')
Linked_list.s_list.insert_node(100, 3)
Linked_list.s_list.print_all_nodes()

print('Step_8. Результат очищения списка:')
Linked_list.s_list.clear()  # удаление всех узлов списка
Linked_list.s_list.print_all_nodes()

print('Задание № 1.7')
'''
1.7. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины
равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
'''
print('Сформированный список №1:')
Linked_list.L_1.print_all_nodes()
print('Сформированный список №2:')
Linked_list.L_2.print_all_nodes()

print('Итоговый список из сумм двух списков: ')

abc = Linked_list.comp_list(Linked_list.L_1, Linked_list.L_2)
if abs is not None:
    abc.print_all_nodes()
else:
    print('У списков №1 и №2 разная длина.')
