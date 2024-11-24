from collections import defaultdict
from itertools import *


f = open("generator/fellows.csv", "r").readlines()
fellows = []
for x in f:
    arr = x[:-1].split(",")
    fellows.append((arr[1], arr[2], arr[5], arr[0]))
    #               first     last     year   full

raw_mentor = {
    "2013": ["JB Rubinovitz", "Matt Bunday", "Randall Hunt", "Sean Hogan"],
    "2014": ["Alex Berke", "Daria Jung", "Gerard O'Neill",  "Ananta Pandey", "Phillip Quiza", "Sean Yeh"],
    "2015": ["Daniel Alabi", "Alex Berke", "Catherine Moresco", "Daniel Lobato", "Matt Condon"],
    "2016": ["Daniel Alabi", "Kevin Yeh", "Kimberly Leon", "Manny Lopez", "Emily Pries", "Simon Ayzman"],
    "2017": ["Claire Durand", "Dan Gorelick", "Sakib Jalal", "Sruti Modekurty", "Su Wang", "Emily Pries", "Simon Ayzman"],
    "2018": ["Alice Ren", "Christopher Wan", "Dan Gorelick", "Jacob Aronoff", "Melanie Sawyer"],
    "2019": ["Chris Wan", "Diana Kris", "Hugh Han", "Marley Alford", "Ray Berger", "Ben Yang", "Zach Hay", "Emily Koagedal", "Oluwatosin Afolabi"],
    "2020": ["Kellie Dinh", "Cliff Lezark", "Alice Phan", "John Philip", "Marley Alford", "Kaitlyn Stewart", "Daniel Alabi"],
    "2021": ["John Philip", "Suzanne Wang", "Diane Phan", "Cliff Lezark", "Diana Kris"],
    "2022": ["Sakib Jalal", "Diane Phan", "Kevin Liao", "Rahma Ahmed", "Erin McNulty"],
    "2023": ["David Frankel", "Lucie le Blanc", "Yamini Ananth", "Jun Woo Shin"],
    "2024": ["Harrison Liddiard", "Sophia Abraham", "Vivian Prince", "Moody Rahman"]
}

mentor = defaultdict(lambda: [])


def find_fellow(person):
    fname = person.split(" ", 1)[0]
    lname = person.split(" ", 1)[1]
    if len([x for x in fellows if x[0] == fname and x[1] == lname]):
        return [x
                for x in fellows if x[0] == fname and x[1] == lname][0]

    # then check if 
    elif len([x[2] for x in fellows if x[1] == lname]):
        return [x for x in fellows if x[1] == lname][0]

    elif len([x[2] for x in fellows if fname in x[3] and lname in x[3]]):
        return [x for x in fellows if fname in x[3] and lname in x[3]][0]
    
    elif len([x[2] for x in fellows if fname in x[3] or lname in x[3]]):
        return [x for x in fellows if fname in x[3] or lname in x[3]][0]
    else:
        print("no match:", person)
    pass

# print(find_fellow("Moody", "Rahman"))

# print(fellows)
for mentor_year, mentor_arr in raw_mentor.items():
    # print("====", mentor_year)
    for person in mentor_arr:
        year = find_fellow(person)[2]
        mentor[mentor_year].append((person, year))





# [print(x) for x in mentor.items()]
# [print(k, "\n", v, "\n\n") for k, v in mentor.items()]
# print(fellows)

def calculate_lineage(name, depth=1):
    while depth != 0:
        mentors = mentor[find_fellow(name)[2]]
        return [
            mentors,
            *chain(
                *[calculate_lineage(x[0], depth=depth-1) for x in mentors]
            )]
        pass
    # [print(v) for k, v in mentor.items()]
    return []
    pass

