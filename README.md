# 🎤 Bot do Tymczasowych Kanałów Głosowych

Bot Discord, który automatycznie tworzy i zarządza tymczasowymi kanałami głosowymi z pełnym panelem zarządzania.

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
git clone https://github.com/twoja-nazwa/temp-voice-bot.git
cd temp-voice-bot
