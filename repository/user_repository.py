from models.user_models import User


class UserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, user: User):
        self.users.append(user)
        return user

    def get_user(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id: int, updated_user: User):
        for index, user in enumerate(self.users):
            if user.id == user_id:
                self.users[index] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: int):
        for index, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[index]
                return True
        return False