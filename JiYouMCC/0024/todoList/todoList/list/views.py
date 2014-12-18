from django.shortcuts import render
from models import Status, List
import datetime


def get_first_status():
    return Status.objects.all()[0]


def get_last_status():
    return Status.objects.order_by('-id')[0]


def create_new_list(user, detail):
    new_list = List(
        user=user,
        createdate=datetime.datetime.now(),
        duedate=datetime.datetime.now(),
        status=get_first_status(),
        detail=detail
    )
    new_list.save()

def next_step_list(id):
    try:
        the_list = List.objects.get(id=id)
        if not the_list.status is get_last_status():
            the_list.status = Status.objects.get(id=the_list.status.id + 1)
        the_list.save()
    except Exception, e:
        print e

def pre_step_list(id):
    try:
        the_list = List.objects.get(id=id)
        if not the_list.status is get_first_status():
            the_list.status = Status.objects.get(id=the_list.status.id - 1)
        the_list.save()
    except Exception, e:
        print e
