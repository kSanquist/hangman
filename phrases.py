import random

phrases = [
    ['unique', 'academy', 'attitude', 'motif', 'fluctuation', 'sausage', 'microphone',
     'distortion', 'artificial', 'scenario', 'orchestra', 'reptile', 'economics', 'invisible',
     'legendary', 'parachute', 'obscure', 'eliminate', 'suppress', 'pepper', 'perception',
     'inappropriate', 'pressure', 'thoughtful', 'volunteer', 'engineering', 'opposition',
     'motorcycle', 'coerce', 'midnight', 'splurge', 'amputate', 'comment', 'participate'    
    ], 
    ['i love you', 'get lost creep', 'get enough sleep', 'now or never', 'keep it legal',
     'over and out', 'ride or die', 'i call bullshit', 'death before dishonor',
     'no shit sherlock', 'octopus tentacle', 'artificial intelligence',
     'chemical reaction', 'golden toilet throne', 'pixelated anteater', 'elegant gentleman',
     'quadruple animals', 'colorful vocabulary', 'secondary education', 'corroded aluminum',
     'excellent specimen'
    ], 
    ['razzmatazz', 'xylophone', 'jazzercise', 'larynx', 'mnemonic devices', 'mystical pneumonia',
     'infinite queue', 'zigzagging zombie', 'awkward beekeeper', 'luxurious galaxies', 'platonic friendship',
     'triangulated position', 'blasphemous shenanigans', 'suspicious rendezvous', 'mannequin hooliganism',
     'interrupted telecommunication', 'bourgeoisie', 'scatological confidante', 'fawning sycophants',
     'corrupt goverment politicians', 'bamboozled apparitions', 'incomprehensibilities',
     'semitranslucent alligator statuette', 'antidisestablishmentarianism',
     'pneumonoultramicroscopicsilicovolcanoconiosis'
    ]
]

def get_random_phrase_idx(difficulty):
    return random.randint(0, len(phrases[difficulty-1])-1)

def get_random_phrase(difficulty):
    if difficulty == 1: return phrases[difficulty-1][get_random_phrase_idx(difficulty)]
    elif difficulty == 2: return phrases[difficulty-1][get_random_phrase_idx(difficulty)]
    else: return phrases[difficulty-1][get_random_phrase_idx(difficulty)]