from celery import Celery
from .stat import load_game_sessions, generate_pie_chart, generate_easy, generate_hard

app = Celery('HelloDjango')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def update_charts():
    game_sessions = load_game_sessions()
    generate_pie_chart(game_sessions)
    generate_easy(game_sessions)
    generate_hard(game_sessions)

# Schedule the task to run every minute
app.conf.beat_schedule = {
    'update-charts-every-minute': {
        'task': 'path.to.update_charts',
        'schedule': 60.0,  # 60 seconds = 1 minute
    },
}