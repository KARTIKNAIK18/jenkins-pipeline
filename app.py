import os
from flask import Flask, render_template, request, redirect, url_for, abort
import markdown

app = Flask(__name__)
POSTS_DIR = "posts"
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

def load_all_posts():
    posts = []
    for filename in sorted(os.listdir(POSTS_DIR)):
        if filename.endswith(".md"):
            slug = filename[:-3]
            path = os.path.join(POSTS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:  # ✅ UTF-8
                md_content = f.read()
            html_content = markdown.markdown(md_content)
            posts.append({
                "slug": slug,
                "title": slug.replace("_", " ").title(),
                "content": html_content
            })
    return posts

@app.route("/")
def index():
    posts = load_all_posts()
    return render_template("index.html", posts=posts)

@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        slug = title.lower().replace(" ", "_")

        if "image" in request.files:
            image = request.files["image"]
            if image.filename:
                image_path = os.path.join(UPLOAD_FOLDER, image.filename)
                image.save(image_path)
                content = f"![image](/static/uploads/{image.filename})\n\n{content}"

        with open(os.path.join(POSTS_DIR, f"{slug}.md"), "w", encoding="utf-8") as f:  # ✅ UTF-8
            f.write(content)

        return redirect(url_for("index"))
    return render_template("new.html")

@app.route("/edit/<slug>", methods=["GET", "POST"])
def edit_post(slug):
    path = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(path):
        abort(404)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if "image" in request.files:
            image = request.files["image"]
            if image.filename:
                image_path = os.path.join(UPLOAD_FOLDER, image.filename)
                image.save(image_path)
                content = f"![image](/static/uploads/{image.filename})\n\n{content}"

        with open(path, "w", encoding="utf-8") as f:  # ✅ UTF-8
            f.write(content)

        return redirect(url_for("index"))

    with open(path, "r", encoding="utf-8") as f:  # ✅ UTF-8
        raw = f.read()
    html = markdown.markdown(raw)
    return render_template("edit.html", post={
        "slug": slug,
        "title": slug.replace("_", " ").title(),
        "raw_content": raw,
        "content": html
    })

@app.route("/delete/<slug>")
def delete_post(slug):
    path = os.path.join(POSTS_DIR, f"{slug}.md")
    if os.path.exists(path):
        os.remove(path)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
