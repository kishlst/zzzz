class Main:
    name = None 
    age = None

    def __init__(self, name, age):
        name = self.name
        age = self.age 
        
    def __str__(self, name, age):
        return f"{name} - {age}"

vlad = Main("vlad", 12)
print(vlad)