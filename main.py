from pet import Pet, PetType
import random
from time import sleep

def main():
    print("""
    🐾✨ WELCOME TO ULTIMATE PET SIMULATOR ✨🐾
    ------------------------------------------
    """)
    
    print("Let's create your new pet!")
    name = input("What will you name your pet? ")
    
    print("\nChoose a pet type:")
    for i, pet_type in enumerate(PetType, 1):
        print(f"{i}. {pet_type.value} {pet_type.name.capitalize()}")
    
    type_choice = int(input("Enter choice (1-5): ")) - 1
    pet_type = list(PetType)[type_choice]
    
    pet = Pet(name, pet_type)
    print(f"\nMeet your new {pet_type.name.lower()}, {name}! {pet_type.value}🎉")
    

    day = 1
    while True:
        print(f"\n🌞 Day {day} with {pet} 🌞")
        print("What would you like to do?")
        
        actions = [
            ("Feed", ["Regular food", "Treat", "Vegetable", "Fruit"]),
            ("Play", ["Fetch", "Laser pointer", "Free play"]),
            ("Sleep", []),
            ("Train", ["Enter custom trick"]),
            ("Check status", []),
            ("Show tricks", []),
            ("Special actions", ["Speak", "Celebrate birthday", "Random event"]),
            ("Quit", [])
        ]
        
        for i, (action, subactions) in enumerate(actions, 1):
            print(f"\n{i}. {action}")
            for j, subaction in enumerate(subactions, 1):
                print(f"    {i}.{j} {subaction}")
        
        choice = input("\nEnter your choice (e.g., '1', '2.3'): ")
        
        try:
            if choice == "1":  
                sub = input("What food? (1-4): ")
                foods = ["food", "treat", "vegetable", "fruit"]
                pet.eat(foods[int(sub)-1])
                
            elif choice == "2":  
                sub = input("What game? (1-3): ")
                games = ["fetch", "laser", "default"]
                pet.play(games[int(sub)-1])
                
            elif choice == "3":  
                pet.sleep()
                
            elif choice == "4":  
                trick = input("What trick to teach? ")
                pet.train(trick)
                
            elif choice == "5":  
                pet.get_status()
                
            elif choice == "6":  
                pet.show_tricks()
                
            elif choice == "7":  
                sub = input("Action? (1-3): ")
                if sub == "1":
                    pet.speak()
                elif sub == "2":
                    pet.birthday()
                elif sub == "3":
                    pet.random_event()
                    
            elif choice == "8":  
                print(f"\nGoodbye! {pet} will miss you! {pet._sad_emoji()}")
                break
                
            else:
                print("Invalid choice. Try again.")
                
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
        
        sleep(1) 
        day += 1
        pet.hunger = min(10, pet.hunger + 1)  
        pet.energy = max(0, pet.energy - 0.5)  
        
       
        if random.random() < 0.2:  
            pet.random_event()

if __name__ == "__main__":
    main()