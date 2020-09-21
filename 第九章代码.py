class Person(object):
    #限定Person对象只能绑定'_name', '_age', '_gender'三个属性
    __slots__ = ('_name', '_age', '_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age
    #getter访问器
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    #setter修改器
    def set_age(self, age):
        self._age =  age
    def set_name(self, name):
        self._name = name
    def paly(self):
        if self._age <= 16:
            print(self._name + "palying planechet")
        else:
            print(self._name + "palying computer")
    name = property(get_name, set_name)
    age = property(get_age, set_age)
def main():
    person = Person("Marvin", 22)
    person.paly()
    person.age = 21
    person.paly()
    person._gender = 'man'
    print(person._gender)
    #person._is_gay = True
if __name__ == '__main__':
    main()
