class User:
    username = "kambiz dirbaz"
    password = "23654"
    def isCorrect(self, _user_name, _password):
        return self.username==_user_name and self.password == _password


user_n = input("enter the username: ")
user_p = input("enter the password: ")
user = User()
print(user.isCorrect(user_n,user_p))
        
