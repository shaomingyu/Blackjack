class PlayerBank:

	def __init__(self, balance):
		self._balance = balance
		self._bets_placed = 0
		self._is_winner = False

	def pay_winner(self, amount):
		self._balance += 2 * amount
		self._is_winner = True

	def bust(self):
		self._is_winner = False

	def get_balance(self):
		return self._balance

	def get_wager(self): 
		return self._bets_placed

	def enter_bet(self, amount):
		self._bets_placed += amount
		self._balance -= amount
		if amount > self._balance:
			raise RuntimeError('bet exceeds balance') 

	def __str__(self):
		output = 'Player assets:\nbet ' + str(self.get_wager()) + ' balance ' + str(self.get_balance())
		if self._is_winner:
			output += ' winner!'
		else:
			output += ' bust.'	
		return output