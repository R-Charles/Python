class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First: {self.first_name}")
        print(f"Last: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):

        if self.gold_card_points < amount:
            print('Insufficient Funds')
            return self
        self.gold_card_points = self.gold_card_points - amount


my_user = User('Raphael', 'Charles', 'rapcharlo@aol.com', 37)

my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(50)
my_user.display_info()
boooooooooooo
