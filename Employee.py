class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
#del emp1.age  # 删除 'age' 属性

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'

 
print "Employee.__doc__:", Employee.__doc__   #  类的文档字符串
print "Employee.__name__:", Employee.__name__   #   类名
#类定义所在的模块（类的全名是'__main__.className'，
#如果类位于一个导入模块mymod中，
#那么className.__module__ 等于 mymod）
print "Employee.__module__:", Employee.__module__
 #  类的所有父类构成元素（包含了以个由所有父类组成的元组）
print "Employee.__bases__:", Employee.__bases__
 #__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
print "Employee.__dict__:", Employee.__dict__   
