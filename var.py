import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from config import Var as Config
    from Config import Var as Config
else:
    from local_config import Development as Config


Var = Config
