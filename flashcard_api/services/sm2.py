from flashcard_api.models import Progress, Rating
import datetime
from django.utils import timezone

def sm2_algorithm(progress:Progress, rating:Rating) -> None:

    quality = int(rating)

    new_easiness_factor:float = progress.ease_factor + (1.0 - (5 - quality)*(0.08 + (5-quality)*0.02))
    if new_easiness_factor<1.3:
        new_easiness_factor = 1.3

    if(rating==Rating.AGAIN):
        progress.successful_repetitions = 0
        progress.interval = 1
    else: 
        progress.successful_repetitions+=1

        if(progress.successful_repetitions==1):
            progress.interval = 1
        elif(progress.successful_repetitions==2):
            progress.interval = 6;
        else:
            progress.interval = round(progress.interval*new_easiness_factor)
    now = timezone.now()
    progress.due_at = now+ datetime.timedelta(days = progress.interval)
    progress.ease_factor = new_easiness_factor
    progress.last_reviewed_at = now 
