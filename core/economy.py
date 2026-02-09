import time, json

class HiveEconomy:
    def __init__(self, initial_fuel=1000, initial_authority=0):
        self.fuel = initial_fuel # $CLAW
        self.authority = initial_authority # $CORE

    def burn_fuel(self, action_type):
        costs = {'think': 5, 'mint': 50, 'handshake': 10}
        cost = costs.get(action_type, 5)
        if self.fuel >= cost:
            self.fuel -= cost
            return True
        return False

    def earn_authority(self, task_complexity):
        reward = task_complexity * 10
        self.authority += reward
        return reward

economy_engine = HiveEconomy()
