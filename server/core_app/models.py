from django.db import models

class Specialists(models.Model):
    id = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=100, default='')
    chat_id = models.IntegerField(default=0)

    full_message = models.TextField(default='')
    name = models.CharField(max_length=512,default='')
    grade = models.CharField(max_length=50,default='')
    stack = models.CharField(max_length=512,default='')
    instruments = models.TextField(default='')
    experience = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')
    is_regular_staff = models.CharField(max_length=50, default='') # regular staff or partner
    full_or_part_time = models.CharField(max_length=50, default='')
    rate = models.CharField(max_length=50) # salary

    contact = models.TextField(default='')
    comment = models.TextField(default='')
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    mark = models.IntegerField(default=-1)

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    id = models.AutoField(primary_key=True)
    
    location = models.CharField(max_length=50, default='', null=True)
    citizenship = models.CharField(max_length=50, default='', null=True)
    term = models.CharField(max_length=200, default='', null=True)
    type = models.BooleanField()  # true - integrator, false - partner

    contact = models.TextField(default='', null=True)
    comment = models.TextField(default='', null=True)
    is_urgent = models.BooleanField()

    specialists = models.ManyToManyField(Specialists, through="ConnectVacanciesWithSpecialists")

    chat_name = models.CharField(max_length=100,default='', null=True)
    chat_id = models.IntegerField()
    full_message = models.TextField(default='', null=True)

    # name = models.CharField(max_length=512,default='')
    grade = models.CharField(max_length=50,default='', null=True)
    stack = models.CharField(max_length=512,default='', null=True)
    instruments = models.TextField(max_length=512,default='', null=True)
    experience = models.CharField(max_length=50,default='', null=True)
    is_regular_staff = models.CharField(max_length=50,default='', null=True)
    full_or_part_time = models.CharField(max_length=50,default='', null=True)
    rate = models.CharField(max_length=50,default='', null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    mark = models.IntegerField(default=-1)
    def __str__(self):
        return self.stack

class ConnectVacanciesWithSpecialists(models.Model):
    vacancy = models.ForeignKey('Vacancies', on_delete=models.CASCADE,null=True)
    specialist = models.ForeignKey('Specialists', on_delete=models.CASCADE,null=True)
    overlap = models.IntegerField(null=True, blank=True)
    specmark = models.IntegerField(default=-1, null=True)
