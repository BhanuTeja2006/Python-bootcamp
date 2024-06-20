#class Student
class Student :
    def __init__ (self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def details(self) :
        print(f'Name    : { self.name }')
        print(f'Roll    : { self.roll}')
        print(f'branch  : { self.branch}')

#main method
def main() :
    obj=Student('Abhinav','23951A0503','CSE')
    obj.details()
    
#calling the main method
if __name__ == '__main__' :
    main()