class PowerBallPlayer:
    def __init__(self, regular_numbers, powerball_number):
        self.lottery_tickets_used = 0
        self.regular_numbers = regular_numbers
        self.powerball_number = powerball_number

    def buy_ticket(self):
        self.lottery_tickets_used += 1

    def get_tickets_used(self):
        return self.lottery_tickets_used
