from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FacturSaaS API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FacturSaaS API is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "FacturSaaS API"}

@app.get("/api/invoices")
def get_invoices():
    return {
        "invoices": [
            {"id": 1, "number": "INV-001", "amount": 1000.0, "status": "paid"},
            {"id": 2, "number": "INV-002", "amount": 750.0, "status": "pending"}
        ]
    }