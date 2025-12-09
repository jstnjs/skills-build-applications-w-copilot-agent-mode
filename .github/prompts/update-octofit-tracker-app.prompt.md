mode: 'agent'
model: GPT-4.1

# Django App Updates

- All Django project files are in de map `octofit-tracker/backend/octofit_tracker`.

1. Update `settings.py` voor MongoDB-verbinding en CORS.
2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` en `admin.py` om ondersteuning te bieden voor users, teams, activities, leaderboard en workouts collecties.
3. Zorg dat `/` naar de API wijst en dat `api_root` aanwezig is in `urls.py`. (Zie <attachments> hierboven voor bestandsinhoud. Je hoeft het bestand mogelijk niet opnieuw te zoeken of te lezen.)
