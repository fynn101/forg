import discord
import random
import datetime
import os


intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
 
    #greeting = "Hi everyone! I'm now online.\n\n`!cmd` to see commands"
    for guild in client.guilds:

        for channel in guild.text_channels:
        
            if channel.permissions_for(guild.me).send_messages:
        
            #    await channel.send(greeting)
                break

@client.event
async def on_message(message):
    async for prev_message in message.channel.history():

        if message.author == client.user:
            return

        if prev_message.content.lower() =='hi':
            await message.channel.send(f"HELLO {message.author.mention}! ")
            break
        
        elif prev_message.content.lower() == "-time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S PST")
            await message.channel.send(f"`The current time is {current_time}`")
            break

        elif prev_message.content.lower() == "-rng10":
            rng = random.randint(1,10)
            await message.channel.send(rng)
            break

        elif prev_message.content.lower() == "-rng100":
            rng = random.randint(1,100)
            await message.channel.send(rng)
            break 
    
        elif prev_message.content.lower() == "who\'s in paris":
            channel = message.channel
            guild = message.guild
            members = guild.members
            user = random.choice(members)
            if members:
                user = random.choice(members)
                await channel.send(f" {user.mention} is in Paris!")
            else:
                await channel.send(f" didn't work")
            break

        elif prev_message.content.lower() == "-frog":
            directory = os.path.join(os.getcwd(), "images", "frog")
            files = os.listdir(directory)
            file = random.choice(files)
            filepath = os.path.join(directory, file)
            with open(filepath, "rb") as f:
                image = discord.File(f)
                await message.channel.send(file=image)
            break

        elif prev_message.content.lower() == "-bunny":
            directory = os.path.join(os.getcwd(), "images", "bunny")
            files = os.listdir(directory)
            file = random.choice(files)
            filepath = os.path.join(directory, file)
            with open(filepath, "rb") as f:
                image = discord.File(f)
                await message.channel.send(file=image)
            break
              
        elif prev_message.content.lower() == "-cat":
            directory = os.path.join(os.getcwd(), "images", "cat")
            files = os.listdir(directory)
            file = random.choice(files)
            filepath = os.path.join(directory, file)
            with open(filepath, "rb") as f:
                image = discord.File(f)
                await message.channel.send(file=image)
            break

        elif prev_message.content == "!cmd":
            await message.channel.send(f"{message.author.mention} here are the cmds \n`-cat\n-frog\n-bunny\n-time\n-rng10\n-rng100`")
            break

        elif prev_message.content.lower() == "eng":
            rng = random.randint(1,8)
            if rng ==1 :
                await message.channel.send(f"{message.author.mention} you should be in `Civil Engineering`")
            elif rng ==2 :
                await message.channel.send(f"{message.author.mention} you should be in `Computer Engineering`")
            elif rng ==3 :
                await message.channel.send(f"{message.author.mention} you should be in `Electrical Engineering`")
            elif rng ==4 :
                await message.channel.send(f"{message.author.mention} you should be in `Geological Engineering`")
            elif rng ==5 :
                await message.channel.send(f"{message.author.mention} you should be in `Integrated Engineering`")
            elif rng ==6 :
                await message.channel.send(f"{message.author.mention} you should be in `Materials Engineering`")
            elif rng ==7 :
                await message.channel.send(f"{message.author.mention} you should be in `Mechanical Engineering`")
            elif rng ==8 :
                await message.channel.send(f"{message.author.mention} you should be in `Eng Pys`")
        
        elif prev_message.content.lower() == "l":
              await message.channel.send("Get Better + Ratio")
        else: 
            break
 
client.run('MTEwMzIwMzkyMTExNzMzNTU3Mg.GxogDL.0a34euRSJ8s72q386pn8wUITAdlSNYvSYhJHAQ')
