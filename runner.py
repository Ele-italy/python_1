import uvicorn

from new_project_with_sql import app

uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

