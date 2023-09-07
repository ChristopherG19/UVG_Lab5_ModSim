import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definición de la clase Agent para representar tanto depredadores como presas.
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Implementa el movimiento básico de un agente.
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)

# Definición de la clase Predator (Depredador) con subclases para diferentes tipos de depredadores.
class Predator(Agent):
    def __init__(self, x, y, behavior):
        super().__init__(x, y)
        self.behavior = behavior

    def move(self, preys):
        # Implementa el movimiento del depredador según su comportamiento.
        if self.behavior == "cazador":
            # El cazador persigue a la presa más cercana.
            if preys:
                closest_prey = min(preys, key=lambda prey: ((prey.x - self.x) ** 2 + (prey.y - self.y) ** 2) ** 0.5)
                self.x += (closest_prey.x - self.x) / 10
                self.y += (closest_prey.y - self.y) / 10
        elif self.behavior == "emboscador":
            # El depredador emboscador se queda en su posición y espera a su presa.
            pass

# Función para simular la interacción entre depredadores y presas.
def simulate(num_predators, num_preys, num_obstacles, num_steps):
    predators = [Predator(random.uniform(0, 10), random.uniform(0, 5), random.choice(["cazador", "emboscador"])) for _ in range(num_predators)]
    preys = [Agent(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_preys)]
    obstacles = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_obstacles)]

    fig, ax = plt.subplots()

    def update(frame):
        nonlocal preys
        if not preys:
            ani.event_source.stop()
            plt.close()
            return

        for predator in predators:
            predator.move(preys)
        for prey in preys:
            prey.move()

        # Lógica para detectar y manejar interacciones entre depredadores y presas.
        for predator in predators:
            for prey in preys:
                if ((prey.x - predator.x) ** 2 + (prey.y - predator.y) ** 2) ** 0.5 < 0.5:
                    preys.remove(prey)

        ax.clear()
        for predator in predators:
            ax.scatter(predator.x, predator.y, c="red", label="Predator")
        for prey in preys:
            ax.scatter(prey.x, prey.y, c="blue", label="Prey")
        for obstacle in obstacles:
            ax.scatter(obstacle[0], obstacle[1], c="gray", marker="X")

        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

    ani = FuncAnimation(fig, update, frames=num_steps, repeat=False, interval=100)
    plt.show()

# Simulación con 100 pasos, 2 depredadores, 5 presas y 3 obstáculos.
simulate(num_predators=3, num_preys=15, num_obstacles=3, num_steps=200)


### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

¿Qué comportamientos puede observar en los depredadores?
En esta simulación, hemos modelado dos tipos de comportamientos para los depredadores: "cazadores" y "emboscadores". 
Los cazadores persiguen activamente a sus presas, mientras que los emboscadores permanecen en su posición y esperan a sus presas.

¿Cómo mejoraría este modelo?
- Agregar más tipos de depredadores con comportamientos únicos.
- Implementar una lógica más sofisticada para las interacciones entre depredadores y presas, como la detección de proximidad y estrategias de caza.
- Incluir una representación más realista de obstáculos y cómo afectan los movimientos de los agentes.
- Utilizar una biblioteca de visualización más avanzada para crear una simulación más atractiva y comprensible.
- Experimentar con diferentes parámetros y reglas para observar cómo afectan el resultado de la simulación.

'''
### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------