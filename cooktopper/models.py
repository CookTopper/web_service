from django.db import models

class Stove(models.Model):
	token = models.CharField(blank=False, max_length=45)
	mac_address = models.CharField(blank=False, max_length=45)

class BurnerState(models.Model):
	description = models.CharField(blank=False, max_length=45)

class Temperature(models.Model):
	description = models.CharField(blank=False, max_length=45)

class Burner(models.Model):
	description = models.CharField(blank=False, max_length=45)
	stove = models.ForeignKey(Stove, on_delete=models.CASCADE)
	temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
	burner_state = models.ForeignKey(BurnerState, on_delete=models.CASCADE)
	time = models.IntegerField()

class RequestBurner(models.Model):
	burner_id = models.ForeignKey(Burner, on_delete=models.CASCADE)
	new_temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
	new_burner_state = models.ForeignKey(BurnerState, on_delete=models.CASCADE)
	programmed_time = models.IntegerField()
	programming_id = models.IntegerField()

class PanState(models.Model):
	description = models.CharField(blank=False, max_length=45)

class Pan(models.Model):
	code = models.CharField(blank=False, max_length=45)
	temperature = models.IntegerField()
	pan_state = models.ForeignKey(PanState, on_delete=models.CASCADE)

class Programming(models.Model):
	temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
	burner_state = models.ForeignKey(BurnerState, on_delete=models.CASCADE)
	programmed_time = models.IntegerField()
	expected_duration = models.IntegerField()
	creation_time = models.IntegerField()

class Shortcut(models.Model):
	description = models.CharField(blank=False, max_length=45)
	programming = models.ForeignKey(Programming, on_delete=models.CASCADE)

class SmokeSensor(models.Model):
	smoke_level = models.IntegerField()
