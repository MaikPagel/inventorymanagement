from django.core.management.base import BaseCommand
from inventory_app.models import Item

class Command(BaseCommand):
    help = "Migriert bestehende Items von description zu category"

    def handle(self, *args, **kwargs):
        updated = 0
        for item in Item.objects.all():
            if not item.category or item.category == "Sonstiges":
                if item.description.strip().lower() == "essen":
                    item.category = "Essen"
                elif item.description.strip().lower() == "elektronik":
                    item.category = "Elektronik"
                else:
                    item.category = "Sonstiges"
                item.save()
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"{updated} Items wurden migriert."))
