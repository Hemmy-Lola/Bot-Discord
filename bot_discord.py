!pip install discord.py
!pip install nest_asyncio 
import nest_asyncio 
nest_asyncio.apply() 

import discord

intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_member_join(member):
  general_channel = client.get_channel(1051551724579606630)
  await general_channel.send("https://tenor.com/view/kidnap-kid-brother-grab-bootloon-gif-22467768")
  await general_channel.send("*Bienvenue dans Treasure Hunter * "+ member.name + "! *écris* - toc toc toc - *pour commencer*")

score_global = 0
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message.content = message.content.lower()

  if message.content.startswith("toc toc toc"):
    await message.channel.send("https://tenor.com/view/where-is-the-library-gif-20023724")
    await message.channel.send("*As-tu entendus parler de ce coffre au trésor insaisissable ? \n Il y a des décennies, John McSlingy et ses frères, célèbres enfants d'un grand explorateur, se voient après le décès de ce dernier, devoir partager sa fortune. \n Hélas, John étant trop égoïste, préfèra se diviser de ses frères pour obtenir la fortune totale de leur père. \n Il se fait alors renommer 'McStingy' pour son orgueil et sa radinerie. \n Il jugera même qu'après sa mort, personne ne prendra sa fortune qu'il a  pris soin de seller d'un code secret. \n Personne jusqu'ici n'a alors réussi à mettre la main sur ce coffre. \n Seras-tu la première personne à le découvrir...?* \n Ecris - GO - si tu veux rentrer dans le jeu.")
  
  if message.content == "go":
    await message.channel.send("*Veux-tu que je t'explique les règles du jeu ?* \n Ecris - OUI - si tu veux les règles ou - NON - si tu veux directement commencer le jeu.")

  if message.content == "oui":
    await message.channel.send("https://drive.google.com/file/d/17fl1rOpdqlm-MQ_p9mshiu9JaeTKNkTk/view?usp=sharing")
    await message.channel.send("*Voici le parchemin t'expliquant notre mission. Lorsque tu es prêt, saisi* - PLAY - *pour que nous puissions commencer.*")
    
  if message.content == "non":
    await message.channel.send("écris - PLAY - pour commencer")

  if message.content == "play":
    
    score_total = 0
    score_global = score_total
    score_manche = 0
    j = 0
    while j!= 6:

      if j == 0:
        score_total = 0
        questions = []
        questions.append(":thought_balloon: Sanaa *est ma capitale.*")
        questions.append("*:thought_balloon: Serais-tu prêt à chanter avec moi sur cette chanson ?:* - O'zbekiston Respublikasining Davlat Madhiyasi - https://drive.google.com/file/d/1k3RoM4FZZsWQkN3k6_mPzFVTZKcJKHqe/view?usp=sharing")
        questions.append("*:thought_balloon: J'ai pris mon indépendance du Royaume-Uni le 1 octobre 1960...*")
        questions.append("*:thought_balloon: Si je te disais* - 19°00'N, 72°25'W -")
        questions.append("*:thought_balloon: Connais-tu* Teofilo Braga ?")
        questions.append("*:thought_balloon: 1 euro = 2459.99 Shilling-T...*")

        reponses = []
        reponses.append("yemen")
        reponses.append("ouzbékistan")
        reponses.append("nigéria")
        reponses.append("haïti")
        reponses.append("portugal")
        reponses.append("tanzanie")

        indices = []
        indices.append("*Et si nous allions faire un tour au Moyen Orient...?*")
        indices.append("*Il s'agit de mon hymne nationale...*")
        indices.append("*Une autre annecdote sur moi est ue j'abrite le plus grand réseau routier d'Afrique de l'Ouest...*")
        indices.append("*Aide toi d'une carte pour me localiser...*")
        indices.append("*Il a été le premier président à me gouverner*")
        indices.append("*Il s'agit de la monnaie de mon pays*")

        transitions = []
        transitions.append("*Je pense que tu commences à comprendre les règles du jeu ! Passons à la deuxième en route pour la prochaine destination...*")
        transitions.append("*Passons à la troisième énigme...*")
        transitions.append("*changeons de cape...*")
        transitions.append("*Passons à la quatrième énigme...*")
        transitions.append("*On approche du but, voilà la cinquième destination...*")
        transitions.append("*Nous voici arrivé à notre destination finale !* \n *Tu as débloqué les lettres suivantes* : :regional_indicator_y:, :regional_indicator_n:, :regional_indicator_o:, :regional_indicator_p:, :regional_indicator_h:, :regional_indicator_t:")

        lettres = []
        lettres.append(":regional_indicator_y:")
        lettres.append(":regional_indicator_o:")
        lettres.append(":regional_indicator_n:")
        lettres.append(":regional_indicator_h:")
        lettres.append(":regional_indicator_p:")
        lettres.append(":regional_indicator_t:")

        transition_avion = []
        transition_avion.append("https://tenor.com/view/plane-avion-ciel-sky-cloud-gif-20391427")
        transition_avion.append("https://tenor.com/view/delta-airplane-delta-airlines-flying-gif-25292527")
        transition_avion.append("https://tenor.com/view/lumipad-camille-viceral-eroplano-nasa-ere-biyahe-gif-17421000")
        transition_avion.append("https://tenor.com/view/a220-aircraft-flying-fast-airplane-gif-14629611")
        transition_avion.append("https://tenor.com/view/korean-air-airplane-fly-gif-7267685")
        transition_avion.append("https://tenor.com/view/plane-airplane-boeing-boeing787-butter-gif-18225611")

      await message.channel.send(questions[0])


      a = await client.wait_for("message")
      a.content = a.content.lower()
      i = 3
      while reponses[0] not in a.content:
        if i>0:
          if a.content == "restart":
            await message.channel.send("Êtes-vous sûr de recommencer ? Ecris - RECOMMENCER - si c'est bien le cas. \n Tu recommenceras au début des questions, et ton score recommenceras égalementau départ. \n Ou continue tout simplement le jeu en répondant au question.")
            a = await client.wait_for("message")
            a.content = a.content.lower()
            if a.content == "recommencer":
              j = 0
              break

          elif a.content == "score":
            await message.channel.send(score_total)
            a = await client.wait_for("message")
            a.content = a.content.lower()
          elif a.content == "indice":
            await message.channel.send(indices[0])
            a = await client.wait_for("message")
            a.content = a.content.lower()
            score_total = score_total - 10
          else:
            await message.channel.send("essaie encore")
            a = await client.wait_for("message")
            a.content = a.content.lower()
            i = i - 1
            score_total = score_total - 5
        else:
          a.content = reponses[0]
          break
          
      if reponses[0] in a.content:
        if i==3:
          await message.channel.send("https://tenor.com/view/oscars-standing-ovation-clap-clapping-applause-gif-20292436")
          await message.channel.send("*BRAVO !!!* :star_struck: \n + 30 points !")
          await message.channel.send(" ->Tu débloques la lettre")
          await message.channel.send(lettres[0])
          await message.channel.send(transitions[0])
          await message.channel.send(transition_avion[0])
          del questions[0]
          del reponses[0]
          del indices[0]
          del lettres[0]
          del transitions[0]
          del transition_avion[0]
          j = j + 1
          score_manche = 30
          score_total = score_total + score_manche
          
        

        if i==2:
          await message.channel.send("https://tenor.com/view/the-wolf-of-wall-street-clap-clapping-clapping-hands-leonardo-dicaprio-gif-22829304")
          await message.channel.send("*BIEN JOUE !!* :partying_face: \n + 20 points !")
          await message.channel.send(" ->Tu débloques la lettre ")
          await message.channel.send(lettres[0])
          await message.channel.send(transitions[0])
          await message.channel.send(transition_avion[0])
          del questions[0]
          del reponses[0]
          del indices[0]
          del lettres[0]
          del transitions[0]
          del transition_avion[0]
          j = j + 1
          score_manche = 20
          score_total = score_total + score_manche
          
          
          
        
        if i==1:
          await message.channel.send("https://tenor.com/view/bravo-clap-clapping-applause-amazed-gif-16646029") 
          await message.channel.send("*PAS MAL !* :stuck_out_tongue_closed_eyes: \n + 10 points !")
          await message.channel.send(" ->Tu débloques la lettre ")
          await message.channel.send(lettres[0])
          await message.channel.send(transitions[0])
          await message.channel.send(transition_avion[0])
          del questions[0]
          del reponses[0]
          del indices[0]
          del lettres[0]
          del transitions[0]
          del transition_avion[0]
          j = j + 1
          score_manche = 10
          score_total = score_total + score_manche
          
        
        if i==0:
          await message.channel.send("https://tenor.com/view/sigh-facepalm-stressed-disappointed-bored-gif-17570669")
          await message.channel.send("*OUPS...perdu...* :face_with_peeking_eye: la réponse était "+ reponses[0])
          await message.channel.send(" ->Tu débloques la lettre ")
          await message.channel.send(lettres[0])
          await message.channel.send(transitions[0])
          await message.channel.send(transition_avion[0])
          del questions[0]
          del reponses[0]
          del indices[0]
          del lettres[0]
          del transitions[0]
          del transition_avion[0]
          j = j + 1
          score_manche = 0
          score_total = score_total + score_manche
          
    question_finale = ["*entre le code secret*"]
    reponse_finale = ["python"]
    indice_final = ["sais-tu maîtriser ce langage...?"]

    await message.channel.send("votre score actuel est de:")
    await message.channel.send(score_total)
    await message.channel.send("Quel est le fameux mot mystère ?")
    await message.channel.send(question_finale[0])
  
    a = await client.wait_for("message")
    a.content = a.content.lower()
    while reponse_finale[0] not in a.content:
      if score_total> 0:
        if a.content == "indice final":
          await message.channel.send(indice_final[0])
          a = await client.wait_for("message")
          a.content = a.content.lower()
          score_total = score_total - 20
        elif a.content == "score":
            await message.channel.send(score_total)
            a = await client.wait_for("message")
            a.content = a.content.lower()
        
        else:
          await message.channel.send("essaie encore")
          a = await client.wait_for("message")
          a.content = a.content.lower()
          score_total = score_total - 15
      else:
        break

    if score_total > 0:
      await message.channel.send("https://tenor.com/view/ninjala-ninjala-season6trailer-ninjala-season6-season6trailer-season6-gif-22070682")
      await message.channel.send("FELICITATIONS !!! LE COFFRE EST OUVERT !!! TU AS REUSSI")
      await message.channel.send("https://tenor.com/view/money-angel-winning-heaven-gif-10564478")
      await message.channel.send("Vous avez obtenu un score final de")
      await message.channel.send(score_total)
      await message.channel.send("*fin du jeu.*")
      await message.channel.send("*co.fondateurs : PINEAU Adrien, PETRIC Romario, MANZEYI Emmanuel et MATHYS Hemmy-Lola*")
    
    else:
      await message.channel.send("https://tenor.com/view/pirates-of-the-caribbean-pirates-dead-pirate-gif-26316215")
      await message.channel.send("OH NON ! Nous étions si près du but...McStingy partira donc avec son trésor à jamais...")
      await message.channel.send("*fin du jeu.*")
      await message.channel.send("*co.fondateurs : PINEAU Adrien, PETRIC Romario, MANZEYI Emmanuel et MATHYS Hemmy-Lola*")


      
      



client.run("MTA1MTQ0NDYxMTcxNDkyMDQ2OQ.GCQaD4.ALtfTxsabw4-jAqqlbaxF1Af4PxTUqBydb1UBA")
