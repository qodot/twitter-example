import os

from twitter.common.container import DIContainerFactory


env = os.environ.get("ENVIRONMENT", "development")
container = DIContainerFactory.factory(env)
