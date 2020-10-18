#by Zanorashe Abel Manzvera
rows = int(input("how many rows do you require? "))
columns = int(input("how many columns do you want? "))

def draw_board(rows, columns):
    def print_boxes():
        for column in range(1, (2*columns)+2): # taken from iteration from box components check below
            if column != ((2*columns)+1):
                if column%2 == 1:
                    print("|", end=" ")
                else:
                    print("__", end=" ")
            else: print("|")

    while rows > 0:
        print_boxes()
        rows -= 1

    return

draw_board(rows, columns)

"""
|__| = 3 ..........................1 box
|__|__| = 5 .......................2 boxes
|__|__|__| = 7.....................3 boxes
etc = etc

therefore 1 box = 3 parts
          2 boxes = 5 parts

so        1 = 1+2*1
          2 = 1+2*2
          X = 1+2*X

but here the last number is not included range(1, 3) takes values 1, 2 and not 3
to include 3 we change the formular to X = 1+1+2*X which is X = 2+2*columns above
"""
