# flask_app.py
from flask import Flask, request, jsonify
from instaloader import Instaloader, Post

app = Flask(__name__)
L = Instaloader()
L.load_session_from_file("session-beyyond_code")


@app.route("/get_reel_stats", methods=["POST"])
def get_reel_stats():
    data = request.json
    shortcode = data.get("shortcode")
    post = Post.from_shortcode(L.context, shortcode)
    
    result = {
        "likes": post.likes,
        "comments": post.comments,
        "views": post.video_view_count if post.is_video else None
    }
    return jsonify(result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
