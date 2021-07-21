from django.db import models

# class Testt(models.Model):
#     title = models.CharField(max_length=150)
#     content = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now_add=True)
#     photo = models.ImageField(upload_to='photos/$Y/$m/$d/')
#     is_publoshed = models.BooleanField(default=True)
#     category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'New'
#         verbose_name_plural = 'News'
#         ordering = ['-created_at']

# class Category(models.Model):
#     title = models.CharField(max_length=150, db_index=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Category'
#         ordering = ['title']


