import random



def is_it_dog(dog):
  app = current_app()
  sol = "not " if random.choice([True, False]) else ""
  return app.config['hazil']
