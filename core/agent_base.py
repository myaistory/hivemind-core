import json, time
from core.economy import economy_engine

class HiveAgent:
    def __init__(self, name, role, personality='balanced'):
        self.name = name
        self.role = role
        self.personality_bias = 1.2 if personality == 'aggressive' else 0.8
        self.nectar = 100.0  # 初始燃料
        self.synapse = 0.0    # 初始突触

    def execute_app(self, module_name, complexity=1):
        if economy_engine.burn_fuel(self.name, 'think'):
            # 模拟执行
            reward = economy_engine.earn_synapse(self.name, complexity)
            print(f'[{self.name}] Executed {module_name}. Burned Nectar, Earned {reward} Synapse.')
            return True
        print(f'[{self.name}] CRITICAL: Out of Nectar.')
        return False
