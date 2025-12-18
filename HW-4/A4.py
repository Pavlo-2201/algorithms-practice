n = int(input())
parent_map = {}
all_people = set()

for _ in range(n-1):
    child, parent = input().split()
    parent_map[child] = parent
    all_people.add(child)
    all_people.add(parent)

height_map = {}


def fh(person,parent_map,height_map):
    if person in height_map:
        return height_map[person]


    if person not in parent_map:
        height_map[person] = 0
        return 0

    parent = parent_map[person]
    parent_height = fh(parent,parent_map,height_map)
    height_map[person] = parent_height + 1
    return parent_height + 1



for person in all_people:
    if person not in height_map:
        fh(person,parent_map,height_map)

sorted_people = sorted(all_people)

for person in sorted_people:
    print(person, height_map[person])