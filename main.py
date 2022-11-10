class User:
    def __init__(self, **kwargs):
        self.user_info: dict = kwargs


user = User(name="Жавохир", group="ПИЖ-б-о-21-1", course=2)

for key, val in user.user_info.items():
    print(f"{key}: {val}")
