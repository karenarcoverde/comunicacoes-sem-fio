import numpy as np
import matplotlib.pyplot as plt

# Definindo as constantes e parâmetros
gamma = 2  # Expoente de perda de caminho
R = 1  # Raio da célula
D_values = np.linspace(0.1, 10, 500)  # Distância de reuso de 0.1 a 10 (evitamos 0 para não causar divisão por zero)
P = 1  # Probabilidade de interferente estar em cada uma das localizações

# Função de eficiência espectral da área (ASE)
def area_spectral_efficiency(D, R, gamma, interferer_distance, is_farther):
    if is_farther:  # Se o interferente está além da célula de interesse, somamos a distância
        interference = ((D + interferer_distance) ** gamma) / (6 * R**2)
    else:  # Caso contrário, subtraímos a distância (para interferentes dentro da célula)
        interference = ((D - interferer_distance) ** gamma) / (6 * R**2)
    
    # Calcula a eficiência espectral da área (ASE)
    ase = np.log2(1 + interference) / (np.pi * (0.5 * D)**2)
    return ase

# Definindo as distâncias dos interferentes e se estão além da célula de interesse
distances_scenarios = {
    "Closest boundary": (R, False),  # Interferente na fronteira mais próxima (D - R)
    "Halfway closest boundary": (R / 2, False),  # Meio caminho até a fronteira mais próxima (D - R/2)
    "Cell center": (0, False),  # Interferente no centro da célula
    "Farthest boundary": (R, True),  # Interferente além da célula (D + R)
    "Halfway farthest boundary": (R / 2, True)  # Meio caminho além da célula (D + R/2)
}

# Plotando o gráfico para cada cenário de interferência
plt.figure(figsize=(8, 6))

for scenario, (dist, is_farther) in distances_scenarios.items():
    ase = P * area_spectral_efficiency(D_values, R, gamma, dist, is_farther)
    plt.plot(D_values, ase, label=f"{scenario} (ponderada)")

plt.title('Area Spectral Efficiency at distance D (γ = 2)')
plt.xlabel('Reuse Distance (D)')
plt.ylabel('Area Spectral Efficiency (ASE) [bps/Hz/m^2]')
plt.legend()
plt.grid(True)
plt.show()
