import os
import subprocess
import time

def sync_to_github():
    print('[SENTINEL] Checking for changes...')
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'System: Autonomous periodic sync & structural cleanup'])
    subprocess.run(['git', 'push', 'origin', 'main'])

if __name__ == '__main__':
    while True:
        sync_to_github()
        time.sleep(7200) # 每2小时同步一次
