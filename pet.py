import random
from enum import Enum

class PetType(Enum):
    DOG = "🐕"
    CAT = "🐈"
    RABBIT = "🐇"
    HAMSTER = "🐹"
    BIRD = "🐦"

class Pet:
    def __init__(self, name, pet_type=PetType.DOG):
        self.name = name
        self.type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.health = 10  
        self.age = 0 
        
    def __str__(self):
        return f"{self.type.value} {self.name}"
    
    def eat(self, food="food"):
        food_emojis = {
            "food": "🍖", "treat": "🍪", "vegetable": "🥕", "fruit": "🍎"
        }
        emoji = food_emojis.get(food, "🍽️")
        
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        self.health = min(10, self.health + (1 if food in ["vegetable", "fruit"] else 0))
        print(f"{self} is eating {food} {emoji}")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        self.health = min(10, self.health + 1)
        print(f"{self} is sleeping... {self._sleep_emoji()}")
    
    def _sleep_emoji(self):
        if self.type == PetType.CAT:
            return random.choice(["💤", "😴", "🐈⬛"])
        return "💤"
    
    def play(self, game="default"):
        if self.energy <= 0:
            print(f"{self} is too tired to play! {self._tired_emoji()}")
            return
        
        game_effects = {
            "fetch": (3, 3, 2),
            "laser": (2, 4, 1) if self.type == PetType.CAT else (2, 2, 1),
            "default": (2, 2, 1)
        }
        energy_cost, happiness_gain, hunger_gain = game_effects.get(game, (2, 2, 1))
        
        self.energy = max(0, self.energy - energy_cost)
        self.happiness = min(10, self.happiness + happiness_gain)
        self.hunger = min(10, self.hunger + hunger_gain)
        print(f"{self} is playing {game}! {self._play_emoji(game)}")
    
    def _play_emoji(self, game):
        emojis = {
            "fetch": "🎾",
            "laser": "🔴",
            "default": "🎮"
        }
        return emojis.get(game, "🎲")
    
    def train(self, trick):
        if self.energy <= 1:
            print(f"{self} is too tired to learn! {self._tired_emoji()}")
            return
        
        difficulty = len(trick.split())  
        success_chance = min(90, 100 - (difficulty * 10))
        
        if random.randint(1, 100) <= success_chance:
            self.tricks.append(trick)
            print(f"{self} learned '{trick}'! 🎉")
        else:
            print(f"{self} didn't quite get '{trick}' this time. 😅")
        
        self.energy -= 1
        self.happiness = min(10, self.happiness + 1)
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self} hasn't learned any tricks yet. {self._sad_emoji()}")
            return
        
        print(f"{self} knows these tricks:")
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick} {'🌟' if len(trick) > 10 else '⭐'}")
    
    def get_status(self):
        print(f"\n{self}'s Status:")
        print(f"Hunger:   {self._meter(self.hunger, reverse=True)}")
        print(f"Energy:   {self._meter(self.energy)}")
        print(f"Happiness:{self._meter(self.happiness)}")
        print(f"Health:   {self._meter(self.health)}")
        print(f"Age:      {self.age} cycles")
    
    def _meter(self, value, reverse=False):
        bars = "█" * value
        empty = " " * (10 - value)
        if reverse:
            bars, empty = empty, bars
        return f"[{bars}{empty}] {value}/10"
    
    def _tired_emoji(self):
        return random.choice(["😴", "💤", "🛌"])
    
    def _sad_emoji(self):
        return random.choice(["😢", "😞", "🥺"])
    
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self}! 🎂")
        self.happiness = min(10, self.happiness + 2)
    
    def speak(self):
        sounds = {
            PetType.DOG: "Woof!",
            PetType.CAT: "Meow!",
            PetType.RABBIT: "...",
            PetType.HAMSTER: "Squeak!",
            PetType.BIRD: "Chirp!"
        }
        print(f"{self} says: {sounds.get(self.type, '...')}")
    
    def random_event(self):
        events = [
            ("found a toy", 1, 0, 1),
            ("saw a squirrel", -1, -1, 0),
            ("took a nap", 0, 2, 0),
            ("met a friend", 0, 0, 2)
        ]
        event, hng, en, hp = random.choice(events)
        self.hunger = max(0, min(10, self.hunger + hng))
        self.energy = max(0, min(10, self.energy + en))
        self.happiness = max(0, min(10, self.happiness + hp))
        print(f"{self} {event}! {random.choice(['🎊', '🎈', '✨'])}")