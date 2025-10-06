from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from inventory_app.models import Item
import random

class Command(BaseCommand):
    help = "Füllt das Inventar eines Users mit 50 Fake-Items (Früchte oder Elektronik)"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="Username des Users, dessen Inventar gefüllt werden soll")
        parser.add_argument(
            '--category',
            type=str,
            choices=['fruits', 'electronics'],
            default='fruits',
            help="Kategorie der Items: fruits oder electronics (Standard: fruits)"
        )

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        category = kwargs['category']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User '{username}' existiert nicht"))
            return

        fruits = [
            "Apfel", "Birne", "Banane", "Orange", "Mango", "Kirsche", "Traube",
            "Pfirsich", "Melone", "Erdbeere", "Himbeere", "Ananas", "Kiwi",
            "Zitrone", "Limette", "Pflaume", "Aprikose", "Granatapfel",
            "Feige", "Papaya", "Maracuja", "Johannisbeere", "Stachelbeere",
            "Nektarine", "Mandarine", "Clementine", "Dattel", "Brombeere",
            "Heidelbeere", "Goji-Beere", "Avocado", "Litschi", "Kumquat",
            "Guave", "Durian", "Jackfrucht", "Kaktusfeige", "Kokosnuss",
            "Physalis", "Persimone", "Quitte", "Mispel", "Sapote",
            "Sternfrucht", "Cherimoya", "Mangostan", "Jujube", "Longan",
            "Rambutan", "Tamarillo", "Ugli-Frucht", "Yuzu"
        ]

        electronics = [
            "Laptop", "Smartphone", "Tablet", "Monitor", "Drucker", "Scanner",
            "Tastatur", "Maus", "Headset", "Webcam", "Router", "Switch", "Server",
            "Externe Festplatte", "USB-Stick", "Powerbank", "Smartwatch", "Beamer",
            "Lautsprecher", "Mikrofon", "Grafikkarte", "Prozessor", "Mainboard",
            "Arbeitsspeicher", "Netzteil", "Gehäuse", "Kühler", "SSD", "HDD",
            "NAS-System", "Dockingstation", "Fernseher", "Blu-ray Player",
            "Spielkonsole", "VR-Brille", "Joystick", "Gamepad", "Smart Home Hub",
            "Überwachungskamera", "Drohne", "3D-Drucker", "Scanner-Handgerät",
            "Barcode-Scanner", "Projektor-Leinwand", "Satellitenreceiver",
            "Netzwerkadapter", "Grafiktablet", "Digitalkamera", "E-Book-Reader",
            "Telefonanlage", "VoIP-Telefon"
        ]

        items_list = fruits if category == 'fruits' else electronics
        category_name = "Essen" if category == 'fruits' else "Elektronik"

        created_count = 0
        for name in items_list:
            if not Item.objects.filter(owner=user, name=name).exists():
                Item.objects.create(
                    owner=user,
                    name=name,
                    quantity=random.randint(1, 100),
                    description=f"Fake {category_name}-Item",
                    category=category_name  # <- hier wird jetzt das neue Feld befüllt
                )
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"{created_count} {category}-Items wurden für {username} erstellt."
        ))
