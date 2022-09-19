# Задание 2.
# Доработайте пример структуры "дерево", рассмотренный на уроке.
# Предложите варианты доработки и оптимизации (например, валидация значений узлов в соответствии
#  с требованиями для бинарного дерева). При валидации приветствуется генерация собственного исключения
# Поработайте с оптимизированной структурой, протестируйте на реальных данных - на клиентском коде

class MyException(Exception):
    pass

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node < self.root:
                # если у узла нет левого потомка
                if self.left_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise MyException("wrong value")
        except MyException:
            print(f'invalid value ({new_node}) entered!')

        # добавить правого потомка

    def insert_right(self, new_node):
        try:
            if new_node > self.root:
                # если у узла нет левого потомка
                if self.right_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise MyException("value is error")
        except MyException:
            print(f'invalid value ({new_node}) entered!')

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # def search_recursiv(v, x):
    #     if v is None or v.root_obj == x:
    #         return v
    #     elif x < v.root_obj:
    #         return x.search_recursiv(v.left, x)
    #     else:  # x > v.key
    #         return x.search_recursiv(v.right, x)

    # def search(x):
    #     v = self
    #     while v is not None:
    #         if v.key == x:
    #             return v
    #         elif x < v.key:
    #             v = v.left
    #         else:  # x > v.key:
    #             v = v.right
    #     return None

r = BinaryTree(8)
print(r.get_root_val())
r.insert_left(5)
r.insert_right(11)
print(r.get_left_child().get_root_val())
print(r.get_right_child().get_root_val())
r.insert_left(9)
r.insert_left(10)
print(r.get_left_child().get_root_val())
r.insert_right(19)
print(r.get_right_child().get_root_val())
r.insert_right(6)
