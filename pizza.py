"""
Задание №1

Используйте ООП

Пиццерия предлагает клиентам три вида пиццы: Пепперони, Барбекю и Дары Моря,
каждая из которых определяется тестом, соусом и начинкой.

Требуется спроектировать и реализовать приложение для терминала,
позволяющее обеспечить обслуживание посетителей.

Дополнительная информация

В бизнес-процессе работы пиццерии в контексте задачи можно выделить 3 сущности (объекта):
Терминал: отвечает за взаимодействие с пользователем:
    - вывод меню на экран;
    - прием команд от пользователя (выбор пиццы, подтверждение заказа, оплата и др.);
    - Заказ: содержит список заказанных пицц, умеет подсчитывать свою стоимость;
    - Пицца: содержит заявленные характеристики пиццы,
    а также умеет себя подготовить (замесить тесто, собрать ингредиенты), испечь, порезать и упаковать.

Пиццерия реализует несколько видов пиццы, которые различаются характеристиками,
логично будет сделать общий класс Пицца,
а в дочерних классах (например, классе ПиццаБарбекю) уточнить характеристики конкретной пиццы.

Алгоритм работы пользователя с терминалом может выглядеть следующим образом:
    - Терминал отображает список меню.
    - Терминал создает новый заказ.
    - Клиент вводит номер пиццы из меню.
    - Заказ добавляет в список выбранную пиццу.
    - Действия 3-4 повторяются до подтверждения или отмены.
    - Клиент подтверждает заказ (или отменяет).
    - Терминал выставляет счет, отображая информацию о заказе.
    - Терминал принимает оплату.
    - Заказ отдается на выполнение.
"""


class Pizza:
    def __init__(self, dough, sauce, toppings):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    @staticmethod
    def cooking():
        print("Замешиваем тесто...")
        print("Добавляем соус...")
        print("Добавляем начинку...")
        print("Пекем в печи...")
        print("Режем на кусочки...")
        print("Упаковываем в коробку...")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("тонкое", "томатный", ["пепперони", "сыр"])


class BBQPizza(Pizza):
    def __init__(self):
        super().__init__("толстое", "барбекю", ["курица", "бекон", "сыр"])


class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__("тонкое", "сливочный", ["креветки", "мидии", "сыр"])


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza):
        self.pizzas.remove(pizza)

    def calculate_total(self):
        total = 0
        for _ in self.pizzas:
            total += 10
        return total


class Terminal:
    def __init__(self):
        self.order = Order()

    @staticmethod
    def display_menu():
        print("Меню:")
        print("1. Пепперони")
        print("2. Барбекю")
        print("3. Дары Моря")

    def take_order(self):
        while True:
            self.display_menu()
            choice = input("Введите номер пиццы: ")
            if choice == "1":
                pizza = PepperoniPizza()
            elif choice == "2":
                pizza = BBQPizza()
            elif choice == "3":
                pizza = SeafoodPizza()
            else:
                print("Неверный выбор")
                continue
            self.order.add_pizza(pizza)
            confirm = input("Добавить еще пиццу? (да/нет) ")
            if confirm.lower() != "да":
                break

    def display_order(self):
        print("Ваш заказ:")
        for pizza in self.order.pizzas:
            print("- Пицца", type(pizza).__name__)
        total = self.order.calculate_total()
        print("Итого:", total)

    def take_payment(self):
        total = self.order.calculate_total()
        print("Сумма заказа:", total)
        while True:
            payment = float(input("Введите сумму оплаты: "))
            if payment >= total:
                change = payment - total
                print("Сдача:", change)
                break
            else:
                print("Недостаточно средств")

    def complete_order(self):
        print("Ваш заказ готовится...")
        for pizza in self.order.pizzas:
            pizza.coocking()
        print("Ваш заказ готов")

    def run(self):
        print("Добро пожаловать в пиццерию!")
        self.take_order()
        self.display_order()
        self.take_payment()
        self.complete_order()


tm = Terminal()
tm.run()
