import pandas as pd
class Admin:
    def __init__(self,name,DOB,email,pw):
        self.username=name
        self.dob = DOB
        self.email = email
        self.pw = pw
        self.a_id=None

class User(Admin):
    def __init__(self):
        self.u_id=None
    def details(self,passw):
        if self.pw==passw:
            df=pd.DataFrame(["Name","Date Of Birth","Email"],[f"{self.f_name} {self.l_name}",f"{self.d}/{self.m}/{self.y}",self.email])
            df.to_csv("details.csv")
            return df
        else:
            print("Error! Incorrect Password")
            
class UserAuthentication:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, full_name, email, dob):
        new_user = User(username, password, full_name, email, dob)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully.")

    def register_admin(self, username, password, full_name, email, dob):
        new_admin = Admin(username, password, full_name, email, dob)
        self.users.append(new_admin)
        print(f"Admin '{username}' registered successfully.")

    def authenticate_user(self, username, password):
        for user in self.users:
            if isinstance(user, User) and user.username == username and user.password == password:
                print(f"User '{username}' authenticated successfully.")
                return True
        print("Authentication failed. Invalid username or password.")
        return False

    def authenticate_admin(self, username, password):
        for admin in self.users:
            if isinstance(admin, Admin) and admin.username == username and admin.password == password:
                print(f"Admin '{username}' authenticated successfully.")
                return True
        print("Admin authentication failed. Invalid username or password.")
        return False

    def update_password(self, user_id, new_password):
        for user in self.users:
            if user.user_id == user_id:
                user.password = new_password
                print(f"Password updated successfully for user '{user.username}'.")
                return
        print(f"User with ID '{user_id}' not found.")

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                print(f"User '{user.username}' with ID '{user_id}' deleted successfully.")
                return
        print(f"User with ID '{user_id}' not found.")

    def display_users(self):
        print("List of registered users:")
        for user in self.users:
            if isinstance(user, User):
                print(f"User ID: {user.user_id}, Username: {user.username}, Full Name: {user.full_name}, Email: {user.email}, DOB: {user.dob}")
            elif isinstance(user, Admin):
                print(f"Admin ID: {user.user_id}, Username: {user.username}, Full Name: {user.full_name}, Email: {user.email}, DOB: {user.dob}")
    