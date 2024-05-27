class Config:
    DATABASE_URL = "sqlite:///./database.db"
    REDIS_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"


config = Config()
