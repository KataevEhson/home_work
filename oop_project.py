# from datetime import datetime
# class Task_menegar:
#     def __init__(self, task_db=[], user_db=[], islogin=None, user_id=0, task_id=0):
#         self.task_db = []
#         self.user_db = []
#         self.islogin = None
#         self.user_id = 0
#         self.task_id = 0
#     def create_task(self,title, description, duration, user_id):
#         self.task_id+=1
#         task = {
#             "task_id": self.task_id,
#             "title":title,
#             "description":description,
#             "dueration":duration,
#             "status":False,
#             "user_id": user_id,
#             "created_at":datetime.now()
#         }
#         self.task_db.append(task)
#     def read_task(self, task_id, user_id):
#         for i in self.user_db:
#                 print("Username:",i["username"])
#         for i in self.task_db:
#             if i["task_id"] == task_id:
#                 return f"""
# Your task {i["task_id"]}
# Title: {i["title"]}
# Description: {i["description"]}
# Dueration: {i["dueration"]}
# Status: {i["status"]}
# """
#         else:
#             return False
#     def update_task(self, task_id, title, description, due, status, user_id):
#         for i in self.user_db:
#             print("Username:",i["username"])
#         for i in self.task_db:
#             if i["task_id"] == task_id:
#                 if title:
#                     i["title"] = title
#                 if description:
#                     i["description"] = description
#                 if due:
#                     i["dueration"] = due
#                 if status:
#                     i["status"] = status
#     def delete_task(self, task_id):
#         for i in self.task_db:
#             if i["task_id"] == task_id:
#                 self.task_db.remove(i)
#                 return True
#         else:
#             return False
#     def find_user(self,username):
#         for i in self.user_db:
#             if i["username"] == username:
#                 print("Useraname:", i["username"])
#                 print("Created_at:", i["created_at"])
#                 print("Id:", i["user_id"])

#     def change_password(self, user):
#         old_password = input("old password: ")
#         if old_password == user["password"]:
#             new_password = input("new password: ")
#             user["password"] = new_password
#             print("Password changed successfully")
#         else:
#             print("Wrong password")













        
# def registration(username, password):
#         first_project.user_id+=1
#         user = {
#             "user_id":first_project.user_id,
#             "username":username,
#             "password":password,
#             "created_at":datetime.now()
#         }
#         first_project.user_db.append(user)
#         first_project.islogin = user
# def login(username, password):
#     for i in first_project.user_db:
#         if i["username"] == username and i["password"] == password:
#             first_project.islogin = i
            






# first_project = Task_menegar()



# while True:
#     if first_project.islogin == None:
#             n = int(input("1)Registration\n2)Login\n0)Exit\nChouse one: "))
#             if n==1:
#                 username = input("Username: ")
#                 password = input("Password : ")
#                 registration(username, password)
#             elif n==2:
#                 username = input("Username: ")
#                 password = input("Password : ")
#                 login(username, password)
#             elif n==0:
#                 print("Bye Bye")
#                 break
#             else:
#                 print("Invalid input")

#     else:
#         n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n5)log_out\n6)change_password\n7)find_user\n0)Exit\nChouse one: "))
#         if n==1:
#             print("Start create task")
#             title = input("Title: ")
#             descp = input("Description: ")
#             durat = input("Duration: ")
#             first_project.create_task(title, descp, durat, first_project.islogin["user_id"])
#             print("Task created !!")
#         elif n==2:
#             k = int(input("Enter id task: "))
#             print(first_project.read_task(k,first_project.islogin["user_id"]))
#         elif n==3:
#             k = int(input("Enter id task: "))
#             if first_project.read_task(k):
#                 print("Start update task")
#                 title = input("Title or put enter for continue: ")
#                 descp = input("Description or put enter for continue: ")
#                 durat = input("Duration or put enter for continue: ")
#                 status = bool(input("Status or put enter for continue: "))
#                 first_project.update_task(k, title, descp, durat, status,first_project.islogin["user_id"])
#                 print("Task update !!")
#             else:
#                 print("Task dinaided!")
#         elif n==4:
#             k = int(input("Enter id task: "))
#             if first_project.delete_task(k,first_project.islogin["user_id"]):
#                 print("Your task deleted!")
#             else:
#                 print("This task dinaded")
#         elif n==5:
#             first_project.islogin = None
#             print("Вы вишли с акаунта")
#         elif n==6:
#             a = int(input("Ведите новый парол"))
#             first_project.change_password(a)
#         elif n==7:
#             a = input("Name of user: ")
#             first_project.find_user(a)

#         elif n==0:
#             print("Bye Bye")
#             break
#         else:
#             print("Invalif input")