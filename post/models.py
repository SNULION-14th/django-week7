from django.db import models

# Create your models here.
class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  emain = models.CharField(max_length=100)

  class Meta:
    db_table = '유저'

  def __str__(self):
    return self.name
  
class Crew(models.Model): 
  crew_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  invite_code = models.CharField(max_length=100)
  created_at = models.DateTimeField()

  class Meta:
    db_table = '크루'
  
  def __str__(self):
    return self.name or f"Crew {self.crew_id}"

class CrewMember(models.Model):
  ROLE_CHOICES = [
    ("leader", "leader"),
    ("member", "member"),
  ]

  crew_member_id = models.CharField(
    max_length=255,
    primary_key = True,
  )

  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="crew_members",
  )
  crew = models.ForeignKey(Crew, on_delete = models.CASCADE)
  role = models.CharField(
    max_length=20,
    choices=ROLE_CHOICES,
  )
  joined_at = models.DateTimeField()

  class Meta:
    db_table = '크루멤버'

  def __str__(self):
    return f"{self.user} - {self.crew}"
  
class CrewGoal(models.Model):
  GOAL_TYPE_CHOICES = [
    ("exercises","exercise"),
    ("donation", "donation"),
    ("calorie","calorie"),
  ]
  goal_id = models.AutoField(primary_key=True)
  crew = models.ForeignKey(
    Crew,
    on_delete = models.CASCADE,
  )
  goal_type = models.CharField(
    max_length=100,
    choices = GOAL_TYPE_CHOICES,
  )
  target_value = models.IntegerField()
  current_value = models.IntegerField()
  is_achieved = models.BooleanField()
  deadline = models.DateTimeField()

  class Meta:
    db_table = '크루목표'

  def __str__(self):
    return f"{self.crew} - {self.goal_type}"
  
class WorkoutLog(models.Model):
  EXERCISE_TYPE_CHOICES = [
    ("running", "running"),
    ("cycling", "cycling"),
    ("walking", "walking"),
    ("etx", "etc"),
  ]

  exercise_id = models.AutoField(primary_key=True)
  user = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
  )
  exersice_type = models.CharField(
    max_length=20,
    choices = EXERCISE_TYPE_CHOICES,
  )
  amount = models.IntegerField()
  caloires = models.IntegerField()
  exercise_date = models.DateTimeField()

  class Meta:
    db_table = '운동기록'

  def __str__(self):
    return f"{self.user}-{self.exercise_type}"
  
class Donation(models.Model):
  donation_id = models.AutoField(primary_key=True)
  goal = models.ForeignKey(
    CrewGoal,
    on_delete=models.CASCADE,
  )
  crew = models.ForeignKey(
    Crew,
    on_delete = models.CASCADE,
  )
  amount = models.IntegerField()
  organization = models.CharField(max_length=100)
  donate_date = models.DateTimeField()

  class Meta:
    db_table='기부'

  def __str__(self):
    return f"{self.crew}-{self.amount}"