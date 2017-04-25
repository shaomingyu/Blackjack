class ConservativePlayer:

	def make_bet(self, balance):
		return balance / 10

	def use_ace_hi(self, hand):
		return not hand.score_hand(True) >= 21

	def want_card(self, hand, bank, dealer_cards, dealt_cards):
		return hand.get_score() < 15
			
