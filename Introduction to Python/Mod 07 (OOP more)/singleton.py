# singleton: one single instance of a class
# If you want a new instance, you will get the old (already created) instance

class Singleton:
    __instance = None

    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('Only one instance is allowed')
    
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

# Creating instances of the Singleton class
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s1)
print(s2)