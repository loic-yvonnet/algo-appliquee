
def display_tower(tower, index):
    content = ", ".join([str(i) for i in tower])
    print(f"tower{index}: {content}")

iterations = 0
def display_towers(towers):
    global iterations
    print(f"--- {iterations}")
    iterations += 1

    for i, tower in enumerate(towers, start=1):
        display_tower(tower, i)

def move_cylinder(towers, from_tower, to_tower):
    disk = towers[from_tower].pop()
    towers[to_tower].append(disk)
    display_towers(towers)

def move(towers, depth, from_tower, intermediary_tower, to_tower):
    if (depth == 1):
        # Recursion end: just move the cylinder from the origin to the target
        move_cylinder(towers, from_tower, to_tower)
    else:
        # Move the whole stack but the largest cylinder to the intermediary tower recursively
        move(towers, depth-1, from_tower, to_tower, intermediary_tower)

        # Move the largest cylinder to the target tower
        move_cylinder(towers, from_tower, to_tower)

        # Move the stack of cylinders from intermediary to the target tower recursively
        move(towers, depth-1, intermediary_tower, from_tower, to_tower)

def solve_hanoi(nb_disks):
    towers = [
        list(range(nb_disks,0,-1)),
        [],
        []
    ]
    display_towers(towers)

    move(towers, nb_disks, 0, 1, 2)
    
def init_hanoi():
    nb_disks = 3 #int(input("Number of disks: "))
    if nb_disks < 1:
        print("Error: invalid number of disks (must be greater or equal to 1)")

    solve_hanoi(nb_disks)

if __name__ == "__main__":
    init_hanoi()