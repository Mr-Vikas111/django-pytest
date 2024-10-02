import json
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from app.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
        # StudentData.objects.create
                            

