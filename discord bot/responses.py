from random import choice, randint

def get_response(user_input: str)-> str:
    lowered: str=user_input.lower()
    
    if lowered=='':
        return 'kuch bol le bhyi'
    elif 'hie' in lowered:
        return 'helu'
    elif 'how are you' in lowered:
        return 'fine'
    elif 'roll dice' in lowered:
        return f'you rolled :{randint(1,6)}'
    else :
        return choice(['didnt understand!'])
    