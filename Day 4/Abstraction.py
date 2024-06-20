from abc import ABC,abstractmethod

#Abstract parent class
class Sample (ABC) :
    @abstractmethod
    def hello(self) : pass

#implementation child class
class Implement (Sample) :
    #implementing abstract method
    def hello(self):
        print('Hello')

#main method
def main() :
    obj = Implement()
    obj.hello()
if __name__ == "__main__" :
    main()

    
'''
***Important points to remember during dealing with abstract classes and interfaces***
1) cannot create objects for abstract classes or interfaces
2) abstract class : class with mixture of abstract and normal methods
3) interface : only has abstract methods
4) we provide methods definitions in the in child class
5) mandatory to provide definitions for all abstract methods ( doesnt matter if you use then or not)
'''