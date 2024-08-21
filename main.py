from fastapi import FastAPI

from app.db.postgresql_db import create_db_and_tables

app = FastAPI()

from app.app import create_app

app = create_app()


# init app service todo how can i do this init in another way ?
@app.on_event("startup")
async def startup_event():
    # init database and tables
    await create_db_and_tables()
    print("Database initialized with tables.")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=7000, reload=True)
