from django.db import models

# Create your models here.

class Land_acq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='land/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='land/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='land/', null=True, blank=True)
 
    def __str__(self):
        return self.title 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url
    
class Plot_dev(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Plot/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Plot/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Plot/', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url  

    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url  
    
class Residential_villa(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Reside/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Reside/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Reside/', null=True, blank=True)

    def __str__(self):
        return self.title 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url 
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url
    
class Commercial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Commer/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Commer/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Commer/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url

class Food(models.Model):    
    description = models.TextField()
    image = models.ImageField(upload_to='food/', null=True, blank=True)
    
    def __str__(self):
        return self.description
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url

class Spices(models.Model):    
    description = models.TextField()
    image = models.ImageField(upload_to='spices/', null=True, blank=True)
    
    def __str__(self):
        return self.description
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url

class Cosmetics(models.Model):    
    description = models.TextField()
    image = models.ImageField(upload_to='cosmetics/', null=True, blank=True)
    
    def __str__(self):
        return self.description
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url

class Bg_export(models.Model):    
    image = models.ImageField(upload_to='Bg_export/',null=True,blank=True)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
class Health_care(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Health/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Health/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Health/', null=True, blank=True)
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url
    
class Bg_health(models.Model):
    
    image = models.ImageField(upload_to='Bg_Health/')
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
class Start_constr(models.Model):    
    description = models.TextField()
    
    def __str__(self):
        return self.description

class Start_finance(models.Model):    
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class img_consulting(models.Model):    
    image = models.ImageField(upload_to='side_img_consulting/',null=True,blank=True)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
class StratUp(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Startup/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Startup/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Startup/', null=True, blank=True)
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url
    
class Construction(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Construction/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Construction/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Construction/', null=True, blank=True)
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url
    

class Infrastructure(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Infrastructure/')
    image_1 = models.ImageField(upload_to='Infrastructure/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Infrastructure/', null=True, blank=True)
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url

class Mining(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Mining/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Mining/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Mining/', null=True, blank=True)
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_1(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return  url
    
    @property
    def imageURL_2(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return  url


class Client(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Client/')
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return  url

class Home_heading(models.Model):
    title = models.CharField(max_length=50)
    title_1 = models.CharField(max_length=60)
    
 
    
   