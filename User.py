
class User:
    
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.senha = ""
    def validate(self):
        if self.password =="123" and self.nome == "deivison":
            return True
        return False
     