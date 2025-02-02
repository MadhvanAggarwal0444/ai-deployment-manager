import random

def send_alerts():
    balance = random.uniform(0, 100)
    if balance < 10:
        return {"alert": "Low balance warning! Recharge needed."}
    return {"status": f"Balance is sufficient: ${balance:.2f}"}
