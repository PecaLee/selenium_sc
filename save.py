import csv

def save_to_file(data):
    file = open("result.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["date", "round", "num01", "num02", "num03", "num04", "num05", "num06", "num07", "num08"])
    for bingo in data:
        writer.writerow(list(bingo.values()))
    return