from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

RENEW_BASE = "https://renew.corporateformfiling.com"

@app.get("/{token}")
def redirect_token(token: str):
    return RedirectResponse(
        url=f"{RENEW_BASE}/?t={token}",
        status_code=302
    )

@app.get("/health")
def health():
    return {"ok": True}

