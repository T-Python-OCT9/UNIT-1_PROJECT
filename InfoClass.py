class Shows:
    kind="shows"
    def __init__(self,name:str, summary : str, NumberOfEpisodes: int) -> str:
        #initilizing the class
        #instance attributes / properties
        self.name = name
        self.summary = summary
        self.NumberOfEpisodes = NumberOfEpisodes
        
    def ShowsInfo(self)-> str:
        return f"Here is the summary for the show {self.name} , {self.summary} and it has a {self.NumberOfEpisodes}" 
#the action categories 
the_batman = ShowsInfo("The Batman","","")
demon_salyer = ShowsInfo("Demon Salyer","","")
hunter_hunter = ShowsInfo("Hunter X Hunter: Phantom Rouge","","")
Ambulance = ShowsInfo("Ambulance","","")
doctor_strange = ShowsInfo("Doctor Strange in the Multiverse of Madness","","")
spider_man= ShowsInfo("Spider-Man: No Way Home","","")
jurassic_world = ShowsInfo("Jurassic World Dominion","","")
memory = ShowsInfo("Memory","","")