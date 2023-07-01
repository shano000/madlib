# In this project I will be recreating the madlib in attempt to make it more interactive. \
# It will consist of different genres of stories. I will also add more words to substitute \
# to create more user customization.

print('The Mad Lib genres are: action, adventure, romance, comedy, drama, scifi, thriller, \
fantasy, horror')
genre = input('Choose your favorite genre: ')

noun1 = input('noun: ')
noun2 = input('noun: ')
noun3 = input('noun: ')
adj1 = input('adjective: ')
adj2 = input('adjective: ')
adj3 = input('adjective: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
verb3 = input('verb: ')

action = f'With a {adj1} roar, the fearless {noun1} {verb1} the elusive {noun2} through the \
labyrinthine streets of the city, his heart pounding with adrenaline. The {adj2} {noun2}, clad \
in a sleek black attire, {verb2} over {noun3}, skillfully evading capture. Finally, \
in a {adj3}  showdown, the {noun1} cornered the desperate {noun2}, overpowering him with \
a decisive blow and {verb3} justice to the city.'

adventure = f'In a remote, uncharted island, a {adj1} {noun1} {verb1} on a treacherous \
journey, venturing deep into the dense jungle, adorned with ancient ruins and lush vegetation. \
Armed with a {adj2} {noun2} and a keen sense of adventure, she {verb2} into mysterious caverns, \
unearthing long-lost artifacts and deciphering cryptic symbols. Overcoming {adj3} {noun3}, \
she {verb3} triumphant, her quest for discovery etching her name in the annals of history.'

romance = f'Underneath the moonlit sky, a {adj1} {noun1} met an enchanting {noun2}, their \
eyes locking in an electric{adj2}through the starlit night, their laughter {verb1} through \
the {adj3} {noun3}. In a whirlwind of emotions, they {verb2} to the irresistible pull of love, {verb3} a \
vibrant masterpiece of eternal devotion.'

comedy = f'In a wacky circus, a {adj1} {noun1} {verb1} a daring tightrope walk, teetering precariously \
above the cheering crowd. His comically {adj2} shoes and exaggerated gestures added to the spectacle, \
as he stumbled and {verb2}, narrowly avoiding {noun2}. The {noun3} {verb3} in laughter, applauding \
his {adj3} performance, and the acrobat, despite his mishaps, became the unexpected star of the show.'

drama = f'Within the confines of a desolate theater, a {adj1} {noun1} {verb1} a melancholic masterpiece, \
weaving together themes of love, loss, and betrayal. The {adj2} melodies of the {noun2} {verb2} through \
the dimly lit auditorium, intensifying the emotions conveyed by the riveting actors on stage. As the \
final act {verb3}, tears welled in the eyes of the {adj3} {noun3}, moved by the tragic tale that had \
unfolded before them.'

scifi = f'In the {adj1} reaches of the {noun1}, a {adj2} {noun2} {verb1} through the interstellar \
expanse, its {adj3} design {verb2} with advanced technology. A brave crew of {noun3} {verb3} on a \
perilous mission, venturing into uncharted territories, their hearts pulsating with anticipation. \
They encountered sentient alien beings, engaged in epic space battles, and unlocked the secrets of \
the universe, forever changing the course of human history.'

thriller = f'In the {adj1} lit corridor of the {adj2} {noun1}, a chilling silence {verb1} heavy, \
broken only by the distant echoes of a creaking door. The relentless pursuit between \
the {adj2} {noun2} and the {adj3} {noun3} escalated, their cat-and-mouse game {verb2} by unyielding \
determination. With a sudden burst of adrenaline, the detective {verb3} the elusive murderer, the \
final piece of the puzzle falling into place as justice was served in a spine-tingling climax.'

fantasy = f'Amidst the {adj1} realm of {adj2} {noun1} and {adj3} {noun2}, a courageous {noun3} {verb1} \
an ancient staff adorned with shimmering gemstones, {verb2} raw elemental energy. The mystical beasts \
roamed freely, their majestic wings {verb3} gracefully through the celestial skies, while the emerald \
forests whispered secrets to those who dared to listen. With a flick of the sorcerers wrist, a \
torrential surge of magic surged forth, unraveling the ancient spell and unveiling a hidden portal \
to realms yet unexplored.'

horror = f'In the {adj1} {noun1} nestled deep within the {adj2} forest, an {adj3} presence loomed, \
shrouded in darkness and malevolence. A spine-chilling howl {verb1} the night air, {verb2} shivers \
down the spines of those unfortunate {noun2} trapped within its vicinity. Their trembling hands \
clutched tightly to their hearts as they {verb3} helplessly to the haunting whispers that echoed \
through the {adj1} {noun3}, foretelling their impending doom.'

if genre == 'action':
    print(action)
elif genre == 'adventure':
    print(adventure)
elif genre == 'romance':
    print(romance)
elif genre == 'comedy':
    print(comedy)
elif genre == 'drama':
    print(drama)
elif genre == 'scifi':
    print(scifi)
elif genre == 'thriller':
    print(thriller)
elif genre == 'fantasy':
    print(fantasy)
else:
    print(horror)
