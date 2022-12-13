
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



mesh.faces.reshape(-1, 4)[:, 1:]



mesh = examples.download_cad_model()
cpos = [(107.0, 68.5, 204.0), (128.0, 86.5, 223.5), (0.45, 0.36, -0.8)]
mesh.plot(cpos=cpos)


mesh = examples.download_doorman()
mesh.plot(cpos="xy")



mesh = examples.download_teapot()
mesh.plot(cpos=[-1, 2, -5], show_edges=True)



mesh = examples.download_bunny_coarse()
cpos = [(0.2, 0.3, 0.9), (0, 0, 0), (0, 1, 0)]
mesh.plot(cpos=cpos, show_edges=True, color=True)
