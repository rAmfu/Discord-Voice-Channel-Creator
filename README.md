# Discord Server Manager Bot

Bot Discord do podstawowego zarządzania serwerem, w tym ping, kick, ban i przywitaj nowych użytkowników.

## Instalacja

1. Skopiuj `.env.example` do `.env`
2. Uzupełnij `BOT_TOKEN` w pliku `.env`
3. Uruchom `npm install`
4. Uruchom `npm start`

## Komendy

- `!ping` - sprawdza opóźnienie bota
- `!kick @user [powód]` - wyrzuca użytkownika (wymaga uprawnień Kick Members)
- `!ban @user [powód]` - banuje użytkownika (wymaga uprawnień Ban Members)
- `!help` - wyświetla listę komend

## Konfiguracja

Plik `.env` powinien zawierać:

```
BOT_TOKEN=twoj_token_bota
PREFIX=!
GUILD_ID=twoj_id_serwera
TRIGGER_CHANNEL_ID=id_kanalu_trigger
```

## Uwagi

Bot wymaga uprawnień do czytania wiadomości, wysyłania wiadomości oraz zarządzania członkami, aby w pełni działać.
