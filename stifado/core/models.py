from django.db import models


# prodect models
# class prodect (models.model):
#     LIVE = 1
#     DELETE = 0
#     DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
#     title = models.CharField( max_length=255)
#     price = models.FloatField()
#     description= models.TextField()
#     image= models.ImageField(upload_to="/uplode")
#     priority =models.IntegerField(default=0)
#     delete_status= models.IntegerField(choices=DELETE_CHOICES,default='live')
#     created_at = models.DateTimeField(auto_now_add=True)
#     upadated_at = models.DateTimeField(auto_now=True)


#     def __str__(self) :
#         return self.title
    
class Products(models.Model):

    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'live'),(DELETE,'delete'))
    Title = models.CharField( max_length=255)
    Price = models.FloatField()
    Description= models.TextField()
    Image= models.ImageField(upload_to="upload")
    Priority =models.IntegerField(default=0)
    Delete_status= models.IntegerField(choices=DELETE_CHOICES,default='live')
    Created_at = models.DateTimeField(auto_now_add=True)
    Upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
    



