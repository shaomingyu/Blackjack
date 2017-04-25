class DealerPlayer:

	def use_ace_hi(self, hand):
		return not hand.get_score() >= 21

	def want_card(self, hand, bank, dealer_cards, dealt_cards):
		return hand.get_score() < 17		