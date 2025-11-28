class myClass:
    __privateVar=27;
    def __privMeth(self):
        print("I'm inside this class myClass")
    def hello(self):
        print("Private Variable's value:",myClass.__privateVar)
foo=myClass()
foo.hello()
foo.__privMeth