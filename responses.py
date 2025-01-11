from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'joke' in lowered:
        return choice([
            'Why don’t scientists trust atoms? Because they make up everything!',
            'Why did the scarecrow win an award? Because he was outstanding in his field!',
            'Why don’t skeletons fight each other? They don’t have the guts.'
        ])
    elif 'fact' in lowered:
        return choice([
            'Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.',
            'Bananas are berries, but strawberries aren’t.',
            'A day on Venus is longer than a year on Venus.'
        ])
    else:
        return choice([
            'I don\'t understand...',
            'What are you talking about?',
            'Do you mind rephrasing that?'
        ])