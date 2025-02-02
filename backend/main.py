from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend origins
    allow_credentials=True,
    allow_methods=["*"],   # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],   # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.get("/auto-scale")
def auto_scale():
    return {"status": "Auto-Scaling triggered successfully!"}

@app.get("/cost-management")
def cost_management():
    return {"status": "Cost Management is optimized!"}

@app.get("/error-fix")
def error_fix():
    return {"status": "Errors fixed and site redeployed!"}

@app.get("/alerts")
def alerts():
    return {"status": "Alerts sent for possible issues!"}

@app.get("/optimize")
def optimize():
    return {"status": "One-Click Optimization complete!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
