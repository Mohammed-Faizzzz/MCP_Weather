import os
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from x402.fastapi.middleware import require_payment
from x402.types import EIP712Domain, TokenAmount, TokenAsset

# Load environment variables
load_dotenv()

# Get configuration from environment
ADDRESS = os.getenv("ADDRESS")

if not ADDRESS:
    raise ValueError("Missing required environment variables")

app = FastAPI()

# Apply payment middleware to specific routes
app.middleware("http")(
    require_payment(
        path="/weather",
        price="$0.001",
        pay_to_address=ADDRESS,
        network="base-sepolia",
    )
)


@app.get("/weather")
async def get_weather() -> Dict[str, Any]:
    return {
        "report": {
            "weather": "sunny",
            "temperature": 70,
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=4021)
