class Shows:
    kind="shows"
    def __init__(self,name:str, summary : str, NumberOfEpisodes: str) -> str:
        #initilizing the class
        #instance attributes / properties
        self.name = name
        self.summary = summary
        self.NumberOfEpisodes = NumberOfEpisodes
        
    def ShowsInfo(self)-> str:
        return f"Here is the summary for the show {self.name},{self.summary} and it has a {self.NumberOfEpisodes}" 

#the action categories start...
try:
    the_batman = Shows("The Batman: \n","The mayor of Gotham is murdered on Halloween night by a masked assailant who calls himself The Riddler (Paul Dano). The Gotham City Police Department investigate the murder, and Lieutenant James Gordon (Jeffrey Wright) and Batman find a message addressed to “The Batman.”","Movie 2h 56min")
except:
     print("An error occurred,please try to write the var correctly")
try:
    demon_salyer = Shows("Demon Salyer : \n","Tanjiro Kamado, our protagonist, is a youth whose family is brutally murdered by a demon. Although badly injured, his sister, Nezuko, is the sole survivor of the attack. Tanjiro rushes to town in a desperate attempt to find medical assistance for her. Along the way, she wakes and suddenly attacks him. As Nezuko attempts to kill him, an incredible swordsman appears.","26 ep")
except:
     print("An error occurred,please try to write the var correctly")
     
hunter_hunter = Shows("Hunter X Hunter: \n","Hunter X Hunter revolves around Gon Freecss whose goal in life is to find his father Ging, a renowned hunter. In order to find his father, Gon must become a hunter himself and sets out to do so.","148 ep")

Ambulance = Shows("Ambulance: \n","Ambulance' Plot Summary Distinguished US army veteran Will Sharp lives a life of financial struggle as he is turned away by every medical insurance company for experimental surgery to treat his wife's cancer. The couple also have a very young son, and Will promises his wife to stay out of trouble and look for an honest job.","80min")

doctor_strange = Shows("Doctor Strange in the Multiverse of Madness: \n","Doctor Strange teams up with a mysterious teenage girl from his dreams who can travel across multiverses, to battle multiple threats, including other-universe versions of himself, which threaten to wipe out millions across the multiverse. They seek help from Wanda the Scarlet Witch, Wong and others.","2h 28min")

spider_man= Shows("Spider-Man: No Way Home: \n","Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.","2h 13 min")

jurassic_world = Shows("Jurassic World Dominion:  \n","Jurassic World is a 2015 American science fiction action film directed by Colin Trevorrow, who co-wrote the screenplay with Rick Jaffa, Amanda Silver, and Derek Connolly from a story by Jaffa and Silver. It is the first installment in the Jurassic World trilogy and the fourth installment overall in the Jurassic Park franchise.","2h26min")

memory = Shows("Memory : \n","Alex Lewis is a long-time professional assassin working in Mexico and the US, who wants to now retire, probably because of his growing age and failing health.","1h 54min")
#action categorie end ...
#drama catgorie start...
a_silent_voice = Shows("A silent Voice: \n","story of redemption. Shouya's life grew increasingly unbearable in the years after he'd been pinned as a schoolyard bully. Nothing he did could dissuade other students from seeing him as a bad guy, so he quit trying, and grew depressed.","2h 9min")

tomorrow = Shows("Tomorrow : \n","Tomorrowtells about Choi Joon Woong (Rowoon). Choi Joon Woong is the man who gets into the accident while searching for a job. That accident makes him pass with the grim reaper. Koo Ryeon (Kim Hee Sun) and Lim Ryung Gu (Yoon Ji On) are grim reapers. They show up to help people who want to end their lives.","16 ep")

the_good_doctor = Shows("The Good Doctor: \n","Shaun Murphy, a young surgeon with autism and savant syndrome, relocates from a quiet country life to join a prestigious hospital's surgical unit. Alone in the world and unable to personally connect with those around him, Shaun uses his extraordinary medical gifts to save lives and challenge the skepticism of his colleagues.","18 ep")

a_beautiful_mind = Shows("A Beautiful Mind: \n","36 years old assistant professor at the department of neurology in Hyunsung hospital. He is a genius neurosurgeon who is unable to feel empathy. He is daring and has impeccable observational, deductive and logical skills which he uses to make lightning quick diagnosis.","14 ep")

parasite = Shows("Parasite:\n","he film starts with the Kim family, a South Korean family struggling with poverty in a poor neighborhood in an unnamed city. Ki-taek and Chung-sook, the patriarch and matriarch, are having trouble finding employment, and their children, Ki-woo and Ki-jung are trying to help in whatever way they can.","2h 12min")

grave_of_the_fireflies = Shows("Grave of the Fireflies: \n","the film tells the story of two siblings, Seita and Setsuko, and their desperate struggle to survive during the final months of the Second World War .","2h 28min")

#drama catgorie end...
#comedies start...
gilmore_grils= Shows("Gilmore Grils:\n","Gilmore Girls focuses on Lorelai Gilmore and her daughter Rory. Lorelai had Rory at the age of 16 and raised her daughter on her own. She left home soon after Rory was born and moved to Stars Hollow Connecticut, a small town where everyone knows each other.","153 ep")

SPY_FAMILY = Shows("SPYx FAMILY : \n","A spy on an undercover mission gets married and adopts a child as part of his cover. His wife and daughter have secrets of their own, and all three must strive to keep together.","25 ep")

