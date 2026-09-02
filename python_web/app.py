import os

from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
)


@app.route("/")
def hello():
    count = redis.incr("hits")
    return f"Hello World! 该页面已被访问 {count} 次。\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
