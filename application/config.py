class Config:
    """Base configuration."""
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:JonJamLil24!@localhost/lesson5_db"
    CACHE_TYPE = "SimpleCache"
    DEBUG = True
    CACHE_DEFAULT_TIMEOUT = 300

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """Production-specific configuration."""
    SQLALCHEMY_DATABASE_URI = 'postgresql://m16l2assignment_user:jaVndQdAFRwMQKNCbHC5k3IZ5JFDMber@dpg-cs782at6l47c7393anlg-a.oregon-postgres.render.com/m16l2assignment'
    DEBUG = False
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}