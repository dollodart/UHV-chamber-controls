density=5.61 # g/cm^3
mol_mass=81.4 # g/mol
area=0.5*1 #cm^3
thickness=0.4e-1 #cm
volume=area*thickness
emissivity=0.98
R=8.314 # J/(mol K)
heat_capacity=3*R/mol_mass # J/(mol K), order of magnitude estimate by Dulong-Petit
#inclusion of molecular mass gives divergent heat
sigma=5.67e-12 # W/(cm^2 K^4)
T_inf=273+25 #K
U=0.005 #overall heat transfer coefficient, W/K
thermal_inertia=density*heat_capacity*volume
radiant_U=sigma*area*emissivity
