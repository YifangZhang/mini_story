


class character:

	health = 0
	defense = 0
	attack = 0
	sanity = 0
	henati = 0

	def __init__(self):

		self.health = 100
		self.defense = 10
		self.attack = 10
		self.sanity = 100
		self.hentai = 50

		return None

	def effect(self, effect_stats):

		#effects
		self.health = self.health + effect_stats[0]
		self.defense = self.defense + effect_stats[1]
		self.attack = self.attack + effect_stats[2]
		self.sanity = self.sanity + effect_stats[3]
		self.hentai = self.hentai + effect_stats[4]

		return None