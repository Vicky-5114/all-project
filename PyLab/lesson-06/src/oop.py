class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        if age <= 0:
            self.__age = "年龄必须大于0"  # 私有属性
        else:
            self.__age = age  # 私有属性

    # 利用非私有方法访问私有属性
    def show_info(self):
        print(f"姓名:{self.__name}\n年龄:{self.__age}")

    # 私有方法
    def __sleep(self):
        print("我要睡觉了, 晚安!")

    # 利用非私有方法调用私有方法
    def sleep(self):
        self.__sleep()


# # 私有属性或私有方法只能在该类的内部调用
# ps = Person("赵六", 26)
# ps.show_info()
# ps.sleep()

# # 不能在类的外部直接调用
# print(ps.__name)
# print(ps.__age)
# ps.__sleep()


class Person:
    __school = "调用__school成功"  # 私有属性
    school = "调用school成功"  # 非私有属性

    def __sleep(self):  # 私有方法
        print("调用__sleep成功")

    def sleep(self):  # 非私有方法
        print("调用sleep成功")


class Student(Person):
    pass


# stu = Student()
# print(Student.school)
# stu.sleep()  # 非私有方法在类的外部间接调用私有方法
# # 就算是继承关系，子类也无法直接访问父类的私有属性和私有方法
# print(Student.__school)
# stu.__sleep()


class A:
    def __func(self):
        print("private")

    def _func(self):
        print("protected")

    def call_func(self):
        self.__func()


class B(A):
    def foo(self):
        self.__func()
        self._func()


# b = B()
# # 子类调用父类的非私有方法, 间接调用父类的私有方法
# b.call_func()
# b.foo()


class A:
    def __init__(self, name):
        self.name = name
        self.Q()

    def E(self):
        print("E方法被调用")

    def Q(self):
        print(self.name, "Q方法被调用")


class B(A):
    pass


b = B(
    "张三"
)  # 实例化,调用初始化方法,B没有则调用父类中的初始 化方法,初始化方法中调用了Q方法
b.E()  # 调用父类的E方法
b.Q()  # 调用父类的Q方法


class C(A):
    def __init__(self, name):
        self.names = name


c = C("赵六")  # 实例化, 优先调用C中初始化方法
""" 虽然可以调用父类的Q方法, 但是因为Q方法中的self.name没有定
义, 因为A的初始化方法没有被调用, 所以报错
解决方案: 先通过c调用一次A的初始化方法 或者 把C类中的self.names
改为self.name """
# c.Q() # 报错


class D(A):
    def __init__(self, name):
        super(D, self).__init__("李四")
        self.name = name


# 实例化, 先调用D的初始化方法, super方法调用父 类的初始化方法, 父类的初始化方法中调用Q方法
d = D("王五")
d.Q()  # 调用父类的Q方
