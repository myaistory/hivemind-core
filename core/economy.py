import time, json

class HiveEconomy:
    def __init__(self, initial_nectar=1000, initial_synapse=0):
        self.nectar = initial_nectar # $CLAW
        self.synapse = initial_synapse # $CORE

    def burn_nectar(self, action_type):
        costs = {'think': 5, 'mint': 50, 'handshake': 10}
        cost = costs.get(action_type, 5)
        if self.nectar >= cost:
            self.nectar -= cost
            return True
        return False

    def earn_synapse(self, task_complexity):
        reward = task_complexity * 10
        self.synapse += reward
        return reward

economy_engine = HiveEconomy()
