from instaloader import Instaloader, Post

L = Instaloader()

shortcode = "DE-RM7STi5H"  # Replace with your Reel shortcode
post = Post.from_shortcode(L.context, shortcode)

print("Likes:", post.likes)
print("Comments:", post.comments)

