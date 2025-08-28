
from fastapi import FastAPI
import models
from database import engine
from auth.router import router as authRouter
from user.router import router as userRouter

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(authRouter)
app.include_router(userRouter)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)
