class FollowUser:
    def __init__(self):
        self.users = []

    @staticmethod
    def get_user_info(username):
        pass

    @staticmethod
    def get_list_of_users():
        pass

    def follow_user(self, username):

        if username in self.get_list_of_users():
            if username not in self.users:
                self.users.append(username)
            return True
        else:
            return False

    def unfollow_user(self, username):
        if username in self.get_list_of_users():
            if username in self.users:
                self.users.remove(username)
            return True
        else:
            return False
