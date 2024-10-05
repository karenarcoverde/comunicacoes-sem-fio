import numpy as np  # Para cálculos matemáticos e operações com arrays
import matplotlib.pyplot as plt  # Para geração de gráficos

# Dados fornecidos
ht = 50  # Altura da antena transmissora
hr = 2  # Altura da antena receptora
f = 900e6  # Frequência em Hz
c = 3e8  # Velocidade da luz em m/s
lambda_wave = c / f  # Comprimento de onda
GR = [1, 0.316, 0.1, 0.01]  # Ganhos da antena receptora
Gt = 1  # Ganho da antena transmissora
R = -1  # Coeficiente de reflexão
d = np.arange(1, 100001)  # Distância de 1 a 100 km

# Cálculo das distâncias
d0 = np.sqrt(d**2 + (ht - hr)**2)  # Distância direta (LOS)
d1 = np.sqrt(d**2 + (ht + hr)**2)  # Distância refletida
phd = 2 * np.pi / lambda_wave * (d1 - d0)  # Diferença de fase
dc = 4 * ht * hr / lambda_wave  # Distância crítica

# Inicializar o gráfico
plt.figure(figsize=(10, 10))

# Loop para diferentes valores de Gr
for counter in range(4):
    Gr = GR[counter]
    
    # Cálculo do vetor complexo
    Vec = np.sqrt(Gt) / d0 + R * np.sqrt(Gr) / d1 * np.exp(-1j * phd)
    
    # Potência recebida (Pr)
    Pr = (lambda_wave / (4 * np.pi))**2 * np.abs(Vec)**2
    
    # Subplot para cada Gr
    plt.subplot(3, 2, counter + 1)
    
    # Plotar a potência normalizada - pega o Pr com d=1m (primeiro valor do gráfico)
    plt.plot(10 * np.log10(d), 10 * np.log10(Pr) - 10 * np.log10(Pr[0]), label='Pr(d)')
    
    # Marcar a distância crítica (dc) com uma linha vertical vermelha
    plt.axvline(x=10 * np.log10(dc), color='red', linestyle='--', label='Critical distance (dc)')
    
    # Configurar título e legenda
    plt.title(f'Gr = {Gr}')
    plt.xlabel('10*log10(d)')
    plt.ylabel('10*log10(Pr)')
    plt.legend()
    plt.grid(True)

# Exibir o gráfico ajustado
plt.tight_layout()
plt.show()