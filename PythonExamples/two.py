'''
OK. this file is being called from another script called 1.py
It will only have three things
1 - a loop
2 -  def test():
3 - if __name__='__main__':
main()

My goal is to show what happens when you import this file from the other scrip
also, what happens when no __name_=... exist.
and finally calling an specific function from the othet file such as:
from 2 import test....

'''


def temp():
    print("\nHello from two.py")
    print("If two.py runs alone, you will not see me...")
    
    for y in range(10, 20, 1): #From 10 to 20 incrementing by 1
        print (y)
    
        
def main():
     print("__name__='__main__': was called")
     print("\nThis means that when a script is called by it self, it look for def main():")
if __name__ == '__main__':
    main()

