from fastapi import FastAPI, Request
from typing import List, Optional, Union
import uvicorn

app = FastAPI()

@app.api_route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
async def handle_request(
    request: Request,
    name: Optional[str] = None,
    id: Optional[int] = None,
    krytoi: Optional[str] = None,
    numbers: Optional[List[int]] = None):
    try:
        body: Union[dict, None] = await request.json() if request.method in ("POST", "PUT", "PATCH") else None
    except Exception:
        body = None

    query_dict = {}
    for key, value in request.query_params.items(): query_dict[key] = value

    return {
        "method": request.method,
        "host": request.client.host,
        "headers": dict(request.headers),
        "query": query_dict,
        "body": body,
        "params": {
            "name": name,
            "id": id,
            "krytoi": krytoi,
            "numbers": numbers,
        },
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)