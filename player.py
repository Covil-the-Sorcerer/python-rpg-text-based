health = 10
defense = 0
level = 0
name = ""


def setup_player() -> str:
    input_name = input("Qual o nome do seu personagem?\n->")
    
    return format_name(input_name)

def format_name(Name) -> str:
    formatted_name = Name.split()
    
    return formatted_name[0] if len(formatted_name) == 1 else " ".join(formatted_name)


name = setup_player()

print(name, level, health, defense)
