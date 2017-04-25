class Hand:
 
	def __init__(self):
		self._cards = []
		self._score = 0

	def add_card(self, card):
		self._cards.append(card)

	def get_score(self):
		return self._score

	def set_score(self, score):
		self._score = score

	def has_ace(self):
		for card in self._cards:
			if card[0] == 'A':
				return true

	def score_hand(self, ace):
		face = ['J', 'Q', 'K']
		output = 0
		for card in self._cards: 
			if card[0] in face:
				output += 10
			elif card[0] == 'A':
				if ace:
					output += 11
				else:
					output += 1
			else:
				output += int(card[0])
		self._score = output
		return self._score

	def get_cards(self):
		output = self._cards
		return output

	def __len__(self):
		return len(self._cards)

	def __str__(self):
		output = ''
		for card in self._cards:
			output += str(card) + ' '
		return output