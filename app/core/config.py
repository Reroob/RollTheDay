from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Required settings (no defaults - must be in .env)
    
    environment: str | None = 'Development'

    database_url: str = ""
    secret_key: str = ""
    default_admin_password: str = "b00mb00!"
    default_admin_email: str = "root@rolltheday.com"
    
    # Optional settings with safe defaults
    algorithm: str = ""
    access_token_expire_minutes: int = 30
    bcrypt_rounds: int = 12


    # Simple logging configuration
    log_level: str = "INFO"
    envvar: str='envvarnotpresent'

    class Config:
        env_file = ".env"


settings = Settings()