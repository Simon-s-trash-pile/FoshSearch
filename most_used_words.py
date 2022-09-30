from collections import defaultdict
import csv
import os
from turtle import clear


def index():
	index = []
	for file in ["general.csv","chat1.csv","chat2.csv","chat3.csv","clue.csv","res.csv"]:
		with open(f"csv/{file}",encoding="utf8") as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				index.append(row[3])
	return index

def search(index):
	temp = defaultdict(int)
	# memoizing count
	for sub in index:
		for wrd in sub.split():
			temp[wrd] += 1
	return temp



def clearConsole() -> None:
	"""
	Clears the console
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	common = ["can","could","me","is","just","time","be","good","to","the","person","have","new","of","and","year","do","first","in","a","way","say","last","for","that","day","get","long","on","I","thing","make","great","with","it","man","go","little","at","not","world","know","own","by","he","life","take","other","from","as","hand","see","old","up","you","part","come","right","about","this","child","think","big","into","but","eye","look","high","over","his","woman","want","different","after","they","place","give","small","her","work","use","large","she","week","find","next","or","case","tell","early","an","point","ask","young","will","government","work","important","my","company","seem","few","one","number","feel","public","all","group","try","bad","would","problem","leave","same","there","fact","call","able","their","the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","u"]
	for word in range(len(common)):
		common[word] = common[word]. lower()
	index = index()
	temp = search(index)
	print("#########################")
	sorted_words = sorted(temp.items(), key=lambda x: int(x[1]))
	sorted_words.reverse()
	i = 0
	clearConsole()
	for word,value in sorted_words:
		if word.lower() in common:
			continue
		print(f"'{word}' has been mentioned {value} times")
		i += 1
		if i == 10:
			input("Next 10 (Press Enter)")
			clearConsole()
			i = 0

