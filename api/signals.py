from django.db.models.signals import post_save , post_delete

from django.dispatch import receiver
from .models import Book
import logging
 

logger = logging.getLogger(__name__) 


@receiver(post_save, sender=Book)
def log_book_created(sender, instance, created, *args,**kwargs):
    if created:
        logger.info(f"Book '{instance.title}' by {instance.author.name} created."  )
  

@receiver(post_delete, sender=Book)
def log_book_deleted(sender, instance,**kwargs):
    
        logger.info(f"Book '{instance.title}' by {instance.author.name} deleted."  )
  


 