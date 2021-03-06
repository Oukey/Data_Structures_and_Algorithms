# Примеры структур данных

## Оглавление


- [1. Связанный список](#Связанный-список)
- [2. Двунаправленный связанный список](#Двунаправленный-связанный-список)
- [3. Динамический массив](#Динамический-массив)
- [4. Стек](#Стек)
- [5. Очередь](#Очередь)
- [6. Упорядоченный список](#Упорядоченный-список)
- [7. Хэширование](#Хэширование)
- [8. Ассоциативный массив](#Ассоциативный-массив )
- [9. Фильтр Блума](#Фильтр-Блума)
- [10. Множества](#Множества)
- [11. Кэш](#Кэш)
- [12. Деревья](#Деревья)
- [13. Пирамида-куча](#Пирамида-куча)
- [14. Графы](#Графы)


### Связанный список 
- цепочка узлов, узел хранит информацию и ссылку на следующий узел
- временная сложность:
    индексация	O(n)
    поиск	O(n)
    вставка	O(1)
    удаление	O(1)


### Двунаправленный связанный список 
- цепочка узлов, узел хранит информацию и ссылки на следующий и предыдущие узлы
- временная сложность:
    индексация	O(n)
    поиск	O(n)
    вставка	O(1)
    удаление	O(1)


### Динамический массив 
- индексируется
- позволяет добавлять элементы в позиции по индексу 
- автоматически расширяется при добавлении новых элементов и сжимается при удалении
- временная сложность:
    индексация	O(1)
    поиск	O(n)
    вставка	O(n)
    удаление	O(n)


### Стек
- это простой тип данных 
- представляет собой линейное хранилище элементов 
- из стека есть только один выход, он же вход
- работает по принципу "последний вошёл - первый вышел"
- поддерживает две операции: push (втолкнуть) и pop (вытолкнуть) 


### Очередь
- это простой тип данных
- отличается от стека наличием входа и выхода
- работает по принципу "первый вошёл - первый вышел"
- функционал может расширяться, например до двухсторонней очереди


### Упорядоченный список
- доработанный двухсторонний связанный список
- хранит данные в упорядоченном виде
- позиция каждого элемента в списке определяется автоматически по значению относительно других элементов


### Хэширование
- пример схемы универсального хэширования


### Ассоциативный массив
- пример расширения хэш-таблиц до концепции словаря


### Фильтр Блума
- Один из подходов, который может повысить эффективность работы хэш-системы
- ФБ выдает вероятностный результат присутствия элемента в множестве, допускаются ложноположительные срабатывания
- Пример применения - Google BigTable использует фильтры Блума для уменьшения числа обращений к жесткому диску при проверке на существование заданной строки или столбца в таблице базы данных


### Множества
- Пример расширения хэш-таблиц до концепции множества


### Кэш
- Кэш - своеобразная хэш-таблица, промежуточный буфер с быстрым доступом


