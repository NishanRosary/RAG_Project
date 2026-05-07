from __future__ import annotations

import os

import uvicorn


def main() -> None:
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    reload_enabled = os.getenv("RELOAD", "true").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload_enabled,
    )


if __name__ == "__main__":
    main()
