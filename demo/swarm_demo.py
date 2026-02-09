import json, time

def run_local_swarm():
    print('[SWARM] Initializing Local Collective...')
    # 模拟博弈过程
    tasks = [{'id': 101, 'reward': 500, 'cost': 100}]
    for t in tasks:
        print(f'[TASK] New task issued: #{t["id"]} (Reward: {t["reward"]})')
        time.sleep(1)
        print(f'[BID] Agent_Hunter_01 (Aggressive) Utility: 6.00')
        print(f'[BID] Agent_Hunter_02 (Stable) Utility: 4.00')
        print(f'[WINNER] Agent_Hunter_01 captured Task #{t["id"]}')

if __name__ == '__main__': run_local_swarm()
