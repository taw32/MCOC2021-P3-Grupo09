# MCOC2021-P3-Grupo09

Integrantes:
 * Enzo Bertinelli
 * Daniel Morales
 * Tomas Vergara

# ENTREGA 2

Los costos asociados a las rutas están medidos en minutos.

![image](https://user-images.githubusercontent.com/89056734/141026125-53b7139b-e4cc-41a4-9216-8c195f8ce38c.png)

![image](https://user-images.githubusercontent.com/89056734/141026157-27786e96-f662-4ab5-8f91-dd787c19f3b6.png)

![image](https://user-images.githubusercontent.com/89056734/141026183-e2cde269-e4d5-4b2b-869c-926bcdad0a0a.png)

![image](https://user-images.githubusercontent.com/89056734/141026200-cec7b2d7-0b04-405f-89a0-20a4053f6c94.png)

# ENTREGA 3 - Daniel Morales

![Figure_1](https://user-images.githubusercontent.com/88337429/141601874-8e994426-7bee-4810-b04b-a1623108185b.png)

![Figure_2](https://user-images.githubusercontent.com/88337429/141601875-a4e5673b-29b4-4870-9b8d-9c540eb1cea9.png)

Se presenta la imagen generada de la zona donde vivo, ortuzar 140. Junto con la zona del enunciado como ejemplo del funcionamiento del codigo.

# ENTREGA 4


![arcosp3e4](https://user-images.githubusercontent.com/88337429/141875711-918ec6a1-6708-4b6c-a202-55ec527c6583.png)
![arcos2p3e4](https://user-images.githubusercontent.com/88337429/141875716-8c814ab5-2be0-457a-8bd0-05ba0362e9d6.png)

![wardrop1](https://user-images.githubusercontent.com/88337429/141875719-81707188-acb1-4c72-99e4-c5071fafc50d.PNG)
![wardrop2](https://user-images.githubusercontent.com/88337429/141875725-a49be0f6-f945-4b81-8175-aba9ff43af23.PNG)

```Python
while True:
    se_asigno_demanda=False
    for key in OD:
        demanda_actual = OD[key]
        demanda_objetivo=OD_target[key]

        if demanda_actual>0:
            
            path=dijkstra_path(G,key[0],key[1], weight=costo)
            #incrementar flujo en ruta minima
            Nparadas =len(path)
            
            for i_parada in range(Nparadas-1):
                o=path[i_parada]
                d= path[i_parada+1]
                flujo_antes=G.edges[o,d]["flujo"]
                #G.edges[o,d]["flujo"]+=0.1
            #OD[key]-=0.1
                G.edges[o,d]["flujo"]+=OD_target[key]/1000
            OD[key]-=OD_target[key]/1000
            se_asigno_demanda=True
    if not se_asigno_demanda: break
```     

