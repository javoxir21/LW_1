class UserManager:
    users: list = list()

class User:
    def __init__(self, score: int, name: str, group: str):
        self.id: int = len(UserManager.users)
        UserManager().users.append(self)

        self.name: str = name
        self.group: str = group
        self.score: int = score


user: User = User(score=3, name="Жавохир", group="ПИЖ-б-о-21-1")

print(f"ID: {user.id}\n"
      f"Имя: {user.name}\n"
      f"Группа: {user.group}\n"
      f"Баллы: {user.score}\n")
