from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Required settings with sensible defaults for development
    
    environment: str = 'development'

    database_url: str = "sqlite:///./rolltheday.db"
    secret_key: str = "your-secret-key-here-change-in-production"
    default_admin_password: str = "b00mb00!"
    default_admin_email: str = "root@rolltheday.com"
    
    # Optional settings with safe defaults
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    bcrypt_rounds: int = 12

    # Simple logging configuration
    log_level: str = "INFO"
    envvar: str = 'envvarpresent'

    class Config:
        env_file = ".env"


settings = Settings()