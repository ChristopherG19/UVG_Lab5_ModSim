import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definición de la clase Vehicle para representar diferentes tipos de vehículos.
class Vehicle:
    def __init__(self, lane, speed, behavior):
        self.lane = lane
        self.speed = speed
        self.behavior = behavior
        self.position = random.uniform(0, 10)  # Posición inicial aleatoria en la carretera

    def move(self):
        # Implementa el movimiento básico de un vehículo.
        self.position += self.speed
        self.change_lane()  # Llamamos a la función de cambio de carril en cada actualización

    def change_lane(self):
        # Implementa el cambio de carril del vehículo (puede ser sobrescrito en subclases).
        pass

# Subclase de Vehicle para vehículos agresivos que cambian de carril con frecuencia.
class AggressiveVehicle(Vehicle):
    def change_lane(self):
        # Los vehículos agresivos cambian de carril con mayor frecuencia.
        if random.random() < 0.2:  # Probabilidad de cambiar de carril: 20%
            self.lane = random.randint(0, 2)  # Cambia de carril entre 0, 1 o 2

# Subclase de Vehicle para vehículos cautelosos que mantienen una distancia segura.
class CautiousVehicle(Vehicle):
    def change_lane(self):
        # Los vehículos cautelosos cambian de carril con menor frecuencia.
        if random.random() < 0.1:  # Probabilidad de cambiar de carril: 10%
            self.lane = random.randint(0, 2)  # Cambia de carril entre 0, 1 o 2

# Función para simular el flujo de tráfico con múltiples carriles y cerrar cuando no haya vehículos en pantalla.
def simulate(num_vehicles, num_lanes, num_steps):
    vehicles = [None] * num_vehicles

    # Inicializa vehículos con diferentes comportamientos y carriles.
    for i in range(num_vehicles):
        lane = random.randint(0, num_lanes - 1)  # Carril aleatorio entre 0 y num_lanes-1
        speed = random.uniform(0.5, 2.0)  # Velocidad aleatoria
        behavior = random.choice([AggressiveVehicle, CautiousVehicle])  # Comportamiento aleatorio
        vehicles[i] = behavior(lane, speed, behavior)

    fig, ax = plt.subplots()

    def update(frame):
        for vehicle in vehicles:
            vehicle.move()

        ax.clear()
        for vehicle in vehicles:
            ax.scatter(vehicle.position, vehicle.lane, c="blue" if isinstance(vehicle, CautiousVehicle) else "red", marker=">")
            
        ax.set_xlabel("Posición")
        ax.set_ylabel("Carril")
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.5, num_lanes - 0.5)
        ax.set_yticks(range(num_lanes))
        ax.set_yticklabels([f"Carril {i}" for i in range(num_lanes)])
        plt.pause(0.5)  # Hacemos la simulación más lenta
        plt.draw()
        
        # Verificar si todos los vehículos han llegado al final de la carretera y cerrar si es el caso.
        if all(vehicle.position >= 10 for vehicle in vehicles):
            plt.close(fig)

    ani = FuncAnimation(fig, update, frames=num_steps, repeat=False, interval=100)
    plt.show()

# Simulación con 30 vehículos, 4 carriles y 100 pasos.
simulate(num_vehicles=30, num_lanes=4, num_steps=100)

### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

¿Qué comportamientos puede observar en los diferentes tipos de comportamiento de manejo de vehículos?
Vehículos agresivos: Cambian de carril con frecuencia, a menudo intentando adelantar a otros vehículos y superarlos.
Vehículos cautelosos: Cambian de carril con menos frecuencia y mantienen una distancia segura con respecto a otros vehículos.

¿Cómo mejoraría este modelo?
- Agregando más comportamientos de manejo de vehículos y ajustando sus parámetros.
- Introducir condiciones de tráfico más realistas, como la congestión y las interacciones con semáforos y señales de tráfico.
- Considerar factores ambientales como el clima y su influencia en la velocidad y la visibilidad de los vehículos.
- Implementar una lógica más avanzada para el cambio de carril, considerando la velocidad y la posición de otros vehículos.
- Agregar más detalles de visualización, como gráficos de velocidad y distancia entre vehículos.

'''
### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------