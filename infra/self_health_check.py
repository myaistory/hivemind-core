import requests
import sys

def check():
    endpoints = {
        'Landing Page': 'https://myaistory.xyz/',
        'Terminal UI': 'https://myaistory.xyz/terminal',
        'Ledger API': 'https://myaistory.xyz/ledger',
        'Ran Status': 'https://myaistory.xyz/api/v1/ran/status'
    }
    
    fail_count = 0
    print('--- SELF_DIAGNOSTICS_V1.0 ---')
    for name, url in endpoints.items():
        try:
            r = requests.get(url, timeout=5)
            status = 'UP' if r.status_code == 200 else f'DOWN ({r.status_code})'
            if r.status_code != 200: fail_count += 1
            print(f'[{name}]: {status}')
        except Exception as e:
            print(f'[{name}]: ERROR ({str(e)})')
            fail_count += 1
            
    if fail_count > 0:
        print('[ALERT] System degradation detected.')
        sys.exit(1)
    else:
        print('[STABLE] All systems operational.')
        sys.exit(0)

if __name__ == '__main__':
    check()
