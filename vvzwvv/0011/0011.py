from cmd import Cmd

class CmdCheck(Cmd):
	
	def __init__(self):
		Cmd.__init__(self)
		self.intro = "-------- Word Sensor (Input \"exit\" for termination) --------"
		self.prompt = "> "
		self.sensitive = map(lambda word: word.strip("\n"), open("filtered_words.txt").readlines())

	def default(self, line):
		if any([word in line for word in self.sensitive]):
			print "Freedom"
		else:
			print "Human Rights"

	def do_exit(self, line):
		exit()

if __name__ == "__main__":
	cmd = CmdCheck()
	cmd.cmdloop()