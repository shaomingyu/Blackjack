from dealer import Dealer
from conservative_player import ConservativePlayer
from dealer_player import DealerPlayer
from hand import Hand
from random_player import RandomPlayer 
from player_bank import PlayerBank 
from french_deck import FrenchDeck

class Tester:

	dealer = Dealer ( FrenchDeck (12345) )
	dealer.add_player ('lia9 ', ConservativePlayer () , PlayerBank (100) )
	dealer.add_player ('lia8 ', RandomPlayer () , PlayerBank (100) )
	dealer.add_player ('lia7 ', ConservativePlayer () , PlayerBank (100) )
	dealer.add_player ('lia6 ', RandomPlayer () , PlayerBank (100) )
	dealer.take_bets ()
	dealer.deal_initial_hand ()
	dealer.deal_player_hands ()
	dealer.deal_dealer_hand ()
	dealer.settle_bets ()
	print ( str ( dealer ))