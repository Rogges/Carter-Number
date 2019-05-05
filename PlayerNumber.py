class PlayerGraph():

	def __init__(self, player_id):

		self.player_id = player_id
		# Placeholder for graph construction function
		self.graph = make_graph(player_id)

	def find_path(self, player2_id):

		'''
		Finds the shortest path between player_id and player2_id
		@param str player2_id: the ID of the player you want to find
		@param list rtype: ordered list from player_id to player2_id
		player_id will always be the last element and player2_id will
		always be the last element
		'''

		pass

	def is_between(self, player2_id, player_inter_id):

		'''
		Determines whether there is a connection between player_id
		and player2_id through player_inter_id
		@param str player2_id
		@param str player_inter_id
		@rtype list: returns shortest path as a list with player_inter_id
		in bewtween; if no path exists returns an empty list
		'''
		pass

	def player_with_num(self, num):
		
		'''
		Returns a list of all players with a player number equal to num
		@param int num
		@rtype list
		'''
		pass
	
	def is_fully_connected(self):
		
		'''
		Checks if graph is fully connected
		@rtype bool
		'''
		pass
