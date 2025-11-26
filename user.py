class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"


class UserService:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, email):
        if self._user_exists(username):
            raise ValueError("Username already taken.")
        user = User(username, email)
        self.users.append(user)
        return user
    
    def get_all_users(self):
        return self.users
    
    def _user_exists(self, username):
        return any(user.username == username for user in self.users)
