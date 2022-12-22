from time import sleep
endMessage = r"I am a bot \(thankfully not russian\), and this action was performed automatically. Please [contact the moderators of this subreddit](https://www.reddit.com/message/compose?to=%2Fr%2F2westerneurope4u&subject=2WE4uBot) if you have any questions or concerns."

needMoreMessage = "\n\nThis bot is new, and I don't have info to roast this flair. Please input some."

typeOfMessages = {
    "flairUp":f"Hello, I'm your local bot. I need you to flair yourself to roast you correctly, you coward.\n\n**Your comment/post has been removed by rule 3.**\n\nI will approve your comment/post when you flair yourself.",
    "d2918ce2-7ad1-11ed-b5bc-26aa68d2e47b":f"Finally, you flaired yourself. Let's see... Oh... So you're a Spaniard tax evading. That or you're Fr🤢nch.", #Andorra
    "53f4601c-bdb7-11ec-87db-4e94b7ed41d4":f"Finally, you flaired yourself. Let's see... Oh... So you're a painter that entered art school... I hope.", #Austria
    "522192e6-7b9e-11ed-80c3-3e80839b3739":f"Finally, you flaired yourself. Let's see... Oh... So you're a speedbump. Please, pick a real nation.", #Belgium
    "b7971146-bdb7-11ec-8b54-36fd3cae5f92":f"Finally, you flaired yourself. Let's see... Oh... So you're from Belgium, Flanders {needMoreMessage}", 
    "3554e270-bdb8-11ec-b025-32bbb6f910d9":f"Finally, you flaired yourself. Let's see... Oh... So you're from Belgium, Wallonia {needMoreMessage}",
    "554214e2-7ad0-11ed-9456-3ea726807d58":f"Finally, you flaired yourself. Let's see... Oh... So you're from Bulgaria {needMoreMessage}",
    "f014d5d8-7a79-11ed-a48e-d6aaa3fc2c26":f"Finally, you flaired yourself. Let's see... Oh... So you're from Croatia {needMoreMessage}",
    "ed6172be-7acf-11ed-9e7b-fe27d1fba7a6":f"Finally, you flaired yourself. Let's see... Oh... So you're from Cyprus {needMoreMessage}",
    "7c58e72c-7ad0-11ed-8d2b-e6cf7ad42cf0":f"Finally, you flaired yourself. Let's see... Oh... So you're from Czechia {needMoreMessage}",
    "e4a8ae62-c7d3-11ec-b1e3-ea8c297dcd76":f"Finally, you flaired yourself. Let's see... Oh... So you're from Denmark {needMoreMessage}",
    "2d4d0b8e-7c67-11ed-80d2-b29fde56bf38":f"Finally, you flaired yourself. Let's see... Oh... So you're from Estonia {needMoreMessage}",
    "2548602a-c7d4-11ec-8ecf-7afa8b67663b":f"Finally, you flaired yourself. Let's see... Oh... So you're from Finland {needMoreMessage}",
    "5ba41c22-81dd-11ed-a9ba-aa97e6863674":f"Finally, you flaired yourself. Let's see... Oh... So you're from Finland, Sapmi {needMoreMessage}",
    "4b9ea5e4-bdb7-11ec-b344-e2f3858ee251":f"Finally, you flaired yourself. Let's see... Oh... So you're from France {needMoreMessage}",
    "54019fc2-81dc-11ed-9ccc-76e6d81031a8":f"Finally, you flaired yourself. Let's see... Oh... So you're from France, Brittany {needMoreMessage}",
    "ceefff92-c1c2-11ec-95a1-924036b33468":f"Finally, you flaired yourself. Let's see... Oh... So you're from Germany {needMoreMessage}",
    "6fe504d4-bdb7-11ec-97fa-be3b2ab3081d":f"Finally, you flaired yourself. Let's see... Oh... So you're a German. Don't pass out when Oktoberfest starts.", #Germany, Bavaria"
    "35e3504c-cf14-11ec-b540-ae8031436c51":f"Finally, you flaired yourself. Let's see... Oh... So you're from Greece {needMoreMessage}",
    "2ba21802-7ad1-11ed-8f87-3ea726807d58":f"Finally, you flaired yourself. Let's see... Oh... So you're from Hungary {needMoreMessage}",
    "13964ac2-c7d4-11ec-9a8f-227f1635cfc5":f"Finally, you flaired yourself. Let's see... Oh... So you're from Iceland {needMoreMessage}",
    "c68992aa-bdb7-11ec-881d-e2b3a9190c48":f"Finally, you flaired yourself. Let's see... Oh... So you're from Ireland {needMoreMessage}",
    "d0ff0ab2-bdb7-11ec-b741-7a9fefbf0b77":f"Finally, you flaired yourself. Let's see... Oh... So you're from Italy {needMoreMessage}",
    "53727cd2-7ad1-11ed-bd02-5e10d83233f2":f"Finally, you flaired yourself. Let's see... Oh... So you're from Latvia {needMoreMessage}",
    "6b2f992c-7ad1-11ed-b9dd-aece9855b49c":f"Finally, you flaired yourself. Let's see... Oh... So you're from Lithuania {needMoreMessage}",
    "d9f2f638-bdb7-11ec-8b3f-7e9556fda3c2":f"Finally, you flaired yourself. Let's see... Oh... So you're from Luxembourg {needMoreMessage}",
    "cad551f0-7ad1-11ed-8cb3-36ce6a7a2d10":f"Finally, you flaired yourself. Let's see... Oh... So you're from Malta {needMoreMessage}",
    "e11a1f72-bdb7-11ec-8185-c22b83b8c1f8":f"Finally, you flaired yourself. Let's see... Oh... So you're from Netherlands {needMoreMessage}",
    "6fd14506-7b0e-11ed-8188-fa5e43563d6f":f"Finally, you flaired yourself. Let's see... Oh... So you're from the Netherlands, Friesland {needMoreMessage}",
    "028531a8-c7d4-11ec-8c80-1280e52d18c6":f"Finally, you flaired yourself. Let's see... Oh... So you're from Norway {needMoreMessage}",
    "17532e30-7ad2-11ed-adab-dac8f94fb420":f"Finally, you flaired yourself. Let's see... Oh... So you're from Poland {needMoreMessage}",
    "6ba25f6a-c1c3-11ec-adb5-1a865bbdd462":f"Finally, you flaired yourself. Let's see... Oh... So you're a towel seller. Please, just don't speak Brazilian here.", #Portugal"
    "bed3ed48-7ad2-11ed-ac8f-72ec02862332":f"Finally, you flaired yourself. Let's see... Oh... So you're a... you can go, but please don't rob me.", #Romania
    "a401beb0-7b9e-11ed-9079-8e53027eeec7":f"Finally, you flaired yourself. Let's see... Oh... So you're a son of a war criminal.", #Serbia
    "c60cbfea-7ad2-11ed-b634-66e637854993":f"Finally, you flaired yourself. Let's see... Oh... So you're from Slovakia {needMoreMessage}",
    "cb2fac76-7ad2-11ed-a7de-8e99bcc0c45e":f"Finally, you flaired yourself. Let's see... Oh... So you're from Slovenia {needMoreMessage}",
    "074a2656-c1c3-11ec-bdb7-868c9735db73":f"Finally, you flaired yourself. Let's see... Oh... So you're a lazy siesta. Wake up, today is a work day.", #Spain
    "2ce3644c-7c6f-11ed-a411-d25ac7ac116c":f"Finally, you flaired yourself. Let's see... Oh... So you're a real Spaniard. Close Reddit and go to work.", #Spain, Andalucia
    "75cd58ca-81dd-11ed-8152-f62496c24006":f"Finally, you flaired yourself. Let's see... Oh... So you're an engineer making rockets. Please do not speak your demonic language.", #Spain, Basque Country
    "bdd70bb2-7afc-11ed-844a-72ec02862332":f"Finally, you flaired yourself. Let's see... Oh... So you're an African. ", #Spain, Canary Islands
    "df046d48-c7d3-11ec-bbe8-121542c6281b":f"Finally, you flaired yourself. Let's see... Oh... So you're a Spaniard. Just cope dude.", #sPain, Catalunya
    "fb92536c-c7d3-11ec-a972-7e7abb2e9213":f"Finally, you flaired yourself. Let's see... Oh... So you're from Sweden {needMoreMessage}",
    "24ffee42-bdb8-11ec-8106-16322fd742cf":f"Finally, you flaired yourself. Let's see... Oh... So you're from Switzerland {needMoreMessage}",
    "58ab816e-7b9c-11ed-952a-42126ba9440b":f"Finally, you flaired yourself. Let's see... Oh... So you're an Ukranian. Слава Україні!", #Ukraine
    "334dae08-7b9f-11ed-bbe0-0eca0a8d77f3":f"Finally, you flaired yourself. Let's see... Oh... So you're a British. You just don't want to admit it.", #United Kingdom
    "4ec16f72-c1a4-11ec-a714-8e8de98ba9a8":f"Finally, you flaired yourself. Let's see... Oh... So you're a drunk brexiter. I don't know what to joke about, being British it's already one.", #United Kingdom, England
    "097d10aa-bdb8-11ec-be93-3e24c79bf379":f"Finally, you flaired yourself. Let's see... Oh... So you're British but you live on another island.", #United Kingdom, Northern Ireland
    "14eddb54-bdb8-11ec-a91e-fe4ebcc30285":f"Finally, you flaired yourself. Let's see... Oh... So you're a British in disguise. You guys ruined Scotland.", #United Kingdom, Scotland
    "2fd65e46-bdb8-11ec-9e2c-aa2c49b0874c":f"Finally, you flaired yourself. Let's see... Oh... So you're from the United Kingdom, Wales {needMoreMessage}",
    "69e22baa-bdb9-11ec-9190-36b910b9b93f":f"Finally, you flaired yourself. Let's see... Oh... So you're an Ameritard. I hope not. I will keep an eye on you.", #Non-european
    "508d9fbc-7ad4-11ed-b050-0eb92af99381":f"Finally, you flaired yourself. Let's see... Oh... So you're a bot. Hello mate!" # Funded by the EU
}


def reply(toComment, message: str) -> None:
    toComment.reply(f"{typeOfMessages[message]}\n\n---\n\n^({endMessage})")
    print(f"Commented on {toComment} because {message}.")

def edit(comment, message: str) -> None:
    comment.edit(f"{typeOfMessages[message]}\n\n---\n\n^({endMessage})")
    print(f"Edited on {comment} because {message}.")