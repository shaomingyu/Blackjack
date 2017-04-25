import random

class RandomPlayer:

	def make_bet(self, balance):
		return balance // random.randrange(2, 10)

	def use_ace_hi(self, hand):
		return not hand.get_score() >= 21

	def want_card(self, hand, bank, dealer_cards, dealt_cards):
		return hand.get_score() < random.randrange(1, 20)
			