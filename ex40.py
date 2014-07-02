class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

all_around = Song(["All around me",
					"Are familiar faces"])

variable = ["I've been working on the railroad",
			"All the livelong day"]

railroad = Song(variable)					
					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

all_around.sing_me_a_song()

railroad.sing_me_a_song()