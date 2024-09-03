class VWOLoginPage:
     def __init__(self,email,password):
         self.email=email
         self.password=password

     def login_confirm(self):
         if self.email=="parmod@gmail.com" and self.password=="pass123":
             print("allowed")
         else:
             print("not allowed")

email=input("enter the mail: ")
password=input("enter the password: ")
vobj=VWOLoginPage(email,password)
vobj.login_confirm()
