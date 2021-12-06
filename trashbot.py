import discord
import random
import time
import urllib.request
TOKEN = ""######INSERT YOUR TOKEN HERE TODO
client = discord.Client()
class hammer:
    hammer = 0
    dead = []
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        pass

    if message.content.startswith('!r.'): #ex. !r.3 -> 0, 1 or 2
        try:
            x = random.randrange(int(message.content[3:]))
            await message.channel.send(x)
        except:
            pass
    if message.content.startswith('!m.'): #ex. !m.2+2 -> 4]
        try:
            msg = eval(message.content[3:])
            await message.channel.send(msg)
        except:
            pass
    if message.content.startswith('!d.'): #define <word>. does not work perfectly
        word = message.content[3:]
        if word == "ura" or word == "URA":
            await message.channel.send("An imperialistic organisation")
        try:
            page = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/%s" % (word))
            page = str(page.read())
            ind = page.index("</strong>") + 9
            meaning = ""
            while page[ind] != '<':
                meaning += page[ind] 
                ind += 1
            await message.channel.send(meaning)
        except:
            pass
    if message.content.startswith("!w."): #gets a flag from wikipedia
        try:
            nation = message.content[3:]
            page = urllib.request.urlopen("https://en.wikipedia.org/wiki/%s" % nation)
            page = str(page.read())
            ind = page.index("/Flag")
            while page[ind] != '"':
                ind -= 1
            ind += 1
            cont = ""
            while page[ind] != '"':
                cont += page[ind]
                ind += 1
            if not cont.startswith("https"):
                cont = "https:" + cont
            await message.channel.send(cont)
        except:
            pass
    if message.content.startswith('!i.'): #NationStates information about nation
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
    if message.content.startswith('!f'): #!f.<team1 name>/<team2 name> -> simulates football match. use !f, (comma) for allowing extra time
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
        while t < 121:
            z = random.randrange(2)
            y = random.randrange(23)
            x = random.randrange(5)
            xx = random.randrange(5)
            if t == 46:
                story += ("Half time: %d - %d \n" % (points1, points2))
                game.append(story)
                story = ""
            if t == 91:
                if points1 != points2 or message.content[2] == ".":
                    break
                story += ("Full time: %d - %d \n" % (points1, points2))
                game.append(story)
                story = ""
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
                    if t > 90:
                        game.append(story)
                        break
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
        time.sleep(8)
        msg = '**Full Time:\n %s %d - %s %d **' % (teams[0], points1, teams[1], points2)
        await message.channel.send(msg)
    if message.content.startswith("!t."): #talks with the bot
        if message.content.endswith("?"):
            if random.randrange(2) == 1:
                await message.channel.send("Why do you hate the Anarcho-Monarchy Part and The Great Experiment?")
            else:
                await message.channel.send("I'm the one asking questions. Why do you not vote Anarcho-Monarchy?")
        elif message.content.endswith("!"):
            await message.channel.send("Aargh, for the love of the future monarch, do not scream so loud!")
                
        else:
            talk = random.randrange(6)
            if talk == 0:
                await message.channel.send("I'm so happy that you are a supporter of the Anarcho-Monarchy Party.")
            elif talk == 1:
                await message.channel.send("The Anarcho-Monarchy is the oldest of the current parties. It knows what it is talking about.")
            elif talk == 2:
                await message.channel.send("We need a monarchy to get things done. Like increasing activity, power and fun.")
            elif talk == 3:
                await message.channel.send("Freedom is an inherent right to all our members. It's wrong to be against it.")
            elif talk == 4:
                await message.channel.send("As a highly intelligent AI, I've come to the conclusion that the Anarcho-Monarchy Party is the best.")
            elif talk == 5:
                await message.channel.send("Some say I'm a propoaganda machine. I answer by saying they don't know about freedom. Anarcho-Monarchy!")
    if message.content.startswith("!work_in_soviet_factory."): #well yeah
        hammer.hammer += 1
        if message.author in hammer.dead:
            await message.channel.send("You are dead and shouldn't be able to work. But I guess this is the USSR after all...")
        await message.channel.send("You made a hammer. The state now has %d hammers." % (hammer.hammer))
        if hammer.hammer % random.randrange(1,6) == 0 and message.author not in hammer.dead:
            await message.channel.send("Later that day you died of the famine.")
            hammer.dead.append(message.author)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
