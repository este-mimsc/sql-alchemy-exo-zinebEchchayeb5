from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models  # Import models après db.init_app

    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Flask + SQLAlchemy assignment"})

    @app.route("/users", methods=["GET", "POST"])
    def users():
        if request.method == "GET":
            all_users = models.User.query.all()
            return jsonify([{"id": u.id, "username": u.username} for u in all_users])

        elif request.method == "POST":
            data = request.get_json()
            if not data or "username" not in data:
                return jsonify({"error": "username is required"}), 400
            new_user = models.User(username=data["username"])
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"id": new_user.id, "username": new_user.username}), 201

    @app.route("/posts", methods=["GET", "POST"])
    def posts():
        if request.method == "GET":
            all_posts = models.Post.query.all()
            return jsonify([
                {
                    "id": p.id,
                    "title": p.title,
                    "content": p.content,
                    "author": p.author.username
                } for p in all_posts
            ])

        elif request.method == "POST":
            data = request.get_json()
            if not data or "title" not in data or "content" not in data or "user_id" not in data:
                return jsonify({"error": "title, content and user_id are required"}), 400

            user = models.User.query.get(data["user_id"])
            if not user:
                return jsonify({"error": "User not found"}), 404

            new_post = models.Post(title=data["title"], content=data["content"], author=user)
            db.session.add(new_post)
            db.session.commit()
            return jsonify({
                "id": new_post.id,
                "title": new_post.title,
                "content": new_post.content,
                "author": user.username
            }), 201

    return app
