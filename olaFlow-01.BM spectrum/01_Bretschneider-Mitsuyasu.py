#%%
import numpy as np
import random
import math
#import matplotlib.pyplot as plt

# Modified Bretschneider-Mitsuyasu parameters
Hs = 4.5  # significant wave height
Tp = 15.8  # peak period
n_waves = 250

def mbm(f, Hm0, Tp, df):
    g = 9.81
    method = 'MBM'
    normalize = True
    
    if method == 'MBM':
        E = 0.205 * Hm0**2 * Tp**-4 * f**-5 * np.exp(-0.75 * (Tp * f) ** -4)
        
        if normalize:
            # Use np.trapezoid instead of np.trapz
            corr = Hm0**2 / (16 * np.trapezoid(E, f))  
            E = E * corr
    return E

def generate_waves(n_waves):
    fp = 1.0 / Tp               # 0.2
    f_min = fp / 4.0            # 0.05 
    f_max = fp * 4.0            # 0.8 
    df = (f_max - f_min) / (n_waves - 1)
    f = np.linspace(f_min, f_max, n_waves)  # Frequency range 0.75/200 =0.00375
    spectrum = mbm(f, Hs, Tp, df)

    # Calculate Hm0 using np.trapezoid instead of np.trapz
    Hm0 = 4.004 * math.sqrt(np.trapezoid(spectrum, f))  # Goda book p.40
    print("Hm0:", Hm0)
    idx = np.argsort(-spectrum)[:n_waves]
    wave_heights = np.sqrt(spectrum * df * 2) * 2
    wave_periods = 1 / f        # 266.6667
    wave_phases = [random.uniform(0, 2 * np.pi) for _ in range(n_waves)]

    return wave_heights, wave_periods, wave_phases

# Generate waves
wave_heights, wave_periods, wave_phases = generate_waves(n_waves)

# Write to file in a user-writable directory (e.g., home directory)
output_path = '/home/sik/code/waveDict.txt'  # Adjust the path as needed

with open(output_path, 'w') as f:
    f.write('waveHeights\n')
    f.write(str(len(wave_heights)) + '\n(\n' + '\n'.join(map(str, wave_heights)) + '\n);\n')
    f.write('wavePeriods\n')
    f.write(str(len(wave_periods)) + '\n(\n' + '\n'.join(map(str, wave_periods)) + '\n);\n')
    f.write('wavePhases\n')
    f.write(str(len(wave_phases)) + '\n(\n' + '\n'.join(map(str, wave_phases)) + '\n);\n')
    f.write('waveDirs\n')
    f.write(str(len(wave_phases)) + '\n{\n0\n};\n')

# Plot waveHeight
# plt.plot(wave_heights)
# plt.xlabel('time')
# plt.ylabel('Wave height')
# plt.title('Wave height')
# plt.show()

# Plot wavePeriods
# plt.plot(wave_periods)
# plt.xlabel('time')
# plt.ylabel('Wave periods')
# plt.title('Wave periods')
# plt.show()

# Plot wavePhases
# plt.plot(wave_phases)
# plt.xlabel('time')
# plt.ylabel('Wave elevation')
# plt.title('Wave phase')
# plt.show()
# %%

