from django.db import models

# Create your models here.
class User(models.Model):
  user_id = models.IntegerField(primary_key=True)
  password = models.CharField(max_length=20)
  name = models.CharField(max_length=20)
  work_start_time = models.TimeField()
  work_end_time = models.TimeField()

  def __str__(self):
    return str(self.user_id)
  
class Task(models.Model):
  # Enum definition (for "status" field)
  class Status(models.TextChoices):
    PENDING = 'PE', 'Pending'
    WORKING = 'WO', 'Working'
    DONE = 'DO', 'Done'

  task_id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=100)
  category = models.CharField(max_length=20)
  priority = models.IntegerField()
  deadline = models.DateTimeField()
  estimated_duration = models.IntegerField()
  status = models.CharField(
    max_length=2,
    choices=Status.choices,
    default=Status.PENDING,
  )
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.task_id)
  
class Scheduled_task(models.Model):
  scheduled_id = models.IntegerField(primary_key=True)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  is_locked = models.BooleanField()
  task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.scheduled_id)
  
class Task_history(models.Model):
  history_id = models.IntegerField(primary_key=True)
  planned_duration = models.IntegerField()
  actual_duration = models.IntegerField()
  completed_at = models.DateTimeField()
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.history_id)
  
class Fixed_schedule(models.Model):
  schedule_id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.schedule_id)