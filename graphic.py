import networkx as nx
import matplotlib.pyplot as plt

def ploting(sec, solution):
    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar los vértices con sus sec correspondientes
    if solution[1]:
        for i in range(len(sec)):
            G.add_node(i+1, degree=sec[i])

        # Agregar aristas al grafo
        for i in range(len(sec)):
            for j in range(i+1, len(sec)):
                if sec[i] > 0 and sec[j] > 0:
                    G.add_edge(i+1, j+1)

        # Definir la posición de los nodos
        pos = nx.spring_layout(G, seed=42)

        # Obtener los colores de los nodos según su grado
        colores = [nodo[1]['degree'] for nodo in G.nodes(data=True)]

        # Dibujar el grafo sin etiquetas de los nodos
        nx.draw_networkx(G, pos, node_size=1000, node_color=colores, cmap='Accent_r', with_labels=False, edgecolors='k')

        # Agregar un borde negro alrededor de cada nodo
        node_collection = nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colores, cmap='Accent_r', edgecolors='k')
        node_collection.set_edgecolor('black')

        # Ajustar los límites del gráfico y ocultar los ejes
        plt.xlim((-2, 2))
        plt.ylim((-2, 2))
        plt.axis('off')
        font = {'family': 'serif',
            'color':  'black',
            'weight': 'normal',
            'size': 16,
            }
        # Mostrar el grafo
        plt.title('Grafo gráfico', fontdict=font, fontsize=20)
        plt.show()