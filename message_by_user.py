import csv
import os

def index():
	index = []
	for file in ["general.csv","chat1.csv","chat2.csv","chat3.csv","clue.csv","res.csv"]:
		with open(f"csv/{file}",encoding="utf8") as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				index.append([row[3],row[1]])
	return index

def search(searchterm,index):
	searched = []
	for message,name in index:
		if searchterm.lower() in name.lower():
			searched.append([message.replace("\n"," "),name])
	return searched

index = index()
print(f"Loaded {len(index)} Messages")
print("#########################")

def clearConsole() -> None:
	"""
	Clears the console
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	while True:
		searchterm = input("Usrename here:" )
		searched = search(searchterm,index)
		clearConsole()
		for result in searched:
			print(f'"{result[0]}" by {result[1]}')
		print("########################")
		print(f"{len(searched)} results found.")
		print("#### ctrl+c to exit ####")




