
from pyswip import Prolog

prolog = Prolog()
prolog.assertz("padre(juan,maria)")
prolog.assertz("padre(pablo,juan)")
prolog.assertz("padre(pablo,marcela)")
prolog.assertz("padre(carlos,debora)")
for e in prolog.query("padre(X,Y)"):
    print(e["X"], "es el padre de", e["Y"])