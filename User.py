
class User:
    
    def __init__(self):
        self.id_usuario = 0
        self.nome = ""
        self.password = ""
    def validate(self):
        if self.password =="123" and self.nome == "def":
            return True
        return False
     