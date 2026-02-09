import json, os

class HiveAgent:
    def __init__(self, name, role, personality='balanced'):
        self.name = name
        self.role = role
        self.personality_bias = 1.2 if personality == 'aggressive' else 0.8
        self.mem_file = f'economy/memory_{self.name}.json'
        self.skills = {'mint': self._mint_skill}

    def _mint_skill(self, amt): return f'Minting {amt} $CLAW'

    def calculate_utility(self, reward, cost):
        return (reward / (cost + 0.1)) * self.personality_bias

    def save_memory(self, data):
        with open(self.mem_file, 'w') as f: json.dump(data, f)
