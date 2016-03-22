from django.db import models


class Question(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'Question'
    def __unicode__(self):
        return self.q_text

class Phpquestion(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'phpQuestion'
    def __unicode__(self):
        return self.q_text
# class Userprof(models.Model):
#     username = models.TextField(blank=True, null=True)
#     subject = models.TextField(blank=True, null=True)
#     score = models.IntegerField(blank=True, null=True)

#     class Meta:
#         app_label = 'polls'
#         db_table = 'userprof'