import random
import copy
from door import Door

GOAT, CAR = 'GOAT', 'CAR'
SWAP, NO_SWAP = 'SWAP', 'NO_SWAP'
WIN, LOSS = 'WIN', 'LOSS'

class GameEngine:
    def __init__(self, n_of_doors):
        self.n_of_doors = n_of_doors
        self.init_stats()

    def start_game(self):
        self.doors = self.init_doors()
        self.closed_doors = list(range(1, self.n_of_doors + 1))
        self.player_initial_choice = None
        self.player_final_choice = None

    def end_game(self):
        self.open_all_doors()
        self.calculate_game_result()
        self.update_stats()

    def get_doors(self):
        return self.doors

    def get_stats(self):
        return self.stats

    def get_opened_doors(self):
        opened_doors = {}
        for number in self.doors:
            if number in self.closed_doors:
                continue
            opened_doors[number] = self.doors[number]

        return opened_doors

    def set_player_initial_choice(self, door_number):
        self.player_initial_choice = door_number

    def swap_doors(self):
        if self.player_initial_choice == self.car_door:
            self.player_final_choice = self.last_closed_goat_door
        else:
            self.player_final_choice = self.car_door

    def confirm_initial_choice(self):
        self.player_final_choice = self.player_initial_choice

    def is_win(self):
        return self.player_won

    def open_all_but_one_goat_doors(self):
        self.last_closed_goat_door = self.get_goat_door_to_keep_closed()
        doors_to_keep_closed = [self.car_door, self.last_closed_goat_door]
        doors_to_open = [i for i in range(1, self.n_of_doors + 1) if i not in doors_to_keep_closed]
        self.open_doors(doors_to_open)

    def open_doors(self, door_numbers):
        for i in door_numbers:
            self.open_door(i)

    def open_door(self, door_number):
        self.closed_doors.remove(door_number)

    def open_all_doors(self):
        closed_doors = copy.deepcopy(self.closed_doors)
        self.open_doors(closed_doors)

    def get_goat_door_to_keep_closed(self):
        if self.player_initial_choice == self.car_door:
            another_door_number = self.choose_random_goat_door()
            return another_door_number
        return self.player_initial_choice

    def choose_random_goat_door(self):
        random_door_number = random.randint(1, self.n_of_doors)
        if not self.doors[random_door_number].is_goat():
            return self.choose_random_goat_door()
        return random_door_number

    def increment_stats(self, did_swap, did_win):
        self.stats[did_swap][did_win] += 1

    def calculate_game_result(self):
        self.player_won = self.player_final_choice == self.car_door

    def update_swap_stats(self):
        if self.player_won:
            self.increment_stats(SWAP, WIN)
        else:
            self.increment_stats(SWAP, LOSS)

    def update_no_swap_stats(self):
        if self.player_won:
            self.increment_stats(NO_SWAP, WIN)
        else:
            self.increment_stats(NO_SWAP, LOSS)

    def update_stats(self):
        stats_branch = None
        player_swapped = self.player_final_choice != self.player_initial_choice
        if player_swapped:
            self.update_swap_stats()
        else:
            self.update_no_swap_stats()

    def generate_car_door_number(self):
        random_number = random.randint(1, self.n_of_doors)
        self.car_door = random_number

        return random_number

    def init_doors(self):
        car_door_number = self.generate_car_door_number()
        doors = {}
        for i in range(1, self.n_of_doors + 1):
            door_type = CAR if i == car_door_number else GOAT
            doors[i] = Door(i, door_type)
        return doors

    def init_stats(self):
        self.stats = {
        SWAP: { WIN: 0, LOSS: 0 },
        NO_SWAP: { WIN: 0, LOSS: 0 } }
