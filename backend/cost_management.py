import random

def monitor_costs():
    current_cost = random.uniform(10, 50)
    if current_cost > 40:
        return {"alert": "High cost detected! Consider optimizing your setup."}
    return {"status": f"Current cost: ${current_cost:.2f}"}
