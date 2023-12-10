class Student:
    minimum = 50

    def __init__(self, name, lastname, age, utorid, gpa):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.utorid = utorid
        self.gpa = gpa

    def fullname(self):
        return self.name + self.lastname

    def passing(self):
        return self.gpa > self.minimum

    def __str__(self):
        return Student.fullname(self), self.age, self.utorid, self.gpa


class FirstYear(Student):
    minimum = 60

    def __init__(self, name, lastname, age, utorid, gpa, course):
        super().__init__(name, lastname, age, utorid, gpa)
        self.course = course


class Prof(Student):

    def __init__(self, name, lastname, age, utorid, students=None):
        super().__init__(name, lastname, age, utorid, gpa=100)
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, new_student):
        new_student.self = new_student
        if new_student not in self.students:
            self.students.append(new_student)

    def remove_student(self, new_student):
        new_student.self = new_student
        if new_student in self.students:
            self.students.remove(new_student)

    def print_students(self):
        for student in self.students:
            student.fullname()


orange = Student("Apple", "Banana", 18, 111111111, 95)

Apple = FirstYear("A", "P", 18, 222222, 55, "CSC108")

Doc = Prof("D", "K", 40, 7777777, [Apple, orange])
Cod = Prof("D", "K", 40, 7777777)


print(Apple.passing())

print(orange.passing())

print(Doc.gpa)

print(Doc.__str__())

print(orange.__str__())

Doc.print_students()

print(Cod.gpa)
print(Cod.students)


def puzzle(thing):
    for i in range(len(thing)):
        if thing[i - 1] < thing[i]:
            return i - 1
    return -1

x = puzzle([3, 2, 1])
print(x)
class Product:
    def __init__(self, name: str, price: float, weight: int) -> None:
        """Initialize a new product with product name, price in dollars, and
        weight in grams.
        >>> prod = Product('Science Umbrella', 23.97, 408)
        >>> prod.product_name
        'Science Umbrella'
        >>> prod.price
        23.97
        >>> prod.weight
        408
        """
        self.product_name = name
        self.price = price
        self.weight = weight


    def __str__(self) -> str:
        """Return a string representation of this product.
        >>> prod = Product('Science Umbrella', 23.97, 408)
        >>> str(prod)
        'Science Umbrella ($23.97)'
        """
        return str(self.product_name) + " ($" + str(self.price) + ")"


prod = Product('Science Umbrella', 23.97, 408)
print(str(prod))

class ShoppingCart:
    def __init__(self, name: str) -> None:
        """Initialize a new shopping cart that is named name with an empty list
        of products.
        >>> cart = ShoppingCart('School Supplies')
        >>> cart.name
        'School Supplies'
        >>> cart.products
        []
        """
        self.name = name
        self.products = []

    def add_product(self, product: "Product") -> None:
        """Adds the product to the list of products in the ShoppingCart.
        >>> cart = ShoppingCart('School Supplies')
        >>> cart.products
        []
        >>> cart.add_product(Product('Science Umbrella', 23.97, 408))
        >>> len(cart.products)
        1
        """
        self.products.append(product)


    def shipping_cost(self) -> float:
        """Return the cost of shipping the products in the ShoppingCart. Shipping
        is free ($0) if total price of products in ShoppingCart is above $50,
        otherwise the cost depends on total product weight as follows:
        * under 100g : $ 5.50
        * over 100g, under 500g : $15.00
        * over 500g : $25.00
        >>> cart = ShoppingCart('School Supplies')
        >>> cart.add_product(Product('Pencil', 3.95, 65))
        >>> cart.shipping_cost()
        5.5
        >>> cart.add_product(Product('Science Umbrella', 23.97, 408))
        >>> cart.shipping_cost()
        15.0
        >>> cart.add_product(Product('Computer Science Umbrella', 24.97, 408))
        >>> cart.shipping_cost()
        0.0
        """
        sum = 0
        wsum = 0
        for prod in self.products:
            sum += prod.price

        for prod in self.products:
            wsum += prod.weight

        if sum > 50:
            return 0.0
        if wsum > 500:
            return 25.0
        if wsum > 100:
            return 15.0
        return 5.5



cart = ShoppingCart('School Supplies')
print(cart.products)
cart.add_product(Product('Science Umbrella', 23.97, 408))
print(len(cart.products))
cart = ShoppingCart('School Supplies')
cart.add_product(Product('Pencil', 3.95, 65))
print(cart.shipping_cost())
