import psutil

def handle_auto_scaling():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        return {"status": "Scaling up: Adding more resources"}
    elif cpu_usage < 30:
        return {"status": "Scaling down: Reducing resources"}
    return {"status": "Stable: No scaling needed"}
