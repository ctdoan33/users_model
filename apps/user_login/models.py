# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

# call create_valid_user with inputs in shell to validate and create user if valid
def create_valid_user(first_name="", last_name="", email_address="", age=None):
    valid=True
    if len(first_name)<2:
        print "first_name must be at least 2 characters"
        valid=False
    if len(last_name)<2:
        print "last_name must be at least 2 characters"
        valid=False
    if not EMAIL_REGEX.match(email_address):
        print "email_address is invalid"
        valid=False
    elif User.objects.filter(email_address=email_address):
        print "email_address already exists"
        valid=False
    if age==None:
        print "age must be given"
        valid=False
    if valid:
        User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address, age=age)
        print "Successfully created valid user"

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
