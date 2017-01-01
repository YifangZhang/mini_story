


class interface:

	def introduction(self):

		print("long long ago, there is a stupid human")
		print("you need to make a choice every day to reach your goal")
		print("however, we are even worse on programming, so you can keep the goal yourself")
		print("we are really lazy, so we do not calculate if you reached your goal by decisions")
		print("just making sure you survived for this 100 days")
		print("even though there is no way you can lose XD")

		return None

	def displayQuestion(self, currentQuestion):

		## input: self - interface class
		## 		  currentQuestion - {"text" : "xxx", "effect_stats" : [1,2,3,4,5]}
		print(currentQuestion["text"])

		return None


