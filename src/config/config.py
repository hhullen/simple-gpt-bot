from dataclasses import dataclass
from environs import Env

@dataclass
class DBConfig:
    db: str
    host: str
    user: str
    password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DBConfig


def load_configuration(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(TgBot(token=env("BOT_TOKEN"),
                                  admin_ids=list(map(int, env.list("ADMIN_IDS")))),
                            DBConfig(db=env("DATABASE"),
                                     host=env("DB_HOST"),
                                     user=env("DB_USER"),
                                     password=env("DB_PASSWORD")))
