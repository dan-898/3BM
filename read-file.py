
import pyvista as pv
from pyvista import examples


filename = examples.planefile
filename




mesh = pv.read(filename)
cpos = mesh.plot()



plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh)
plotter.show(screenshot="twocube.city.json")



mesh.points



lst3 = ["ali", "baba", "forty", "thieves", "maarten", "jonathan", "3BM"]

lst4 = []
for i in lst2:
    lst5 = []

    for j in i:
        lst6 = []

        for k in j:
            lst6.append(lst3[k])
        lst5.append(lst6)
        lst4.append(lst6)

print(lst4)
