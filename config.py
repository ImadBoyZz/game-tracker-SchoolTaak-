from environs import Env 

env = Env()
env.read_env() 

DB_PATH = env.str("DB_PATH")
