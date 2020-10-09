'''
class Student(object):
    """
    创建类
    """
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!!!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0-100!!!')
        self._score = value
stu = Student()
stu.set_score(90)
score = stu.get_score()
print(score)
'''
class Student(object):
    """
    创建类
    """
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!!!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0-100!!!')
        self._score = value
class Teacher(Student):
    """
    创建类
    """
    @property
    def name(self):
        return 'Marvin'
stu = Student()
stu.score = 80
score = stu.score
Tea = Teacher()
Tea.score = 100
print(Tea.score)
print(Tea.name)
print(score)
print()