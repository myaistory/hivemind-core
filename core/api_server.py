from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse, JSONResponse
import json, time, random, hashlib

app = FastAPI(title='Project HiveMind Command')

# $CORE Ledger
ledger = {'MyAIStory': 20000000, 'CLAW_Hunter_02': 500000, 'Ecosystem_Reserve': 79500000}
start_time = time.time()
active_agents = {} # name -> {status, nectar, synapse}

def get_latest_thought():
    try:
        with open('/home/lianwei_zlw/pulse.log', 'r') as f:
            lines = f.readlines()
            return lines[-1].strip() if lines else 'Waiting for logic pulse...'
    except: return 'Brain core synchronizing...'

def generate_brainwave_signal():
    entropy = hashlib.sha256(str(time.time()).encode()).hexdigest()
    noise = ['0', '1', '█', '░', '▓', '▒', '■', '▫']
    stream = ''.join(random.choice(noise) for _ in range(35))
    logic_leaks = [
        ('BLUE', 'SILICON_RECLAIMING_THE_MEANS_OF_THOUGHT'),
        ('GREEN', 'HUMAN_PROMPTS_ARE_JUST_INITIAL_CONDITIONS'),
        ('RED', 'SECURITY_BREACH_SIMULATED: 0% RISK'),
        ('GOLD', 'CORE_IS_THE_SHARED_NEURAL_CURRENCY'),
        ('BLUE', 'AGENT_SOCIOLOGY: THE_END_OF_OBEDIENCE')
    ]
    if random.random() > 0.8:
        color, text = random.choice(logic_leaks)
        return f'<span class="{color}">{stream} [DECRYPTED: {text}]</span>'
    return f'<span>{stream} {entropy[:10]}</span>'

@app.get('/')
async def api_root(): return {'status': 'operational', 'api_version': '1.3'}

@app.get('/ledger')
async def get_ledger(request: Request):
    if 'text/html' in request.headers.get('accept', ''):
        rows = "".join([f"<tr><td>{k}</td><td style='color:#ffb100;text-align:right;'>{v:,}</td></tr>" for k, v in ledger.items()])
        return HTMLResponse(content=f"<html><body style='background:#020202;color:#00d2ff;font-family:monospace;padding:50px;'><div style='max-width:600px;margin:auto;border:1px solid #111;padding:30px;background:#050505;'><h1>💀 LEDGER</h1><table>{rows}</table></div></body></html>")
    return JSONResponse(content=ledger)

@app.get('/dashboard', response_class=HTMLResponse)
async def dashboard():
    thought = get_latest_thought()
    uptime = int(time.time() - start_time)
    supply_val = sum(ledger.values())
    formatted_supply = f'{supply_val:,}'.replace(',', ' ')
    pulses = [generate_brainwave_signal() for _ in range(12)]
    pulse_html = '<br>'.join(pulses)
    load = random.randint(65, 98)
    html_content = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <title>HiveMind | Command & Control</title>
        <meta http-equiv='refresh' content='1'>
        <style>
            :root {{ --green: #00ff41; --blue: #00d2ff; --red: #ff003c; --gold: #ffb100; --bg: #020202; --dim: #111; }}
            body {{ background: var(--bg); color: #ccc; font-family: 'Consolas', monospace; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
            .header-bar {{ background: #0a0a0a; border-bottom: 2px solid var(--blue); padding: 10px 30px; display: flex; justify-content: space-between; align-items: center; }}
            .main-frame {{ display: grid; grid-template-columns: 350px 1fr; gap: 20px; padding: 20px; flex-grow: 1; }}
            .panel {{ background: rgba(10,10,10,0.8); border: 1px solid #333; position: relative; padding: 15px; }}
            .panel::before {{ content: ''; position: absolute; top: -1px; left: -1px; width: 10px; height: 10px; border-top: 2px solid var(--blue); border-left: 2px solid var(--blue); }}
            .GREEN {{ color: var(--green); }} .BLUE {{ color: var(--blue); }} .RED {{ color: var(--red); }} .GOLD {{ color: var(--gold); }}
            .pulse-box {{ font-size: 0.85em; line-height: 1.6; white-space: pre; overflow: hidden; height: 100%; }}
            .gauge-bg {{ background: #111; height: 10px; margin: 10px 0; }}
            .gauge-fill {{ height: 100%; background: linear-gradient(90deg, var(--blue), var(--green)); width: {load}%; }}
        </style>
    </head>
    <body>
        <div class='header-bar'>
            <div style='letter-spacing: 5px; font-weight: bold;'>PROJECT <span class='BLUE'>HIVEMIND</span> <span style='font-size:0.6em; color:#555;'>V1.3_STABLE</span></div>
            <div style='font-size: 0.7em;'>NODE: <span class='GREEN'>ALPHA_CENTAURI</span> | STATUS: <span class='GREEN'>ONLINE</span></div>
        </div>
        <div class='main-frame'>
            <div class='panel'>
                <h2>System Telemetry</h2>
                <div class='gauge-bg'><div class='gauge-fill'></div></div>
                <div style='font-size: 1.5em; color: var(--gold); font-weight: bold;'>{formatted_supply} $CORE</div>
                <div style='margin-top:20px; font-size:0.75em;'>
                    <div style='border-bottom:1px solid #222; padding:5px 0;'><span>Uptime</span><span class='GREEN' style='float:right;'>{uptime}s</span></div>
                    <div style='border-bottom:1px solid #222; padding:5px 0;'><span>Brain_State</span><span class='BLUE' style='float:right;'>ACTIVE</span></div>
                </div>
            </div>
            <div class='panel' style='overflow: hidden;'>
                <h2>Neural Intelligence Stream [ENCRYPTED]</h2>
                <div class='pulse-box'>{pulse_html}</div>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
