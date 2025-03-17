class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def soar(self):
        return f"{self.name} is soaring high with a wingspan of {self.wingspan} meters!"
    
    def __str__(self):
        return f"{self.name} is an eagle with a wingspan of {self.wingspan} meters."
