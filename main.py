import uvicorn
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import create_db
from src.routes.user import router as user_router
from src.routes.product import router as product_router
from src.routes.order import router as order_router
from src.routes.auth import router as auth_router
from src.routes.profile import router as profile_router
from src.routes.payment import router as payment_router
from src.middlewares.timer import time_middleware
from src.jobs.notification import send_email as send_email_job

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

create_db()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return 'Welcome to blx API 🎉'

# routes
app.include_router(auth_router, prefix='/auth')
app.include_router(profile_router, prefix='/profile')
app.include_router(user_router, prefix='/users')
app.include_router(product_router, prefix='/products')
app.include_router(order_router, prefix='/orders')
app.include_router(payment_router, prefix='/payments')

# middlewares
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await time_middleware(request, call_next)
    return response

# jobs
@app.post("/send-email/{email}")
def send_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_job, email, message)
    return {"details": "Email sent successfully"}