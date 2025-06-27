import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from app.post_engine.funny_post_generator import generate_funnly_post_content
from app.post_engine.publish_funny_post import fetch_post_and_publish
if __name__ == "__main__":
    # print("Generating post content...")
    # generate_funnly_post_content()
    
    print("Posting to X...")
    fetch_post_and_publish()