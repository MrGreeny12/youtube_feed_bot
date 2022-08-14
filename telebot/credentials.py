from environs import Env

env = Env()
env.read_env()


bot_token = env("BOT_TOKEN")
bot_user_name = env("BOT_USERNAME")
URL = env("WEBHOOK_URL")
