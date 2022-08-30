# Задание 5. На закрепление навыков работы со стеком
# Реализуйте собственный класс-структуру "стопка тарелок".
# Мы можем складывать тарелки в стопку и при превышении некоторого значения
# нужно начать складывать тарелки в новую стопку.
# Структура должна предусматривать наличие нескольких стопок.
# Создание новой стопки происходит при достижении предыдущим
# стеком порогового значения.
# После реализации структуры, проверьте ее работу на различных сценариях.
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# --реализуйте по аналогии с примером, рассмотренным на уроке
# --создание нового стопки можно реализовать добавлением нового пустого массива
# в массив стопок (lst = [[], [], [], [],....]).

class Stack():

    def __init__(self, max_count):
        self.elems = []
        self.max_count = max_count

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def put(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_count:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def take_out(self):
        out = self.elems[len(self.elems) - 1].pop
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()

    def get_item(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        plates_sum = 0
        for stack in self.elems:
            plates_sum += len(stack)

    def stack_count(self):
        return len(self.elems)


plates = Stack(4)
print(type(plates))
plates.put('Plate_1')
plates.put('Plate_2')
plates.put('Plate_3')
plates.put('Plate_4')

print(plates)
print(plates.take_out())
print(plates.get_item())
print(plates.stack_size())
print(plates.stack_count())
print(plates)
