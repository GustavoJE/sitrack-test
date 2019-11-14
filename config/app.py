import os

"""
Application configurations
"""

config = {
    "port": os.getenv("APP_PORT",8000),
    "debug": os.getenv("APP_DEBUG",False)
}

