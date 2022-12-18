import json
from blog_app.models import Post

with open('posts.json') as f:
    post_json = json.load(f)

for post in post_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()
