"""
Version: 0.1
Author: LC
DateTime:2018年11月15日15:22:27
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
class Student(object):

    def __init__(self, id, name, age, sex):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def watch_av(self):
        if self.age >= 18:
            print(f'{self.name}正在观看岛国片.')
        else:
            print(f'{self.name}只能看《熊出没》.')


def main():
    dict1 = {
        'id': 1001,
        'name': '王大锤',
        'age': 18,
        'sex': True
    }
    stu = Student(**dict1)
    stu.study('Python程序设计')
    stu.watch_av()


if __name__ == '__main__':
    main()
