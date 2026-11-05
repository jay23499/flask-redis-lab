import os

from flask import Flask, jsonify
import redis

app = Flask(__name__)

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    socket_connect_timeout=2,
    socket_timeout=2,
    decode_responses=True,
)


@app.get("/")
def home():
    try:
        visits = cache.incr("visits")
        return (
            "<h1>Jerry's Flask + Redis Lab</h1>"
            f"<p>Visits: {visits}</p>"
        )
    except redis.exceptions.RedisError:
        return "<h1>Redis is unavailable</h1>", 503


@app.get("/health")
def health():
    try:
        cache.ping()
        return jsonify(status="healthy"), 200
    except redis.exceptions.RedisError:
        return jsonify(status="unhealthy", dependency="redis"), 503
