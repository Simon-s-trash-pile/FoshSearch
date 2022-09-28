import csv
import os

def index():
	index = []
	for file in ["general.csv","chat1.csv","chat2.csv","chat3.csv","clue.csv","res.csv"]:
		with open(f"csv/{file}",encoding="utf8") as csvfile:
			reader = csv.reader(csvfile)
			first = True
			for row in reader:
				if first:
					first = False
					continue
				if row[-1] != "":
					index.append(str(row[-1]).split("(")[0].strip())
	return index

def search(searchterm,index):
	temp = []
	for reaction in index:
		if reaction == searchterm:
			temp.append("­")
	return len(temp)

index = index()
print(f"Loaded {len(index)} Reactions")
print("#########################")

def clearConsole() -> None:
	"""
	Clears the console
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	while True:
		searchterm = input("Search term here:" )
		searched = search(searchterm,index)
		clearConsole()
		print("########################")
		print(f"Found {searched} occurences of {searchterm}")
		print("#### ctrl+c to exit ####")




