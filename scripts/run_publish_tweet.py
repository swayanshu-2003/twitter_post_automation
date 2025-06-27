import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app.post_engine.publish_funny_post as publish_funny

def run_publish_job():
    publish_funny.fetch_post_and_publish()

#below is for long conceptual threaded tweets


# import app.post_engine.publish as publish

# def run_publish_job():
#     publish.fetch_post_and_publish()

if __name__ == "__main__":
    run_publish_job()