from flashcard_api.models import Progress, Rating
import datetime
from django.utils import timezone

def sm2_algorithm(progress:Progress, rating:Rating) -> None:

    quality = int(rating)

    print(f"DEBUG{progress.ease_factor}")
    print((0.1- (5 - quality)*(0.08 + (5-quality)*0.02)))

    new_easiness_factor:float = round(progress.ease_factor + (0.1 - (5 - quality)*(0.08 + (5-quality)*0.02)),2)
    if new_easiness_factor<1.3:
        new_easiness_factor = 1.3
    print(f"DEBUG:{new_easiness_factor}")

    if(rating==Rating.AGAIN):
        progress.successful_repetitions = 0
        progress.interval = 0
    else: 
        progress.successful_repetitions+=1

        if(progress.successful_repetitions==1):
            progress.interval = 1
        elif(progress.successful_repetitions==2):
            progress.interval = 6;
        else:
            progress.interval = round(progress.interval*new_easiness_factor)
    now = timezone.now()
    progress.ease_factor = new_easiness_factor
    progress.last_reviewed_at = now 
    progress.due_at = now+ datetime.timedelta(days = progress.interval)

