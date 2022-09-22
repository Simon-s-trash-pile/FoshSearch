import csv

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
		if searchterm in message:
			searched.append([message.replace("\n"," "),name])
	return searched

index = index()
print(f"Loaded {len(index)} Messages")

if __name__ == "__main__":
	while True:
		searchterm = input("Searchterm here:" )
		searched = search(searchterm,index)
		print(f"{len(searched)} results found.")
		print("#########################")
		for result in searched:
			print(f'"{result[0]}" by {result[1]}')
		print("############ ctrl + c to exit ############")


