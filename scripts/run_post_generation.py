import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app.post_engine.funny_post_generator as funny_post_generator

def run_post_generation_job():
    funny_post_generator.generate_funnly_post_content()





# import app.post_engine.post_generator as post_generator

# def run_post_generation_job():
#     post_generator.generate_post_content()


if __name__ == "__main__":
    run_post_generation_job()




