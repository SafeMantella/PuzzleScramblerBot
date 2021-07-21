import discord
import random
import pycuber as pc

#put your discord token here
DISCORD_TOKEN = ''

client = discord.Client() #bota o bot online
print("bot on")

def convert_list_to_string(org_list, seperator=' '):
    return seperator.join(org_list)

# function from https://github.com/BenGotts/Python-Rubiks-Cube-Scrambler/blob/master/scrambleGenerator.py
def Scramble():
    moves = ["U", "D", "F", "B", "R", "L"]
    dir = ["", "'", "2"]
    slen = random.randint(25, 28)

    def gen_scramble():
        s = validate([[random.choice(moves), random.choice(dir)] for x in range(slen)])
        return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) , "[" + str(slen) + "]"

    def validate(ar):
        for x in range(1, len(ar)):
            while ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
        for x in range(2, len(ar)):
            while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
        return ar
    
    return gen_scramble()

@client.event
async def on_message(message):
    message.content = message.content.lower()

    #stops bot from calling himself
    if message.author == client.user:
        return
    
    #scramble and embed generator
    if message.content.startswith("!scramble") or message.content.startswith("!cube"):
        scramble = Scramble()
        print(scramble[0])
        print(scramble[1])
        
        mycube = pc.Cube()
        mycube(scramble[0])
        
        mycube = str(mycube)
        mycube = mycube.replace("[o]", ":orange_square:")
        mycube = mycube.replace("[r]", ":red_square:")
        mycube = mycube.replace("[y]", ":yellow_square:")
        mycube = mycube.replace("[b]", ":blue_square:")
        mycube = mycube.replace("[g]", ":green_square:")
        mycube = mycube.replace("[w]", ":white_large_square:")
        mycube = mycube.replace("   ", ":black_large_square:")

        #embed
        embed = discord.Embed(title=scramble[0] + scramble[1], url="", description=mycube, color=discord.Color.green())
        await message.channel.send("**" + scramble[0] + "**" + "\n" + scramble[1] + "\n" + mycube)


client.run(DISCORD_TOKEN)
