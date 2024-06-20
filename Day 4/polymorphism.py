#parent method
class Parent :
    def func(self) :
        print('This is Parent class method')
#child class
class Child (Parent):
    def func(self) :
        print('This is child class method')
#main method
def main() :
    obj = Child()
    obj.func()
if __name__ == '__main__' :
    main()