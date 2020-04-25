import discord
import random
import time
import urllib.request
TOKEN = #your token
client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        pass

    if message.content.startswith('!r.'):
        try:
            x = random.randrange(int(message.content[3:]))
            await message.channel.send(x)
        except:
            pass
    if message.content.startswith('!m.'):
        try:
            msg = eval(message.content[3:])
            await message.channel.send(msg)
        except:
            pass
    if message.content.startswith('!i.'):
        nation = message.content[3:]
        nation = nation.replace(" ", "_")
        nation = nation.lower()
        try:
            page = urllib.request.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?nation=%s&q=fullname+region+category+motto+tax+capital+currency+leader+wa+flag" % nation)
            page = str(page.read())
            name = page[page.index("E>")+2:page.index("/FU")-1]
            category = page[page.index("RY>")+3:page.index("/CAT")-1]
            region = page[page.index("N>")+2:page.index("/R")-1]
            motto = page[page.index("O>")+2:page.index("/M")-1]
            capital = page[page.index("L>")+2:page.index("/CAP")-1]
            currency = page[page.index("CY>")+3:page.index("/CU")-1]
            tax = page[page.index("X>")+2:page.index("/T")-1]
            leader = page[page.index("R>")+2:page.index("/L")-1]
            wa = page[page.index("S>")+2:page.index("/U")-1]
            flag = page[page.index("G>")+2:page.index("/FL")-1]
            msg = "```Name: %s\nCategory: %s\nRegion: %s\nMotto: %s\nCapital: %s\nCurrency: %s\nLeader: %s\nTax: %s\nWA: %s```\n%s" % (name, category, region, motto, capital, currency, leader, tax, wa, flag)
            await message.channel.send(msg)
        except:
            pass
    if message.content.startswith('!f.'):
        teams = []
        post = message.content[3:]
        a = 0
        name = ""
        while post[a] != "/":
            name += post[a]
            a += 1
        teams.append(name + ", ")
        teams.append(post[a+1:] + ", ")
        events = ["Nice passing play,", "Nice passing play,", "Nice passing play,", "Long shot,", "Long shot,", "Long shot,", "Cross,", "Cross,", "Wait, what happens,",
          "Freekick,", "Freekick,", "Penalty,", "Corner,", "Corner,", "Corner,", "Free against the keeper,", "Beautifully,", "Fancy footwork leads to a shot,", "Cross comes in from the wing,", "Ball is aimed to the corner of the net,", "Long curved shot,", "Quick passing play,", "Quick move and strong shot,"]
        story = ""
        points1 = 0
        points2 = 0
        t = 0
        game = []
        while t < 91:
            z = random.randrange(2)
            y = random.randrange(23)
            x = random.randrange(5)
            xx = random.randrange(5)
            if t == 46:
                story += ("Half time: %d - %d \n" % (points1, points2))
                game.append(story)
                story = ""
            """if t == 91:
                story += ("Full time: %d - %d \n" % (points1, points2))
                game.append(story)
                if points1 != points2:
                    t = 121
                    continue"""
            if x == 0:
                story += str(t) + " minute, " + teams[z] + events[y]
                if y == 11 and random.randrange(2) == 0:
                    xx = 0
                if xx == 0:
                    story += " GOAL!\n"
                    if z == 0:
                        points1 += 1
                    else:
                        points2 += 1
                    story += str(points1) + " - " + str(points2) + "\n"
                else:
                    if random.randrange(2) == 0:
                        story += " Save\n"
                    else:
                        story += " Miss\n"
            else:
                t += 1
                continue
            game.append(story)
            story = ""
            t += 1
        for cell in game:
            time.sleep(8)
            await message.channel.send(cell)
        msg = '**Full Time:\n %s %d -- %s %d **' % (teams[0], points1, teams[1], points2)
        await message.channel.send(msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
