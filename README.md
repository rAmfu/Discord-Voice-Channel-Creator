markdown
# 🎤 Discord Voice Channel Creator

Bot Discord, który automatycznie tworzy i zarządza tymczasowymi kanałami głosowymi z pełnym panelem zarządzania.

[![Status](https://img.shields.io/badge/status-aktywny-success)](https://github.com/rAmfu/Discord-Voice-Channel-Creator)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue)](https://github.com/Rapptz/discord.py)

---

## 📋 Spis treści
- [✨ Funkcje](#-funkcje)
- [🚀 Szybki start](#-szybki-start)
- [📦 Instalacja na Debianie 12](#-instalacja-na-debianie-12)
- [🔧 Uruchamianie w tle](#-uruchamianie-w-tle)
- [🐳 Docker](#-docker)
- [📁 Struktura plików](#-struktura-plików)
- [🎯 Jak to działa](#-jak-to-działa)
- [🔐 Bezpieczeństwo](#-bezpieczeństwo)
- [📝 Konfiguracja](#-konfiguracja)
- [🛠️ Szczegóły techniczne](#️-szczegóły-techniczne)
- [🐛 Rozwiązywanie problemów](#-rozwiązywanie-problemów)
- [🤝 Współpraca](#-współpraca)
- [📄 Licencja](#-licencja)
- [💬 Wsparcie](#-wsparcie)

---

## ✨ Funkcje

### 🚀 Automatyczne tworzenie kanałów
- Gdy użytkownik wejdzie na **kanał trigger**, bot automatycznie tworzy dla niego nowy prywatny kanał głosowy
- Każdy użytkownik otrzymuje swój własny spersonalizowany kanał w formacie: `🎤 {nazwa_użytkownika}`
- Kanały są tworzone w tej samej kategorii co kanał trigger

### ⚙️ Panel zarządzania
Po utworzeniu kanału, na kanale pojawia się interaktywny panel z embedem. Właściciel kanału może:

| Funkcja | Opis |
|---------|------|
| **👥 Limit użytkowników** | Ustawia maksymalną liczbę osób na kanale (0-99) |
| **🔒 Prywatny / Publiczny** | Przełącza widoczność kanału |
| **✏️ Zmiana nazwy** | Zmienia nazwę kanału |
| **📝 Zmień opis** | Dodaje/usuwa opis kanału (wyświetlany w embedzie) |
| **👑 Przekaż właściciela** | Oddaje kontrolę nad kanałem innemu użytkownikowi |
| **🚪 Wyrzuć użytkownika** | Wyrzuca osobę z kanału |
| **🚫 Zablokuj użytkownika** | Blokuje dostęp do kanału |
| **🔓 Odblokuj użytkownika** | Przywraca dostęp zablokowanemu użytkownikowi |
| **🗑️ Usuń kanał** | Usuwa kanał |

### 🧹 Automatyczne czyszczenie
- Puste kanały są automatycznie usuwane po 15 sekundach
- Zapobiega gromadzeniu się nieużywanych kanałów

### 🔄 Trwałość danych
- Dane o właścicielach kanałów są zapisywane w pliku `channels.json`
- Panele zarządzania są automatycznie przywracane po restarcie bota

### 🛡️ Ochrona przed duplikatami
- Każdy użytkownik może posiadać tylko jeden kanał tymczasowy
- Zapobiega tworzeniu wielu kanałów dla tego samego użytkownika

---

## 🚀 Szybki start

### Wymagania
- Python 3.8 lub nowszy
- Token bota Discord z odpowiednimi uprawnieniami
- Serwer Discord z uprawnieniami administratora

### Instalacja

1. **Sklonuj repozytorium:**
```bash
git clone https://github.com/rAmfu/Discord-Voice-Channel-Creator.git
cd Discord-Voice-Channel-Creator
Zainstaluj zależności:

bash
pip install discord.py
Skonfiguruj bota:

Otwórz plik bot.py

Ustaw swoje zmienne:

python
TOKEN = "twój_token_bota"
GUILD_ID = 123456789012345678  # ID twojego serwera
TRIGGER_CHANNEL_ID = 123456789012345678  # ID kanału trigger
Uruchom bota:

bash
python bot.py
Wymagane uprawnienia bota
Zarządzanie kanałami - do tworzenia, edycji i usuwania kanałów

Łączenie - do dołączania do kanałów głosowych

Przenoszenie członków - do przenoszenia użytkowników między kanałami

Zarządzanie uprawnieniami - do ustawiania uprawnień kanałów

Wyświetlanie kanałów - do widzenia kanałów

Wysyłanie wiadomości - do wysyłania panelu zarządzania

Wstawianie linków - dla wyświetlania embedów

Aktywność głosowa - do monitorowania stanu głosowego

Wymagane intenty
guilds - informacje o serwerze

members - szczegóły członków

voice_states - śledzenie aktywności głosowej

message_content - obsługa wiadomości

📦 Instalacja na Debianie 12
Krok 1: Aktualizacja systemu
bash
sudo apt update
sudo apt upgrade -y
Krok 2: Instalacja podstawowych narzędzi
bash
sudo apt install -y python3 python3-pip git screen python3-venv
Krok 3: Instalacja discord.py
bash
pip3 install discord.py
Krok 4: Pobranie bota
bash
git clone https://github.com/rAmfu/Discord-Voice-Channel-Creator.git
cd Discord-Voice-Channel-Creator
Krok 5: Konfiguracja
bash
nano bot.py
Wpisz swoje dane:

python
TOKEN = "twój_token_bota"
GUILD_ID = 123456789012345678
TRIGGER_CHANNEL_ID = 123456789012345678
Krok 6: Uruchomienie
bash
python3 bot.py
Instalacja z środowiskiem wirtualnym (zalecana)
bash
# Utworzenie środowiska wirtualnego
python3 -m venv venv

# Aktywacja środowiska
source venv/bin/activate

# Instalacja discord.py w środowisku
pip install discord.py

# Uruchomienie
python bot.py
🔧 Uruchamianie w tle
Metoda 1: Screen (zalecana)
bash
# Instalacja screen (jeśli nie masz)
sudo apt install -y screen

# Uruchomienie bota w sesji screen
screen -S voicebot
python3 bot.py

# Wyjście z sesji (bot dalej działa)
Ctrl+A, następnie D

# Powrót do sesji
screen -r voicebot

# Zatrzymanie bota
Ctrl+C
Metoda 2: Systemd (usługa)
bash
# Utworzenie pliku usługi
sudo nano /etc/systemd/system/voicebot.service
Wpisz:

ini
[Unit]
Description=Discord Voice Channel Bot
After=network.target

[Service]
Type=simple
User=bot-kick
WorkingDirectory=/home/bot-kick/Discord-Voice-Channel-Creator
ExecStart=/usr/bin/python3 /home/bot-kick/Discord-Voice-Channel-Creator/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
bash
# Aktywacja usługi
sudo systemctl daemon-reload
sudo systemctl enable voicebot
sudo systemctl start voicebot

# Status usługi
sudo systemctl status voicebot

# Logi
sudo journalctl -u voicebot -f
Metoda 3: Tmux
bash
# Instalacja tmux
sudo apt install -y tmux

# Uruchomienie
tmux new -s voicebot
python3 bot.py

# Wyjście
Ctrl+B, następnie D

# Powrót
tmux attach -t voicebot
🐳 Docker
Instalacja Dockera
bash
sudo apt install -y docker.io docker-compose
Tworzenie Dockerfile
bash
cat > Dockerfile << EOF
FROM python:3.11-slim

WORKDIR /app

RUN pip install discord.py

COPY bot.py .
COPY channels.json .

CMD ["python", "bot.py"]
EOF
Budowanie i uruchomienie
bash
# Budowanie obrazu
docker build -t voicebot .

# Uruchomienie w tle
docker run -d --name voicebot --restart unless-stopped voicebot

# Sprawdzenie logów
docker logs -f voicebot

# Zatrzymanie
docker stop voicebot

# Usunięcie kontenera
docker rm voicebot
Docker Compose
bash
cat > docker-compose.yml << EOF
version: '3'

services:
  voicebot:
    build: .
    container_name: voicebot
    restart: unless-stopped
    volumes:
      - ./channels.json:/app/channels.json
EOF
bash
# Uruchomienie
docker-compose up -d

# Logi
docker-compose logs -f

# Zatrzymanie
docker-compose down
📁 Struktura plików
text
Discord-Voice-Channel-Creator/
├── bot.py              # Główny kod bota
├── channels.json       # Dane właścicieli kanałów (tworzony automatycznie)
├── LICENSE            # Licencja MIT
├── README.md          # Ten plik
├── Dockerfile         # Dla Dockera (opcjonalny)
├── docker-compose.yml # Dla Docker Compose (opcjonalny)
└── requirements.txt   # Zależności (opcjonalny)
🎯 Jak to działa
Użytkownik wchodzi na kanał trigger

Bot tworzy nowy kanał głosowy z nazwą użytkownika

Użytkownik jest przenoszony do swojego nowego kanału

Pojawia się panel zarządzania z embedem i sterowaniem

Użytkownik może dostosować swój kanał za pomocą interaktywnego menu

Gdy kanał jest pusty, zostaje automatycznie usunięty po 15 sekundach

🔐 Bezpieczeństwo
Tylko właściciel kanału może używać panelu zarządzania

Stary właściciel traci wszystkie uprawnienia po przekazaniu właściciela

Uprawnienia są automatycznie usuwane podczas usuwania kanału

📝 Konfiguracja
Bot używa trzech głównych zmiennych konfiguracyjnych:

python
TOKEN = "twój_token_bota"
GUILD_ID = 123456789012345678
TRIGGER_CHANNEL_ID = 123456789012345678
Jak znaleźć ID serwera i kanału?
Włącz Tryb dewelopera w Discord (Ustawienia → Zaawansowane → Tryb dewelopera)

Kliknij prawym przyciskiem na serwer → Kopiuj ID

Kliknij prawym przyciskiem na kanał → Kopiuj ID

🛠️ Szczegóły techniczne
Zbudowany z użyciem biblioteki discord.py

Wykorzystuje komponenty UI Discorda (Przyciski, Menu wyboru, Modale)

Trwałe widoki do przywracania paneli

Przechowywanie danych w formacie JSON (nie wymaga bazy danych)

System czyszczenia w pętli (interwał 15 sekund)

Tworzenie kanałów oparte na zdarzeniach

🐛 Rozwiązywanie problemów
Problem: ModuleNotFoundError: No module named 'discord'
bash
pip3 install discord.py
# lub jeśli używasz venv:
source venv/bin/activate
pip install discord.py
Problem: Brak uprawnień
bash
# Dodaj uprawnienia do pliku
chmod +x bot.py

# Uruchom jako root (jeśli konieczne)
sudo python3 bot.py
Problem: Bot nie łączy się z Discord
Sprawdź czy token jest poprawny

Sprawdź czy intenty są włączone w panelu dewelopera

Sprawdź połączenie internetowe

Problem: Bot nie tworzy kanałów
Sprawdź czy bot ma uprawnienia do zarządzania kanałami

Sprawdź czy kanał trigger istnieje

Sprawdź logi bota

Problem: Błąd 404 podczas usuwania kanału
Bot najpierw wysyła odpowiedź, potem usuwa kanał

Jeśli błąd występuje, sprawdź czy kanał został już usunięty

🤝 Współpraca
Zapraszam do współpracy! Jeśli masz pomysł na ulepszenie, zgłoś go przez Issue lub wyślij Pull Request.

Forkuj projekt

Utwórz swoją gałąź (git checkout -b feature/AmazingFeature)

Zatwierdź zmiany (git commit -m 'Add some AmazingFeature')

Wypchnij gałąź (git push origin feature/AmazingFeature)

Otwórz Pull Request

📄 Licencja
Ten projekt jest licencjonowany na warunkach licencji MIT - zobacz plik LICENSE dla szczegółów.

💬 Wsparcie
W przypadku pytań, problemów lub sugestii, otwórz Issue na GitHubie.

🌟 Autor
rAmfu

GitHub: @rAmfu

Stworzone z ❤️ dla społeczności Discord

text
