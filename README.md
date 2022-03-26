# smarthome-zentrale
Dieses Repository soll den Code für die zentrale Steuerung des Smart Homes beinhalten.

Installation:
Auf dem Pi müssen folgende Programme installiert sein:
    php (sudo apt install php php-mysql)
    mysql/MariaDB (sudo apt install mariodb-server)

GitHUB Webhook:
Damit der Pi automatisch die Änderungen des GitHub Repositorys lädt, muss das Verzeichnis "/home/smarthome erstellt" sein, am besten bereits einmal "git pull https://github.com/cooki371/smarthome-zentrale.git" ausgeführt sein und die "/home/smarthome/server.py" automatisch beim booten starten.