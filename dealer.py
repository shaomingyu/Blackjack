
from conservative_player import ConservativePlayer
from dealer_player import DealerPlayer
from hand import Hand
from random_player import RandomPlayer 
from player_bank import PlayerBank 
from french_deck import FrenchDeck

class Dealer:

	def __init__(self, deck):
		self._deck = deck
		self._dealer = DealerPlayer()
		self._dealer_hand = Hand()
		self._players = {}
		self.cards_dealt = []

	def add_player(self, handle, player, playerbank):
		if handle in self._players.keys():
			raise RuntimeError('player already exists')
		self._players[handle] = (Hand(), player, playerbank)

	def take_bets(self):
		for player in self._players.values(): 
			bet = player[1].make_bet(player[2].get_balance()) 
			player[2].enter_bet(bet)

	def deal_initial_hand(self):
		for player in self._players.values():
			card = self._deck.remove_card()
			player[0].add_card(card)
			self.cards_dealt.append(card)
		card = self._deck.remove_card()
		self._dealer_hand.add_card(card)
		self.cards_dealt.append(card)
		for player in self._players.values():
			card = self._deck.remove_card()
			player[0].add_card(card)
			self.cards_dealt.append(card)
		card = self._deck.remove_card()
		self._dealer_hand.add_card(card)

	def deal_player_hands(self):
		for player in self._players.values():
			player[0].set_score(player[0].score_hand(player[1].use_ace_hi(player[0])))
			score = player[0].get_score()
			while score < 21 and player[1].want_card(player[0], player[2], self._dealer_hand, self.cards_dealt):
				card = self._deck.remove_card()
				player[0].add_card(card)
				self.cards_dealt.append(card)
				score = player[0].score_hand(player[1].use_ace_hi(player[0]))
			player[0].set_score(score)
			if score > 21:
				player[2].bust()

	def deal_dealer_hand(self):
		self._dealer_hand.set_score(self._dealer_hand.score_hand(self._dealer.use_ace_hi(self._dealer_hand)))
		score = self._dealer_hand.get_score()
		while score < 17:
			card = self._deck.remove_card()
			self._dealer_hand.add_card(card)
			self.cards_dealt.append(card)
			score = self._dealer_hand.score_hand(self._dealer.use_ace_hi(self._dealer_hand))
		score = self._dealer_hand.set_score(score)

	def settle_bets(self):
		for player in self._players.values():
			if (player[0].get_score() < 21 and player[0].get_score() > self._dealer_hand.get_score()) or ((player[0].get_score() < 21) and (self._dealer_hand.get_score() > 21)):
				player[2].pay_winner(player[2].get_wager())
	
	def __str__(self):
		output = '$$$$$$   Game Summary   $$$$$$\nDealer:\nscore: ' + str(self._dealer_hand.get_score()) + '\n' + str(self._dealer_hand) + '\n\n'
		for key,player in self._players.items(): 
			output += 'Player: ' + key + '\nscore: ' + str(player[0].get_score()) + '\n' + str(player[0]) + '\n' + str(player[2]) + '\n\n'
		return output