class myclass:
    @staticmethod
    def static_method():
        print("this is static method")

    @classmethod
    def class_method(cls):
        print("this is a class method")

    @property
    def name(self):
        return "myclass"


obj = myclass
obj.static_method()
obj.class_method()
print(obj.name)
