import scipy.constants as const

def larmor_power(charge, acceleration):
  
    epsilon_0 = const.epsilon_0  
    c = const.c
    power = (charge**2 * acceleration**2) / (6 * const.pi * epsilon_0 * c**3)
    return power


if __name__ == "__main__":
    charge = 1.602e-19  
    acceleration = 1e18 

    radiated_power = larmor_power(charge, acceleration)
    print(f"The power radiated by the particle is {radiated_power:.3e} watts.")