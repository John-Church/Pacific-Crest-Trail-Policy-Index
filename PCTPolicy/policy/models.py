from django.db import models

class State(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "State"

class Region(models.Model):
    name = models.CharField(max_length=80)

    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Region"


class Park(models.Model):
    name = models.CharField(max_length=80)
    JURISDICTION_CHOICES = [
    ('FD', 'Federal'),
    ('ST', 'State'),
    ]
    federal_or_state = models.CharField(max_length=2, choices=JURISDICTION_CHOICES)
    size_in_acres = models.IntegerField(default=0)
    annual_visitors = models.IntegerField(default=0)
    average_annual_fire_coverage = models.IntegerField(default=0)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Park"


class Policy(models.Model):
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    ammended = models.BooleanField('ammended?', default=False)
    pub_date = models.DateField('date published')
    CATEGORIES = [
        ('CLI', 'climate'),
        ('CST', 'construction'),
        ('INF', 'infastructure'),
        ('TSR', 'trail services'),
        ('COM', 'commercial use'),
        ('CON', 'conservation'),
        ('ENF', 'enforcement'),
        ('TMT', 'trail maintenance'),
        ('OVR', 'oversight'),
        ('FIN', 'finance'),
        ('WIL', 'wildlife'),
        ('PLT', 'plantlife'),
        ('HIK', 'hiking'),
        ('BIK', 'biking'),
        ('HRS', 'horseback riding'),
        ('UNC', 'unconventional use'),
        ('MOT', 'motorized vehicles'),
        ('HEA', 'health'),
        ('WAT', 'water'),
        ('FIR', 'fire'),
        ('VUM', 'visitor use management'),
        ('PER', 'permits'),
        ('VOL', 'volunteers'),
        ('OTH', 'other'),
    ]
    category = models.CharField(max_length=3, choices=CATEGORIES)
    pdf = models.FileField('PDF', upload_to='policypdfs/', blank=True)
    link = models.CharField('Link to Online Copy', max_length=120,  blank=True)


    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = "Policies"
