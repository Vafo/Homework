
def get_top_performers(filepath, number_of_students: int = 5):
    entries = []

    with open(filepath, "r") as file:
        model = file.readline().rstrip().split(',')

        
        for line in file:
            data = line.rstrip().split(',')
            entry = { key:val for key, val in zip(model, data)  }
            entries.append(entry)

    entries = sorted(entries, key = lambda dic : float(dic["average mark"]), reverse=True)
    res = [entry["student name"] for entry in entries[:number_of_students]]

    return res


losers = get_top_performers("../data/students.csv")
print(losers)

