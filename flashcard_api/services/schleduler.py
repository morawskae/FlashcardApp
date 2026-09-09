from sm2 import sm2_algorithm
from flashcard_api.models import FcProgress, Rating

def sm2_scheduler(progress:FcProgress, rating:Rating)-> FcProgress:
    sm2_algorithm(progress=progress, rating=rating)
    progress.save()
    return progress