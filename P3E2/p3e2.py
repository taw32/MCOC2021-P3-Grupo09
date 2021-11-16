import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G = nx.Graph()

G.add_node("0", pos=[1,2])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])
w=3
f=0

bus=nx.get_node_attributes(G,"pos")

G.add_edge("0","1", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["0"])-np.array(bus["1"]))*60/40)
G.add_edge("0","2", costo=0., color="gray",grosor=w, fcosto=np.linalg.norm(np.array(bus["0"])-np.array(bus["2"]))*60/120)
G.add_edge("0","6", costo=0., color="gray",grosor=w, fcosto=np.linalg.norm(np.array(bus["0"])-np.array(bus["6"]))*60/120)
G.add_edge("2","5", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["2"])-np.array(bus["5"]))*60/40)
G.add_edge("1","2", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["1"])-np.array(bus["2"]))*60/40)
G.add_edge("5","7", costo=0., color="gray",grosor=w, fcosto=np.linalg.norm(np.array(bus["5"])-np.array(bus["7"]))*60/120)
G.add_edge("1","7", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["1"])-np.array(bus["7"]))*60/40)
G.add_edge("1","3", costo=0., color="green",grosor=w, fcosto=np.linalg.norm(np.array(bus["1"])-np.array(bus["3"]))*60/60)
G.add_edge("7","9", costo=0., color="green",grosor=w, fcosto=np.linalg.norm(np.array(bus["7"])-np.array(bus["9"]))*60/60)
G.add_edge("7","3", costo=0., color="green",grosor=w, fcosto=np.linalg.norm(np.array(bus["7"])-np.array(bus["3"]))*60/60)
G.add_edge("3","8", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["3"])-np.array(bus["8"]))*60/40)
G.add_edge("3","6", costo=0., color="saddlebrown",grosor=w, fcosto=np.linalg.norm(np.array(bus["3"])-np.array(bus["6"]))*60/40)
G.add_edge("3","4", costo=0., color="green",grosor=w, fcosto=np.linalg.norm(np.array(bus["3"])-np.array(bus["4"]))*60/60)
G.add_edge("4","8", costo=0., color="gray",grosor=w, fcosto=np.linalg.norm(np.array(bus["4"])-np.array(bus["8"]))*60/120)
G.add_edge("6","4", costo=0., color="gray",grosor=w, fcosto=np.linalg.norm(np.array(bus["6"])-np.array(bus["4"]))*60/120)
G.add_edge("8","9", costo=0., color="green",grosor=w, fcosto=np.linalg.norm(np.array(bus["8"])-np.array(bus["9"]))*60/60)


pos = nx.get_node_attributes(G,"pos")
labels = nx.get_edge_attributes(G,"costo")

#widths=nx.get_edge_attributes(G,"width")

#def funcion_costo(ni, nf, atributos_arco):
#	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
#	return atributos_arco["costo"]
colors = []
widths=[]
for ni, nf in G.edges:
    colors.append(G.edges[ni,nf]["color"])
    widths.append(G.edges[ni,nf]["grosor"])

#colores = []
#edgelist = []
#for ni, nf in G.edges:
#	if ni in ruta and nf in ruta:
#		colores.append("r")
#	else:
#		colores.append("k")
#
#	edgelist.append((ni,nf))

plt.figure()
ax = plt.subplot(1, 1, 1)
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos=pos,edge_color=colors, width=widths)
#nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colores)
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
x=[0,1,2,3,4,5,6,7,8,9,10]
xlabels=["0","1","2","3","4","5","6","7","8","9","10"]
y=[0,1,2,3,4,5,6,7,8,9,10]
ylabels=["0","1","2","3","4","5","6","7","8","9","10"]
plt.xticks(x, xlabels)
plt.yticks(y, ylabels)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.grid(True)

plt.xlabel("X (km)")
plt.ylabel("Y (km)")


plt.show()


####
labels = nx.get_edge_attributes(G,"fcosto")

def funcion_costo(ni, nf, atributos_arco):
	return atributos_arco["fcosto"]
Pares= {1:["0","9"],2:["4","5"],3:["0","4"]}
for i in Pares:
    ruta = nx.dijkstra_path(G, source=Pares[i][0], target=Pares[i][1], weight=funcion_costo)
    
    costo_ruta = 0.
    Nparadas = len(ruta)
    
    #print(f"Ruta Nparadas={Nparadas} ruta: {ruta}")
    for i in range(Nparadas-1):
    	parada_i = ruta[i]
    	parada_f = ruta[i+1]
    	costo_tramo_i = G.edges[parada_i, parada_f]["fcosto"]
    	#print(f"Tramo {i}  {parada_i} a {parada_f} costo={costo_tramo_i}")
    	costo_ruta += costo_tramo_i
    
    #print(f"Costo de ruta = {costo_ruta}")
        
    colores = []
    edgelist = []
    widths= []
    for ni, nf in G.edges:
        if ni in ruta and nf in ruta:
            colores.append("r")
            widths.append(3)
        else:
            colores.append("k")
            widths.append(1)
        edgelist.append((ni,nf))
    
    plt.figure()
    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_labels(G, pos=pos)
    nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colores, width=widths)
   # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    x=[0,1,2,3,4,5,6,7,8,9,10]
    xlabels=["0","1","2","3","4","5","6","7","8","9","10"]
    y=[0,1,2,3,4,5,6,7,8,9,10]
    ylabels=["0","1","2","3","4","5","6","7","8","9","10"]
    plt.xticks(x, xlabels)
    plt.yticks(y, ylabels)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.grid(True)
    
    plt.xlabel("X (km)")
    plt.ylabel("Y (km)")
    plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
    
    plt.show()