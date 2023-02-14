import pydantic


class AppSettings(pydantic.BaseSettings):
    redis_url = pydantic.RedisDsn(url="redis://localhost/", scheme="redis")
    redis_port: int = 6379

    class Config:  # type: ignore[misc]
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
