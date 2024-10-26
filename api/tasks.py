from celery import shared_task
from django.utils import timezone
from . models import Book


@shared_task
def archive_old_books():
    ten_years_ago = timezone.now().date() - timezone.timedelta(days=365 * 10)
    Book.objects.filter(published_date___lte=ten_years_ago).update(is_archive=True)