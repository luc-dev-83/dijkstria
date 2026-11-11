def initialiserBrancheNoeud(l1,l2):
	for loop in l1:
		loop.setCouleur("black")
	for loop in l1:
		loop.setCouleur("black")

def plusCourtCheminDijkstra(model):
	for loop in model.getListeNoeuds():
		loop.setStyle(0)
	model.setListeDeuxNoeuds(-1,-1)


