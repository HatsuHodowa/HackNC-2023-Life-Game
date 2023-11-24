import ModelQ

m = ModelQ.Model(5, 5)

m.setCell(1, 0, 1)

m.setCell(1, 1, 1)
m.setCell(1, 2, 1)

m.print()

for k in range(20):
    print(str(k) + " th")
    m.cellUpdate()
    m.print()