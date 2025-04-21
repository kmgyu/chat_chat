# run_once.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django_celery_beat.models import PeriodicTask, IntervalSchedule

# 5초마다 반복되는 스케줄 생성 (없으면 생성)
schedule, created = IntervalSchedule.objects.get_or_create(
    every=5,
    period=IntervalSchedule.SECONDS,
)

# 이미 동일한 이름의 작업이 있다면 건너뜀
if not PeriodicTask.objects.filter(name='Print hello every 5 seconds').exists():
    PeriodicTask.objects.create(
        interval=schedule,
        name='Print hello every 5 seconds',
        task='ws_chat.tasks.print_hello',  # 실제 app 이름과 경로 맞게 수정
    )
    print("✅ Periodic task 등록 완료")
else:
    print("⚠️ 이미 등록된 작업이 있습니다.")
