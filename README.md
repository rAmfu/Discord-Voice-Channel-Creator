# 🎤 Discord Voice Channel Creator

🌍 Język: **Polski** | [English](README_EN.md) 🔄 Wersja: **Node-js** | [Node-js](https://github.com/rAmfu/Discord-Voice-Channel-Creator/)

Bot Discord do automatycznego tworzenia i zarządzania tymczasowymi kanałami głosowymi. Napisany w Node.js z wykorzystaniem discord.js v14.



## ✨ Funkcje

- 🚀 **Automatyczne tworzenie kanałów** - Gdy użytkownik dołączy do kanału trigger, bot automatycznie tworzy dla niego kanał głosowy
- 👑 **Panel zarządzania** - Każdy właściciel kanału otrzymuje interaktywny panel z embedem
- 🔒 **Zarządzanie prywatnością** - Możliwość przełączania między kanałem publicznym a prywatnym
- 👥 **Zarządzanie dostępem** - Dodawanie i usuwanie dostępu dla wybranych użytkowników
- ✏️ **Personalizacja** - Zmiana nazwy, opisu i limitu użytkowników
- 👑 **Transfer własności** - Przekazywanie kanału innemu użytkownikowi
- 🚫 **Moderacja** - Wyrzucanie i blokowanie użytkowników
- 🗑️ **Auto-czyszczenie** - Automatyczne usuwanie pustych kanałów
- 🔄 **Odświeżanie** - Przycisk do ręcznej aktualizacji panelu



## 📋 Wymagania

- Node.js v16.9.0 lub nowszy
- Bot Discord z odpowiednimi uprawnieniami
- Serwer Discord z kanałem trigger



## 🚀 Instalacja

### 1. Sklonuj repozytorium

```
git  clone  https://github.com/twoja-nazwa/temporary-voice-bot.git
cd  temporary-voice-bot
```

  

### 2. Zainstaluj zależności

  

```
npm  install
```

### 3. Stwórz plik `.env` w głównym katalogu

  

```
BOT_TOKEN=twój_token_bota
GUILD_ID=id_twojego_serwera
TRIGGER_CHANNEL_ID=id_kanału_trigger
```
  

### 4. Struktura folderów


```
temporary-voice-bot/
├──  src/
│  └──  bot.js
├──  channels.json
└──  .env
```
  

## 🤖 Konfiguracja Bota

  

### 1. Utwórz Bota na Discord Developer Portal
-  Wejdź  na [Discord Developer  Portal](https://discord.com/developers/applications)
-  Kliknij  "New Application"  i  podaj  nazwę
-  Przejdź  do  zakładki  "Bot"
-  Kliknij  "Add Bot"  i  potwierdź
-  Skopiuj  **TOKEN**  -  będzie  potrzebny  do  pliku  `.env`

  

### 2. Włącz intenty
W  zakładce  "Bot"  włącz:
-  ✅  Presence  Intent
-  ✅  Server  Members  Intent
-  ✅  Message  Content  Intent

  

### 3. Zaproś Bota na serwer
W  zakładce  "OAuth2"  →  "URL Generator":
-  Wybierz  "bot"  i  "applications.commands"
-  Zaznacz  uprawnienia:
-  Manage  Channels
-  Move  Members
-  Connect
-  Speak
-  View  Channel
-  Manage  Roles
-  Skopiuj  wygenerowany  URL  i  otwórz  go  w  przeglądarce

  

### 4. Pobierz ID serwera i kanału
-  Włącz  **Tryb  Deweloperski**  w  Discord (Ustawienia →  Zaawansowane)
-  Kliknij  prawym  przyciskiem  na  serwer  →  "Kopiuj ID"
-  Kliknij  prawym  przyciskiem  na  kanał  trigger  →  "Kopiuj ID"




## 🎯 Uprawnienia Bota
Bot  wymaga  następujących  uprawnień:
-  `Manage Channels`  -  tworzenie  i  usuwanie  kanałów
-  `Move Members`  -  przenoszenie  użytkowników  między  kanałami
-  `Connect`  -  dołączanie  do  kanałów  głosowych
-  `Speak`  -  mówienie  na  kanałach
-  `View Channel`  -  widzenie  kanałów
-  `Manage Roles`  -  edycja  uprawnień  kanałów


  

## 🚀 Uruchomienie
```
node src/bot.js
```
Lub z użyciem nodemon (do rozwoju):
```
npm  install  -g  nodemon
nodemon  src/bot.js
```
  

 

## 📁 Struktura Plików
```temporary-voice-bot/
├──  src/
│  └──  bot.js  # Główny plik bota
├──  channels.json  # Plik z danymi właścicieli kanałów (tworzony automatycznie)
├──  .env  # Zmienne środowiskowe
├──  package.json  # Zależności
└──  README.md  # Ta dokumentacja
```

## 🔧 Zmienne Środowiskowe

  

|Zmienna|Opis|Przykład|
|--|--|--|
|`BOT_TOKEN`|Token  bota  Discord|`MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.G...`|
|`GUILD_ID`|ID  serwera  Discord|`123456789012345678`|
|`TRIGGER_CHANNEL_ID`|ID  kanału  trigger|`123456789012345678`|

  

----------

  

## 🎮 Jak używać

  

1.  **Dołącz  do  kanału  trigger**  -  Bot  automatycznie  utworzy  dla  Ciebie  kanał
2.  **Panel  zarządzania**  -  Po  utworzeniu  kanału  pojawi  się  embed  z  panelem
3.  **Zarządzanie  kanałem**  -  Użyj  menu  wyboru  aby:
-  Ustawić  limit  użytkowników
-  Zmienić  status  na  publiczny/prywatny
-  Zmienić  nazwę
-  Zmienić  opis
-  Przekazać  własność
-  Dodać/Usunąć  dostęp
-  Wyrzucić/Zablokować  użytkownika
-  Usunąć  kanał

## 📸 Panel zarządzania
```
🎤  Panel  twojego  kanału
👑  Właściciel:  @Użytkownik
🔊  Nazwa  kanału:  🎤  Nazwa
👥  Użytkownicy  na  kanale:  •  @User1  •  @User2
👤  Użytkownicy  z  dostępem:  🔒  Tylko  właściciel  ma  dostęp
ℹ️  Informacje:  •  Limit:  5  •  Status:  🔒  Prywatny
⚙️  Zarządzanie:  Użyj  menu  poniżej  aby  zarządzać  kanałem.
```

## 🛠️ Rozwiązywanie problemów

### Bot nie odpowiada

-  Sprawdź  czy  token  w  `.env`  jest  poprawny
-  Sprawdź  czy  bot  ma  odpowiednie  uprawnienia
-  Sprawdź  logi  w  konsoli
### Kanał nie tworzy się

-  Sprawdź  czy  `TRIGGER_CHANNEL_ID`  jest  poprawny
-  Sprawdź  czy  kanał  trigger  ma  ustawioną  kategorię (parent)
-  Sprawdź  czy  bot  ma  uprawnienie  `Manage Channels`

### Błąd "Aplikacja nie odpowiedziała na czas"

-  Bot  ma  wbudowane  `deferReply()` dla wolniejszych operacji
- Sprawdź połączenie internetowe
- Restart bota

## 📝 Licencja

MIT License - dowolne wykorzystanie

## 👨‍💻 Autor

Twoja Nazwa - [rAmfu](https://github.com/rAmfu)
  

## ⭐ Podziękowania

- [discord.js](https://discord.js.org/) - biblioteka Discord
- Wszystkim contributorom

**UWAGA:** Bot wymaga Node.js v16.9.0 lub nowszego!
