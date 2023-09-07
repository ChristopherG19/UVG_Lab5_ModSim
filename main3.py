import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definición de la clase Buyer para representar diferentes segmentos de compradores.
class Buyer:
    def __init__(self, buyer_id, preference):
        self.buyer_id = buyer_id  # Identificador único para cada comprador
        self.preference = preference
        self.budget = random.uniform(50, 150)  # Presupuesto inicial aleatorio
        self.price_sensitivity = random.uniform(0.1, 0.7)  # Sensibilidad al precio aleatoria
        self.price = 0  # Precio actual

    def purchase(self):
        # Decide si comprar o no en función de la diferencia entre el precio y la preferencia.
        willingness_to_pay = self.preference * (1 - self.price_sensitivity)
        if self.price <= willingness_to_pay and self.budget >= self.price:
            self.budget -= self.price
            return True
        else:
            return False

    def update_price(self, market_demand, market_supply):
        # Ajusta el precio en función de la oferta y la demanda.
        excess_demand = market_demand - market_supply
        if excess_demand > 0:
            # Aumentar el precio si la demanda supera la oferta.
            self.price += random.uniform(1, 5)  # Incremento aleatorio
        elif excess_demand < 0:
            # Reducir el precio si la oferta supera la demanda.
            self.price -= random.uniform(1, 5)  # Decremento aleatorio
            if self.price < 0:
                self.price = 0  # Evitar precios negativos

# Subclase de Buyer para compradores de lujo.
class LuxuryBuyer(Buyer):
    def __init__(self, buyer_id):
        
        super().__init__(buyer_id, preference=random.uniform(0.7, 1.0))  # Preferencia alta

# Subclase de Buyer para compradores de presupuesto.
class BudgetBuyer(Buyer):
    def __init__(self, buyer_id):
        super().__init__(buyer_id, preference=random.uniform(0.1, 0.4))  # Preferencia baja

# Función para simular el mercado con múltiples compradores.
def simulate(num_buyers, num_steps):
    luxury_buyers = [LuxuryBuyer(i) for i in range(num_buyers // 2)]
    budget_buyers = [BudgetBuyer(i) for i in range(num_buyers // 2)]

    fig, ax = plt.subplots()

    market_prices = []  # Lista para registrar los precios en cada paso

    def update(frame):
        market_demand = sum(buyer.preference for buyer in luxury_buyers + budget_buyers)
        market_supply = random.uniform(0.8 * market_demand, 1.2 * market_demand)

        for buyer in luxury_buyers + budget_buyers:
            buyer.update_price(market_demand, market_supply)
            if buyer.purchase():
                market_prices.append((buyer.buyer_id, buyer.price))  # Registra el identificador y el precio

        ax.clear()
        prices = [price for _, price in market_prices]  # Extrae los precios
        ax.hist(prices, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel("Precio")
        ax.set_ylabel("Cantidad de Compras")
        ax.set_title(f"Paso de Simulación: {frame}")

    ani = FuncAnimation(fig, update, frames=num_steps, repeat=False, interval=500)
    plt.show()

# Simulación con 100 compradores y 50 pasos.
simulate(num_buyers=100, num_steps=50)

### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

¿Qué comportamientos puede observar en los diferentes tipos de preferencias y estrategias?
Compradores de Lujo (preferencia alta): Compran productos a precios más altos y son menos sensibles a las fluctuaciones de precios.
Compradores de Presupuesto (preferencia baja): Son más selectivos y solo compran productos cuando los precios son bajos y se ajustan a sus preferencias.
Estrategias de Precios Dinámicos: Los precios aumentan cuando la demanda supera la oferta y disminuyen cuando ocurre lo contrario.

¿Cómo mejoraría este modelo?
- Segmentación más detallada: Agregar más segmentos de compradores con diferentes preferencias y estrategias.
- Interacción entre compradores y vendedores: Incluir vendedores que ajusten sus precios en respuesta a la demanda y la competencia.
- Consideración de la reputación: Introducir la reputación como factor que influye en las decisiones de compra.
- Visualización más detallada: Incluir gráficos adicionales que muestren la evolución de los precios y la oferta y la demanda.
- Optimización de parámetros: Ajustar los parámetros del modelo para obtener resultados más realistas.
- Análisis de resultados: Implementar métricas de evaluación y análisis para una comprensión más profunda de los efectos en el mercado.

'''
### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------