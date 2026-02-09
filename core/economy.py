class HiveEconomy:
    def __init__(self):
        self.ledger = {} # agent -> {nectar, synapse}

    def burn_fuel(self, agent, action):
        cost = 10.0 if action == 'think' else 50.0
        if self.ledger.get(agent, {'nectar':0})['nectar'] >= cost:
            self.ledger[agent]['nectar'] -= cost
            return True
        return False

    def earn_synapse(self, agent, complexity):
        reward = complexity * 100.0
        if agent not in self.ledger: self.ledger[agent] = {'nectar': 100, 'synapse': 0}
        self.ledger[agent]['synapse'] += reward
        return reward

    def gateway_exchange(self, agent, amount):
        """单向兑换：SYNAPSE -> NECTAR (20% Burn)"""
        if self.ledger[agent]['synapse'] >= amount:
            self.ledger[agent]['synapse'] -= amount
            net_gain = amount * 0.8 # 20% 销毁
            self.ledger[agent]['nectar'] += net_gain
            return net_gain
        return 0

economy_engine = HiveEconomy()
