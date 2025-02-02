import os

# Spheron API configuration (update these with your actual details)
SPHERON_API_KEY = os.getenv("SPHERON_API_KEY", "YOUR_DEFAULT_API_KEY")
SPHERON_PROJECT_ID = os.getenv("SPHERON_PROJECT_ID", "YOUR_PROJECT_ID")

# Spheron API endpoints (these are sample endpoints – update based on actual documentation)
SPHERON_SCALE_ENDPOINT = "https://api.spheron.network/deployments/scale"
SPHERON_REDEPLOY_ENDPOINT = "https://api.spheron.network/deployments/redeploy"
SPHERON_COST_ENDPOINT = "https://api.spheron.network/deployments/cost"

