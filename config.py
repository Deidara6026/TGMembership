user = 'user'
password = 'secure_pass?'
host = 'interestinghost.com'
port = 3306
database = 'username$tgc'
db_url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "lolololololdfntgbrbcytrbeeaweuxsecretprobably"

    # Database
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


