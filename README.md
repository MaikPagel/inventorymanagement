# Inventory Management System

**Ein webbasiertes Bestandsverwaltungssystem – entwickelt mit Django, PostgreSQL, HTML+CSS**

---

## 🎯 Zielgruppe

Dieses Projekt richtet sich an:

- Nicht-technische Stakeholder (z. B. HR Manager, Management), die einen Überblick über digitale Bestandsverwaltungssysteme erhalten möchten.
- Unternehmen, die ein grundlegendes System zur Verwaltung von Lagerbeständen kennenlernen wollen.

---

## ℹ️ Was macht dieses Projekt?

Das Inventory Management System ermöglicht:

- Hinzufügen, Bearbeiten und Löschen von Produkten über eine Weboberfläche.
- Verwaltung von Produktinformationen wie Name, Kategorie und Lagerbestand.
- Übersichtlich gestaltetes Frontend für bessere Benutzerfreundlichkeit.
- Speicherung der Daten in einer **PostgreSQL-Datenbank**.

---

## ⚙️ Technologien

| Technologie | Verwendung |
|---|---|
| Python & Django | Backend-Logik und Datenverwaltung |
| PostgreSQL | Datenbank für Produktinformationen |
| HTML / CSS | Frontend und Styling |
| Django Templates | Verbindung von Backend und Frontend |

---

## 💻 Wie kann man es ausprobieren?

1. Stelle sicher, dass auf deinem Rechner **Python**, **PostgreSQL** und **pip** installiert sind.
2. Klone das Projekt:
   ```bash
   git clone https://github.com/MaikPagel/inventorymanagement.git
3. Wechsle in das Projektverzeichnis:
   ```bash
   cd inventorymanagement
4. Optional: Erstelle und aktiviere eine virtuelle Umgebung:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
5. Installiere die benötigten Python-Pakete:
   ```bash
   pip install -r requirements.txt
6. Stelle sicher, dass PostgreSQL läuft, und erstelle eine Datenbank für das Projekt. (DBeaver als Programm)
7. Führe die Django-Migrationen durch:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
8. Starte den Entwicklungsserver:
   ```bash
   python manage.py runserver
9. Öffne deinen Browser und gehe zu:
    ```bash
    http://127.0.0.1:8000/

## 🔮 Zukünftige Erweiterungen

- Rollenverwaltung für unterschiedliche Benutzerrechte (Admin / Mitarbeiter)
- Erweiterte Reporting- und Exportfunktionen (API Endpoints)
- Mobile-responsive Design und Optimierung

## 👤 Wer steckt dahinter & Kontakt

Entwickelt von: Maik Pagel

Wenn du Feedback hast oder mitarbeiten möchtest, erreichst du mich hier: [Maik Pagel](https://github.com/MaikPagel)
