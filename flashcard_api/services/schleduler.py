from sm2 import sm2_algorithm
from flashcard_api.models import Progress, Rating

def sm2_scheduler(progress:Progress, rating:Rating)-> Progress:
    sm2_algorithm(progress=progress, rating=rating)
    progress.save()
    return progress