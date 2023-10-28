import Model

m = Model.Model(3, 3)

m.setCell(0, 0, 1)
m.setCell(1, 0, 1)
m.setCell(0, 1, 1)
m.setCell(1, 1, 1)

m.print()

m.cellUpdate()
print("update")
m.print()