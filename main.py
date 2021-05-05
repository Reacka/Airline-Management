import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game(";help")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    mile=0;
    km=0;


    if message.content.startswith(";airline status"):
        await message.channel.send("total pilots: 8\nDistance Flown: 0\nTotal flights flown: 0")

    if message.content.startswith(";help"):
        await message.channel.send("```;airline status: Show total info of airline \n```")

    if message.content.startswith(";distance calculate %d miles", mile):
        await message.channel.send(int(mile) * 1.852)








client.run("ODM5MzIxOTMyMjgwNzU4MzAy.YJH9dg.2BIaoyrsLWKzzenVn17tkchkIEo")