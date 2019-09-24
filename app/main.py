from flask import Flask


web_app = Flask("KUT scheduler API")


@web_app.route("/api/v1/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    web_app.run("0.0.0.0", 8080)
