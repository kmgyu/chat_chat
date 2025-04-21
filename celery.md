celery 사용 기록

python manage.py migrate
python run_once.py

celery worker 실행
celery -A config.celery_app worker --loglevel=info --pool=solo

celery beat 실행
