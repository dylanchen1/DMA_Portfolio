a = [[1, 2, 3], [4, 5, 6]]
#print(a[0])
emptyList = []
list = ["thing", 3123, "dylan", 22.4]
#print(list[3])

grid = [['S', 'F', 'F', 'F',], ['F', 'H', 'F', 'H'], ['F', 'F', 'F', 'H'], ['H', 'F', 'F', 'G']]
x = 4
for i in range(x):
    print(grid[i])

#SFFF
#FHFH
#FFFH
#HFFG

gridTwo = [[1,2,3,4], [5,6], [7,8,9]]
for i in range(len(gridTwo)):
    for j in range(len(gridTwo[i])):
        print(gridTwo[i][j])
    print(" ")