Haikyuu= Shows("Haikyuu:\n","Junior high school student, Shoyo Hinata, becomes obsessed with volleyball after catching a glimpse of Karasuno High School playing in Nationals on TV. Of short stature himself, Hinata is inspired by a player the commentators nickname 'The Little Giant', Karasuno's short but talented wing spiker.","85 ep")

the_Office = Shows("The Office\n","The story of an office that faces closure when the company decides to downsize its branches. A documentary film crew follow staff and the manager David Brent as they continue their daily lives.","201 ep ")

reply_1988 = Shows("Reply 1988:\n","Reply 1988 revolves around the lives of a group of five friends in Ssangmun-dong, a small neighborhood in Seoul. Most of the series covered their struggles and memorable moments when they were 18 and 19 years old.","20 ep")
#comedies end...
#crimes start...
forgotten= Shows("Forgotten:\n","Jin-seok, a young man, moves to a new house with his mother, father, and older brother Yoo-seok. Things seem off to Jin-seok in their new home. One rainy night he witnesses Yoo-seok being kidnapped and dragged into a car. Nineteen days pass and suddenly, Yoo-seok returns. Jin starts noticing discrepancies in his family's personality.","1h 48 min")

how_to_get_away= Shows("How to get away with Murder:\n","Annalise Keating, law professor and criminal defense attorney at Middleton University, selects five students to intern at her firm—Wes Gibbins, Connor Walsh, Michaela Pratt, Asher Millstone, and Laurel Castillo—alongside her employees Frank Delfino and Bonnie Winterbottom, an associate lawyer.","90 ep")

voice= Shows("Voice:\n","Moo Jin-Hyuk (Jang Hyuk) was a popular detective who solved major cases, but after his wife was murdered by a serial killer his life spiraled down.","58 ep")

attack_on_titan= Shows("Attack on titan\n","Attack on Titan is set in a world where humanity lives inside cities surrounded by enormous walls due to the Titans, gigantic humanoid beings who devour humans. The story follows the adventures of Eren Jaeger , his childhood friends Mikasa Ackerman and Armin Arlert , whose lives are changed forever after a Colossal Titan breaches the wall of their home town.","87 ep")

black_list = Shows("Black List: \n"," Raymond Reddington (James Spader), Elizabeth \"Liz\" Keen (Megan Boone) and the members of the Task Force, a multiagency law enforcement working group dedicated to hunting down Reddington. Reddington surrenders to the FBI and offers to identify and help capture the criminals he has worked with, whom he calls \"The Blacklist\", but only if he is allowed to work with Liz Keen, a rookie profiler at the FBI.","200 ep")

suits = Shows("Suits","stars Gabriel Macht (Love and Other Drugs) as Harvey Specter,one of Manhattan's top corporate lawyers,and Patrick J. Adams (Lost) as Mike Ross,a brilliant but unmotivated college dropout. Harvey sets out to recruit a new hotshot associate from a pool of Harvard graduates and hires the only guy that manages to impress him,","134 ep")
#crimes end ...

#docuseries start...
the_great_hack = Shows("The Great Hack: \n"," documentary film about the Facebook Cambridge Analytica data scandal, produced and directed by Jehane Noujaim and Karim Amer, both previous documentary Academy Award nominees","1h 54min")

Mystery_lab= Shows("Mystery Lab: \n","Mystery Lab is by no means an outstanding, award-winning series but there's no denying that it amuses and the facts displayed, along with myths and rumors, make it genuinely good viewing.","8 ep")

How_To_Chanage_Your_Mind= Shows("How To Chanage Your Mind: \n","What the New Science of Psychedelics Teaches Us About Consciousness, Dying, Addiction, Depression, and Transcendence","4 ep")

our_Planet = Shows("Our Planet","It explores the rich natural wonders, iconic species and wildlife spectacles that still remain, and reveals the key issues that urgently threaten their existence. Today, we have become the greatest threat to the health of our planet.Our joint mission is to inspire people over the world to understand our planet - and the challenges it faces.","8 ep")

pandemic = Shows("Pandemic:\n","A five-part web series about a deadly virus and the people at the frontline of fighting bioterrorism.","8 ep")
#docuseries end...

#kids start...
sponge_bob= Shows("Sponge Bob: \n ","an American animated comedy television series created by marine science educator and animator Stephen Hillenburg for Nickelodeon.","250 ep")

Badanamu_Pop = Shows("Badanamu Pop: \n","pop and party with Bada and his adorable friends in a series of exciting singalongs that are as educational as they are fun","26 ep")

dragon_legends= Shows("Dragon Legends:\n","is an action packed ride aimed at children on the lower end of MG. With a missing friend, a big theme of this book is working as a group and trusting one another."," 100 ep")
boss_baby= Shows("Boss Baby: \n","Timothy (Tim) Templeton, an imaginative 7-year-old boy, relishes his parents' attention and is horrified when a new baby brother arrives. Boss Baby, whom he first saw arriving in a taxi, clad in suit and tie, and carrying a briefcase, behaves normally around the adults, crying for attention and food and diapers all day and night."," 40 ep")

kung_fo_panda= Shows("Kung Fo Panda: \n","is a story about a panda, named Po, who somehow finds himself being selected for the position of the Dragon Warrior, despite not having any form of training or athletic ability. This causes him to be shunned by his biggest idols: Shifu and the Furious Five.","52 ep")

cocomelon = Shows("Cocomelon :\n","Cocomelon's videos include children, adults, and animals who interact with each other in daily life.","25 ep")
#kids end...
'''print(the_batman.ShowsInfo())'''