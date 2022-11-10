class User:
    def __init__(self, score: int, name: str, group: str, manager):
        self.manager = manager
        self.id: int = len(manager.user_list)
        self.manager.user_list.append(self)

        self.name: str = name
        self.group: str = group
        self.score: int = score

    def __str__(self) -> str:
        return self.name

    def __del__(self):
        self.manager.remove_user(user=self)

class UserManager:
    def __init__(self):
        self.user_list: list() = list()

    def remove_user(self, user):
        self.user_list.remove(user)
        try:
            del user
        except Exception:
            pass

    def add_user(self, score: int, name: str, group: str, manager):
        new_user: User = User(score=score, name=name, group=group, manager=manager)

manager: UserManager = UserManager()

javohir: User = User(score=3, name="Жавохир", group="ПИЖ-б-о-21-1", manager=manager)
manager.add_user(score=5, name="Егор", group="ПИЖ-б-о-21-1", manager=manager)

for user in manager.user_list:
    print(user)

