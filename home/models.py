from django.db import models

# Create your models here.
class ContactUs(models.Model):
    contact_type = models.CharField(max_length=200)
    request = models.CharField(max_length=500)
    user = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.contact_type}-{self.user}'
    
    class Meta:
        verbose_name = 'ContactUs(requests)'
        verbose_name_plural ='People requests(contacts)'
