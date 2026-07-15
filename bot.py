import discord
from discord.ext import commands, tasks
from discord.ui import View, Button, Select, Modal, TextInput, UserSelect

import json
import os


# ==========================
# KONFIGURACJA
# ==========================

TOKEN = "TWOJ_DISCORD_TOKEN"

GUILD_ID = 659433731034972173

TRIGGER_CHANNEL_ID = 1438665251695624242

DATA_FILE = "channels.json"


# ==========================
# INTENTS
# ==========================

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ==========================
# STORAGE
# ==========================

def load_channels():
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def save_channels():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(channel_owner, file, indent=4)

# format: { "channel_id": owner_id }
channel_owner = load_channels()


# ==========================
# POMOCNICZE
# ==========================

def get_owner(channel_id):
    return channel_owner.get(str(channel_id))

def is_owner(user_id, channel_id):
    return get_owner(channel_id) == user_id

async def delete_channel(channel):
    if channel:
        try:
            await channel.delete()
        except Exception as e:
            print("Błąd usuwania:", e)
    
    channel_owner.pop(str(channel.id), None)
    save_channels()


# ==========================
# PRZYCISK ODŚWIEŻANIA
# ==========================

class RefreshButton(Button):
    def __init__(self, channel_id):
        super().__init__(
            label="🔄 Odśwież",
            style=discord.ButtonStyle.secondary,
            custom_id=f"refresh_{channel_id}"
        )
        self.channel_id = channel_id
    
    async def callback(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(self.channel_id)
        if not channel:
            return await interaction.response.send_message(
                "❌ Kanał nie istnieje!",
                ephemeral=True
            )
        
        owner_id = get_owner(self.channel_id)
        owner = interaction.guild.get_member(int(owner_id)) if owner_id else None
        
        if not owner:
            owner = interaction.user
        
        is_owner = interaction.user.id == int(owner_id) if owner_id else False
        
        embed = await create_embed(channel, owner)
        view = ChannelPanel(owner_id, self.channel_id, is_owner)
        await interaction.response.edit_message(embed=embed, view=view)


# ==========================
# PANEL GŁÓWNY
# ==========================

class ChannelPanel(View):
    def __init__(self, owner_id, channel_id, is_owner=True):
        super().__init__(timeout=None)
        if is_owner:
            self.add_item(ChannelManager(owner_id, channel_id))
        self.add_item(RefreshButton(channel_id))


# ==========================
# MENU ZARZĄDZANIA
# ==========================

class ChannelManager(Select):
    def __init__(self, owner_id, channel_id):
        options = [
            discord.SelectOption(label="Limit użytkowników", emoji="👥", value="limit"),
            discord.SelectOption(label="Prywatny / Publiczny", emoji="🔒", value="privacy"),
            discord.SelectOption(label="Zmiana nazwy", emoji="✏️", value="rename"),
            discord.SelectOption(label="Zmień opis", emoji="📝", value="description"),
            discord.SelectOption(label="Przekaż właściciela", emoji="👑", value="transfer"),
            discord.SelectOption(label="Wyrzuć użytkownika", emoji="🚪", value="kick"),
            discord.SelectOption(label="Zablokuj użytkownika", emoji="🚫", value="ban"),
            discord.SelectOption(label="Odblokuj użytkownika", emoji="🔓", value="unban"),
            discord.SelectOption(label="Usuń kanał", emoji="🗑️", value="delete")
        ]
        
        super().__init__(
            placeholder="⚙️ Zarządzanie kanałem",
            options=options,
            custom_id=f"channel_manager_{channel_id}"
        )
        self.owner_id = owner_id
        self.channel_id = channel_id

    async def callback(self, interaction: discord.Interaction):
        current_owner = get_owner(self.channel_id)
        if interaction.user.id != int(current_owner) if current_owner else None:
            return await interaction.response.send_message(
                "❌ Nie jesteś właścicielem kanału!",
                ephemeral=True
            )
        
        option = self.values[0]
        await handle_action(interaction, option, int(current_owner), self.channel_id)


# ==========================
# LIMIT MODAL
# ==========================

class LimitModal(Modal):
    def __init__(self, channel_id):
        super().__init__(title="Ustaw limit użytkowników", custom_id=f"limit_modal_{channel_id}")
        self.channel_id = channel_id
        
        self.limit_input = TextInput(
            label="Limit użytkowników",
            placeholder="Wpisz liczbę (0 = bez limitu, max 99)",
            min_length=1,
            max_length=2,
            required=True
        )
        self.add_item(self.limit_input)
    
    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(self.channel_id)
        if not channel:
            return await interaction.response.send_message(
                "❌ Kanał nie istnieje!",
                ephemeral=True
            )
        
        try:
            limit = int(self.limit_input.value)
            
            if limit < 0:
                return await interaction.response.send_message(
                    "❌ Limit nie może być ujemny!",
                    ephemeral=True
                )
            if limit > 99:
                return await interaction.response.send_message(
                    "❌ Limit nie może być większy niż 99!",
                    ephemeral=True
                )
            
            await channel.edit(user_limit=limit)
            
            owner_id = get_owner(self.channel_id)
            owner = interaction.guild.get_member(int(owner_id)) if owner_id else None
            if owner:
                embed = await create_embed(channel, owner)
                await interaction.response.edit_message(embed=embed)
            
            await interaction.followup.send(
                f"👥 Limit ustawiony: {limit if limit else 'bez limitu'}",
                ephemeral=True
            )
            
        except ValueError:
            await interaction.response.send_message(
                "❌ To nie jest poprawna liczba!",
                ephemeral=True
            )


# ==========================
# ZMIANA NAZWY
# ==========================

class RenameModal(Modal):
    def __init__(self, channel_id):
        super().__init__(title="Zmień nazwę kanału", custom_id=f"rename_{channel_id}")
        self.channel_id = channel_id
        self.name = TextInput(
            label="Nowa nazwa",
            placeholder="np. Kanał Rafała",
            max_length=50,
            required=True
        )
        self.add_item(self.name)

    async def on_submit(self, interaction: discord.Interaction):
        current_owner = get_owner(self.channel_id)
        if interaction.user.id != int(current_owner) if current_owner else None:
            return await interaction.response.send_message(
                "❌ Nie jesteś właścicielem!",
                ephemeral=True
            )
        
        channel = interaction.guild.get_channel(self.channel_id)
        if channel:
            await channel.edit(name=self.name.value)
            await update_panel(channel)
        
        await interaction.response.send_message("✏️ Nazwa kanału zmieniona.", ephemeral=True)


# ==========================
# ZMIANA OPISU
# ==========================

class DescriptionModal(Modal):
    def __init__(self, channel_id):
        super().__init__(title="Zmień opis kanału", custom_id=f"description_{channel_id}")
        self.channel_id = channel_id
        
        self.description = TextInput(
            label="Nowy opis",
            placeholder="np. Kanał dla przyjaciół",
            max_length=100,
            required=False,
            style=discord.TextStyle.paragraph
        )
        self.add_item(self.description)
    
    async def on_submit(self, interaction: discord.Interaction):
        current_owner = get_owner(self.channel_id)
        if interaction.user.id != int(current_owner) if current_owner else None:
            return await interaction.response.send_message(
                "❌ Nie jesteś właścicielem!",
                ephemeral=True
            )
        
        channel = interaction.guild.get_channel(self.channel_id)
        if channel:
            description_data[str(self.channel_id)] = self.description.value.strip()
            await update_panel(channel)
        
        await interaction.response.send_message(
            f"📝 Opis zaktualizowany!" if self.description.value.strip() else "📝 Opis usunięty!",
            ephemeral=True
        )


# ==========================
# WYBÓR UŻYTKOWNIKA
# ==========================

class UserSelectDropdown(UserSelect):
    def __init__(self, owner_id, channel_id, action):
        super().__init__(
            placeholder="Wybierz użytkownika",
            min_values=1,
            max_values=1,
            custom_id=f"user_select_{channel_id}_{action}"
        )
        self.owner_id = owner_id
        self.channel_id = channel_id
        self.action = action

    async def callback(self, interaction: discord.Interaction):
        current_owner = get_owner(self.channel_id)
        if interaction.user.id != int(current_owner) if current_owner else None:
            return await interaction.response.send_message(
                "❌ Nie jesteś właścicielem!",
                ephemeral=True
            )

        user = self.values[0]
        channel = interaction.guild.get_channel(self.channel_id)
        
        if not channel:
            return await interaction.response.send_message(
                "❌ Kanał nie istnieje!",
                ephemeral=True
            )

        if self.action == "kick":
            if user.voice and user.voice.channel == channel:
                await user.move_to(None)
                msg = f"🚪 Wyrzucono {user.mention}"
            else:
                msg = "❌ Użytkownik nie jest na kanale."

        elif self.action == "ban":
            if user.id == interaction.user.id:
                return await interaction.response.send_message(
                    "❌ Nie możesz zablokować siebie!",
                    ephemeral=True
                )
            
            await channel.set_permissions(user, connect=False)
            if user.voice and user.voice.channel == channel:
                await user.move_to(None)
            msg = f"🚫 Zablokowano {user.mention}"

        elif self.action == "unban":
            await channel.set_permissions(user, overwrite=None)
            msg = f"🔓 Odblokowano {user.mention}"

        elif self.action == "transfer":
            if user.id == interaction.user.id:
                return await interaction.response.send_message(
                    "❌ Nie możesz przekazać właściciela sobie!",
                    ephemeral=True
                )
            
            old_owner = interaction.guild.get_member(self.owner_id)
            new_owner = user

            channel_owner[str(self.channel_id)] = new_owner.id
            save_channels()

            if old_owner:
                await channel.set_permissions(old_owner, overwrite=None)
            
            await channel.set_permissions(
                new_owner,
                manage_channels=True,
                connect=True,
                view_channel=True
            )

            msg = f"👑 Właścicielem został {new_owner.mention}"
            
            embed = await create_embed(channel, new_owner)
            
            try:
                async for message in channel.history(limit=10):
                    if message.author == bot.user and message.embeds:
                        new_view = ChannelPanel(new_owner.id, self.channel_id, True)
                        await message.edit(embed=embed, view=new_view)
                        break
            except Exception as e:
                print("Błąd aktualizacji embed:", e)

        await interaction.response.send_message(msg, ephemeral=True)


class UserActionView(View):
    def __init__(self, owner_id, channel_id, action):
        super().__init__(timeout=60)
        self.add_item(UserSelectDropdown(owner_id, channel_id, action))


# ==========================
# OBSŁUGA MENU
# ==========================

async def handle_action(interaction, action, owner_id, channel_id):
    if action == "limit":
        return await interaction.response.send_modal(LimitModal(channel_id))

    if action == "privacy":
        channel = interaction.guild.get_channel(channel_id)
        role = interaction.guild.default_role
        
        overwrite = channel.overwrites_for(role)
        
        if overwrite.connect is False:
            await channel.set_permissions(role, connect=True, view_channel=True)
            msg = "🔓 Kanał publiczny"
        else:
            await channel.set_permissions(role, connect=False, view_channel=False)
            msg = "🔒 Kanał prywatny"
        
        await update_panel(channel)
        return await interaction.response.send_message(msg, ephemeral=True)

    if action == "rename":
        return await interaction.response.send_modal(RenameModal(channel_id))
    
    if action == "description":
        return await interaction.response.send_modal(DescriptionModal(channel_id))

    if action in ["kick", "ban", "unban", "transfer"]:
        return await interaction.response.send_message(
            "👤 Wybierz użytkownika:",
            view=UserActionView(owner_id, channel_id, action),
            ephemeral=True
        )

    if action == "delete":
        # NAJPIERW wysyłamy odpowiedź
        await interaction.response.send_message("🗑️ Kanał został usunięty.", ephemeral=True)
        
        # POTEM usuwamy kanał
        channel = interaction.guild.get_channel(channel_id)
        if channel:
            await delete_channel(channel)
        
        return


# ==========================
# PRZECHOWYWANIE OPISÓW
# ==========================

description_data = {}

def get_description(channel_id):
    return description_data.get(str(channel_id), "")


# ==========================
# TWORZENIE EMBED
# ==========================

async def create_embed(channel, owner):
    """Tworzy embed z informacjami o kanale"""
    embed = discord.Embed(
        title="🎤 Panel twojego kanału",
        description="Tutaj możesz zarządzać swoim prywatnym kanałem.",
        color=discord.Color.green()
    )
    
    # Dodajemy opis jeśli istnieje
    channel_desc = get_description(channel.id)
    if channel_desc:
        embed.description = channel_desc
    
    # Liczba osób na kanale
    members_list = "\n".join([f"• {member.mention}" for member in channel.members[:10]])
    if len(channel.members) > 10:
        members_list += f"\n... i {len(channel.members) - 10} więcej"
    elif not channel.members:
        members_list = "🔇 Brak użytkowników"
    
    embed.add_field(
        name="👑 Właściciel",
        value=owner.mention,
        inline=True
    )
    
    embed.add_field(
        name="🔊 Nazwa kanału",
        value=f"`{channel.name}`",
        inline=True
    )
    
    embed.add_field(
        name="👥 Użytkownicy",
        value=members_list,
        inline=False
    )
    
    # Informacje o kanale
    info = f"• Limit: {channel.user_limit if channel.user_limit else 'Brak'}\n"
    
    role = channel.guild.default_role
    overwrite = channel.overwrites_for(role)
    is_public = overwrite.connect is not False
    info += f"• Status: {'🔓 Publiczny' if is_public else '🔒 Prywatny'}"
    
    embed.add_field(
        name="ℹ️ Informacje",
        value=info,
        inline=False
    )
    
    embed.add_field(
        name="⚙️ Zarządzanie",
        value="Użyj menu poniżej aby zarządzać kanałem.",
        inline=False
    )
    
    embed.set_footer(text="Temporary Voice System | Kliknij Odśwież aby zaktualizować")
    
    return embed


# ==========================
# WYSYŁANIE PANELU
# ==========================

async def create_panel(channel, owner, description=""):
    if description:
        description_data[str(channel.id)] = description
    embed = await create_embed(channel, owner)
    await channel.send(embed=embed, view=ChannelPanel(owner.id, channel.id, True))


# ==========================
# FUNKCJA AKTUALIZACJI PANELU
# ==========================

async def update_panel(channel):
    """Aktualizuje panel w kanale"""
    owner_id = get_owner(channel.id)
    if not owner_id:
        return
    
    owner = channel.guild.get_member(int(owner_id))
    if not owner:
        return
    
    embed = await create_embed(channel, owner)
    
    try:
        async for message in channel.history(limit=10):
            if message.author == bot.user and message.embeds:
                view = ChannelPanel(owner.id, channel.id, True)
                await message.edit(embed=embed, view=view)
                break
    except Exception as e:
        print("Błąd aktualizacji panelu:", e)


# ==========================
# FUNKCJA TWORZENIA KANAŁU
# ==========================

creating_channels = set()

async def create_voice_channel(member):
    """Tworzy kanał głosowy dla członka"""
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return False
    
    trigger = guild.get_channel(TRIGGER_CHANNEL_ID)
    if not trigger:
        return False
    
    # Sprawdzenie czy już posiada kanał
    for cid, owner in channel_owner.items():
        if owner == member.id:
            return False
    
    if member.id in creating_channels:
        return False
    
    creating_channels.add(member.id)
    
    try:
        category = trigger.category
        if not category:
            return False
        
        channel = await category.create_voice_channel(
            name=f"🎤 {member.display_name}",
            bitrate=96000,
            user_limit=0
        )
        
        channel_owner[str(channel.id)] = member.id
        save_channels()
        
        await channel.set_permissions(
            member,
            connect=True,
            view_channel=True,
            manage_channels=True
        )
        
        await member.move_to(channel)
        await create_panel(channel, member)
        
        return True
        
    except Exception as e:
        print("Błąd tworzenia kanału:", e)
        return False
        
    finally:
        creating_channels.discard(member.id)


# ==========================
# PĘTLA TWORZENIA KANAŁÓW
# ==========================

@tasks.loop(seconds=3)
async def voice_creator():
    """Sprawdza czy ktoś jest w kanale trigger i tworzy dla niego kanał"""
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return

    trigger = guild.get_channel(TRIGGER_CHANNEL_ID)
    if not trigger:
        return

    for member in trigger.members:
        if member.bot:
            continue
        
        # Sprawdzenie czy już posiada kanał
        exists = False
        for cid, owner in channel_owner.items():
            if owner == member.id:
                exists = True
                break
        
        if not exists and member.id not in creating_channels:
            await create_voice_channel(member)


# ==========================
# CZYSZCZENIE KANAŁÓW
# ==========================

@tasks.loop(seconds=15)
async def clear_empty_channels():
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return

    for channel_id in list(channel_owner.keys()):
        channel = guild.get_channel(int(channel_id))
        
        if not channel:
            channel_owner.pop(channel_id, None)
            description_data.pop(channel_id, None)
            save_channels()
            continue

        if len(channel.members) == 0:
            description_data.pop(channel_id, None)
            await delete_channel(channel)


# ==========================
# VOICE STATE UPDATE
# ==========================

@bot.event
async def on_voice_state_update(member, before, after):
    """Wywoływane gdy ktoś zmienia kanał głosowy"""
    
    # Sprawdzenie czy ktoś wszedł do kanału trigger
    if after.channel and after.channel.id == TRIGGER_CHANNEL_ID:
        # Sprawdzenie czy już posiada kanał
        exists = False
        for cid, owner in channel_owner.items():
            if owner == member.id:
                exists = True
                break
        
        if not exists and member.id not in creating_channels:
            await create_voice_channel(member)
    
    # Sprawdzenie czy ktoś wyszedł z kanału i czy był to kanał tymczasowy
    if before.channel:
        if str(before.channel.id) in channel_owner:
            if len(before.channel.members) == 0:
                description_data.pop(str(before.channel.id), None)
                await delete_channel(before.channel)
            else:
                await update_panel(before.channel)
    
    # Jeśli ktoś wszedł do kanału tymczasowego, aktualizujemy panel
    if after.channel:
        if str(after.channel.id) in channel_owner:
            await update_panel(after.channel)


# ==========================
# READY
# ==========================

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

    # odtworzenie paneli po restarcie
    for channel_id, owner_id in channel_owner.items():
        guild = bot.get_guild(GUILD_ID)
        if guild:
            channel = guild.get_channel(int(channel_id))
            if channel:
                view = ChannelPanel(owner_id, int(channel_id), True)
                bot.add_view(view)

    # Uruchomienie pętli
    if not voice_creator.is_running():
        voice_creator.start()

    if not clear_empty_channels.is_running():
        clear_empty_channels.start()
    
    print("✅ System tymczasowych kanałów jest gotowy!")


# ==========================
# START
# ==========================

if __name__ == "__main__":
    bot.run(TOKEN)
