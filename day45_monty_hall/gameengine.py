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

    def swap_doors(self):
        if self.player_initial_choice == self.car_door:
            self.player_final_choice = self.last_closed_goat_door
        else:
            self.player_final_choice = self.car_door

    def set_player_initial_choice(self, door_number):
        self.player_initial_choice = door_number
        self.player_final_choice = self.player_initial_choice

    def open_all_but_one_goat_doors(self):
        self.last_closed_goat_door = self.get_goat_door_to_keep_closed()
        doors_to_keep_closed = [self.car_door, self.last_closed_goat_door]
        for i in range(1, self.n_of_doors + 1):
            if i in doors_to_keep_closed:
                continue
            self.open_door(i)

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

    def open_door(self, door_number):
        self.closed_doors.remove(door_number)

    def is_win(self):
        return self.win

    def end_game(self):
        closed_doors = copy.deepcopy(self.closed_doors)
        for door_number in closed_doors:
            self.open_door(door_number)

        win = self.player_final_choice == self.car_door
        self.win = win

        stats_branch = None
        if self.player_final_choice == self.player_initial_choice:
            stats_branch = self.stats[NO_SWAP]
        else:
            stats_branch = self.stats[SWAP]

        if win:
            stats_branch[WIN] += 1
        else:
            stats_branch[LOSS] += 1

    def get_doors(self):
        return self.doors

    def get_opened_doors(self):
        opened_doors = copy.deepcopy(self.doors)
        for door_number in self.closed_doors:
            opened_doors.pop(door_number)
        return opened_doors

    def get_stats(self):
        return self.stats

    def init_doors(self):
        random_number = random.randint(1, self.n_of_doors)
        doors = {}
        for i in range(1, self.n_of_doors + 1):
            if i == random_number:
                self.car_door = i
                doors[i] = Door(i, CAR)
            else:
                doors[i] = Door(i, GOAT)
        return doors

    def init_stats(self):
        self.stats = {
        SWAP: { WIN: 0, LOSS: 0 },
        NO_SWAP: { WIN: 0, LOSS: 0 } }
