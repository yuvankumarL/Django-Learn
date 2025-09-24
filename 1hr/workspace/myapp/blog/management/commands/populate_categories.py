
from typing import Any
# from blog.models import Post, Category
from blog.models import Category
from django.core.management.base import BaseCommand
import random
from django.db import connection

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Category.objects.all().delete()
        # Reset auto-increment ID (PostgreSQL example)
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE blog_post AUTO_INCREMENT = 1;")

        categories = [
            'Sports',
            'Technology',
            'Science',
            'Art',
            'Food'
        ]
        
        # categories = Category.objects.all()
        for category_name in categories:
            Category.objects.create(name=category_name)


        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))