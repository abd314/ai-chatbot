
import redis
import json
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RedisCache:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0, ttl: int = 600):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.ttl = ttl  # Time-to-live in seconds (default: 10 minutes)

    def get(self, key: str) -> Optional[str]:
        try:
            value = self.client.get(key)
            if value:
                logger.info(f"Cache HIT for key: {key}")
                return value
            else:
                logger.info(f"Cache MISS for key: {key}")
                return None
        except redis.ConnectionError as e:
            logger.error(f"Redis connection error: {e}")
            return None

    def set(self, key: str, value: str) -> bool:
        try:
            self.client.setex(key, self.ttl, value)
            return True
        except redis.ConnectionError as e:
            logger.error(f"Redis connection error: {e}")
            return False