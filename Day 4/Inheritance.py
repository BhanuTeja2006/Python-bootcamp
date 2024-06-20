#single inheritance demonstration
class Parent :
    def classParentMethod(self) :
        print('Method from parent')
class Child (Parent):
    def classChildMethod (self) :
        print('Method from child')
objsingle = Child()
objsingle.classParentMethod()
objsingle.classChildMethod()
#multiple inheritance demonstration
class parent1 :
    def parent1method(self) :
        print('method from parent 1')
class parent2 :
    def parent2method(self) :
        print('method from parent 2')
class child(parent1,parent2) :
    def childmethod(self) :
        print('method from child class')
objmultiple = child()
objmultiple.parent1method()
objmultiple.parent2method()
objmultiple.childmethod()