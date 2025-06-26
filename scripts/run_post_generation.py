
import app.post_engine.post_generator as generate_post_content

def run_post_generation_job():
    generate_post_content()


if __name__ == "__main__":
    run_post_generation_job()







# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from app.post_engine.publish import fetch_post_and_publish
# def run_daily_job():
#     # generate_post_content()
#     fetch_post_and_publish()
    
    
    
# if __name__ == "__main__":
#     run_daily_job()