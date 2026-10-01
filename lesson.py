# class Bank:
#     def __init__(self, owner, pinkod, balance):
#         self.owner = owner
#         self.__pinkod = pinkod
#         self._balance = balance
#     @property
#     def show_info(self):
#         return f"Balance: {self._balance}"
#     @show_info.setter
#     def show_info(self, ammount):
#         if ammount>0:
#             self._balance/=ammount
#             return f"Balance: {self._balance}"

# card1 = Bank("Ehson", 1234, 1000)



# print(card1.show_info)
# card1.show_info = 2
# print(card1.show_info)





from datetime import datetime
task_db = []
user_db = []
is_login = None


user_id = 0
task_id = 0

def create_task(title, description, dueration, user_id):
    global task_id
    task_id+=1
    task = {
        "task_id": task_id,
        "title":title,
        "description": description,
        "dueration": dueration,
        "status": False,
        "user_id": user_id,
        "created_at": datetime.now()
    }
    task_db.append(task)


def read_task(task_id, user_id):
    for i in user_db:
        print("Username:",i["username"])
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            return f"""
Your task {i["task_id"]}:
Title:{i["title"]}
Description:{i["description"]}
Dueration :{i["dueration"]}
Status:{i["status"]}
                  """
    else:
        return False




def update_task(task_id, title, descp, due, status,user_id):
    for i in user_db:
        print("Username:",i["username"])
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            if title:
                i["title"] = title
            if descp:
                i["description"] = descp
            if due:
                i["dueration"] = due
            if status:
                i["status"] = status




def  delete_task(task_id, user_id ):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            task_db.remove(i)
            return True
    else:
        return False



def registration(username, password):
    global user_id, is_login
    user_id+=1
    user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "created_at": datetime.now()
    }
    user_db.append(user)
    is_login = user




def login(username, password):
    for i in user_db:
        global is_login
        if i["username"] == username and i["password"] == password:
            return i





def find_user(usernae):
    for i in user_db:
        if i["username"] == usernae:
            print("Username:", i["username"])
            print("Created_at:", i["created_at"])
            print("Id:", i["user_id"])

def change_password(user):

    old_password = input("old password: ")
    if old_password == user["password"]:
        new_password = input("new password: ")
        user["password"] = new_password
        print("Password changed successfully")
    else:

        print("Wrong password")


while True:
    if is_login == None:
        n = int(input("1)Registration\n2)Login\n6)Find_user\n0)Exit\nChouse one: "))
        match n:
            case 1:
                username = input("Username: ")
                password = input("Password : ")
                registration(username, password)
            case 2:
                username = input("Username: ")
                password = input("Password : ")
                login(username, password)
            case 0:
                print("Good bye")
                break



    else:
        n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n5)log_out\n6)change_password\n0)Exit\nChouse one: "))
        match n:
            case 1:
                print("Start create task")
                title = input("Title: ")
                descp = input("Description: ")
                durat = input("Duration: ")
                create_task(title, descp, durat, is_login["user_id"])
                print("Task created !!")

            case 2:
                k = int(input("Enter id task: "))
                print(read_task(k, is_login["user_id"]))
            case 3:
                print("Start update task")
                k = int(input("Enter id task: "))
                if read_task(k, is_login["user_id"]):
                    title = input("Title or put enter for continue: ")
                    descp = input("Description or put enter for continue: ")
                    durat = input("Duration or put enter for continue: ")
                    status = bool(input("Status or put enter for continue: "))
                    update_task(k, title, descp, durat, status, is_login["user_id"])
                    print("Task update !!")
                else:
                    print("This task dinaded")
            case 4:
                k = int(input("Enter id task: "))
                if delete_task(k, is_login["user_id"]):
                    print("Your task deleted!")
                else:
                    print("This task dinaded")
            case 5:
                is_login = None
                print("Вы вишли с акаунта")
            case 6:
                a = input()
                change_password(a)
            case 0:
                print("Exit")
                break
            case _:
                print("Invalid input!")