from pydantic import BaseSettings, root_validator


class Setting(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = '.env'

    @property
    def get_db_uri(self):
        return (f'postgresql+asyncpg://{self.DB_USER}:'
                f'{self.DB_PASSWORD}@{self.DB_HOST}:'
                f'{self.DB_PORT}/{self.DB_NAME}')


settings = Setting()
