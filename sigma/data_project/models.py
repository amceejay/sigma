from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#grab user details
class users(models.Model):
    first_name=models.CharField(max_length=40, verbose_name= "First name")
    last_name= models.CharField(max_length=40, verbose_name="Last name")
    phone_number= PhoneNumberField(null=False, blank=False, unique=True)




class user_data_input(models.Model):
    #choices in the user_data_input class
    title_choices=  [('MR', 'Mr.'),('MRS', 'Mrs.'), ('MS', 'Ms.'),]
    analysis_choices= [
                        ('RGA', 'Regression analysis'),
                        ('MCS','Monte Carlo simulation'),
                        ('FTA', 'Factor analysis'),
                        ('CHA', 'Cohort analysis'),
                        ('CTA', 'Cluster analysis'),
                        ('TSA', 'Time series analysis')
                        ('STA', 'Sentiment analysis'),
                    ]
    user_id=models.CharField(max_length=30)
    title=models.CharField(max_length=3, choices=title_choices, verbose_name='Title')
    description=models.CharField(max_length=300, verbose_name="Data description")
    column_name=models.JSONField(verbose_name='Column names')
    analysis_type=models.CharField(max_length=3, choices=analysis_choices, default='RGA')
    #data_table_name=


