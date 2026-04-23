#Fist implementations of rotating through a list automatically
class Lineup:
	def __init__(self, characters):
		self.characters = characters
		self.last_character_index = (len(self.characters) - 1)

	def __iter__(self):
		self.n = 0
		return self

	def get_character(self, n):
		return self.characters[n]

	def __next__(self):
		if self.n < self.last_character_index:
			character = self.get_character(self.n)
			self.n += 1
			return character
		elif self.n == self.last_character_index:
			character = self.get_character(self.n)
			self.n = 0
			return character

#Second implementations of rotating through a list automatically
class InfiniteLineup:
	def __init__(self, characters):
		self.characters = characters

	def lineup(self):
		lineup_max = len(self.characters)
		index = 0
		while True:
			if index < lineup_max:
				yield self.characters[index]
			else:
				index = 0
				yield self.characters[index]

			index += 1

	def __repr__(self):
		return f'<Lineup({self.characters})'

	def __str__(self):
		return f'Lineup with the players: ({self.characters})'

characters = [
	'Link',
	'Zelda',
	'Mario',
	'Ridley',
	'Ness',
	'Fox',
	'Pikachu',
	'Donkey Kong',
	'Captain Falco'
]

animal_chars = [
	'Monkey',
	'Zebra',
	'Lion',
	'Bear',
	'Tiger'
]
#Pass data set to each called function and class
characters_lineup = Lineup(characters)
process = iter(characters_lineup)

print('First implementation')
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

#Pass data set once to class. That data set is retained for this instantiation.
full_characters_lineup = InfiniteLineup(characters)
smash_lineup = full_characters_lineup.lineup()
animal_lineup = InfiniteLineup(animal_chars)
animal_super_lineup = animal_lineup.lineup()
print('Second implementation')
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(next(smash_lineup))
print(repr(full_characters_lineup))
print(str(full_characters_lineup))
print('Animals')
print(next(animal_super_lineup))
print(next(animal_super_lineup))
print(next(animal_super_lineup))
print(next(animal_super_lineup))