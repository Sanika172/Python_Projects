class myclass:
    var = "hello"

    @classmethod
    def class_method(cls):
        print(f"class variable value {cls.var}")


myclass.class_method()
