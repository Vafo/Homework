
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

def sort_by_age(file_src, file_out):
    entries = []
    model = ""

    with open(file_src, "r") as file:
        model = file.readline().rstrip().split(',')
        
        for line in file:
            data = line.rstrip().split(',')
            entry = { key:val for key, val in zip(model, data)  }
            entries.append(entry)

    entries = sorted(entries, key = lambda dic : float(dic["age"]), reverse=True)

    with open(file_out, "w") as file:
        file.write(",".join(model) + "\n")

        for entry in entries:

            file.write(",".join( [val for key, val in entry.items()] ) + "\n")


    return file.closed


losers = get_top_performers("../data/students.csv")
print(losers)

sort_by_age("../data/students.csv", "../data/students_srt_by_age.csv")

