from pydantic_settings import BaseSettings


class Config(BaseSettings):
    user_Name: str
    access_Api: str
    app: str

config = Config(_env_file=".env")


