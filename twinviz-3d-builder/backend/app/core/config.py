from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TwinViz 3D Builder"
    DATABASE_URL: str = "sqlite:///./twinviz.db"
    UPLOAD_DIR: str = "uploads"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        extra = "allow"  # lets extra env vars (like host/port) pass

settings = Settings()
