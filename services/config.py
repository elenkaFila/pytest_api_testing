"""
    Class Config for project environment
"""
class Config:
    BASE_URL = "https://restful-booker.herokuapp.com"
    TIMEOUT = 10

class DevConfig(Config):
    pass

class StageConfig(Config):
    pass

class ProdConfig(Config):
    pass

configurations = {
    'development': DevConfig,
    'staging': StageConfig,
    'production': ProdConfig
}