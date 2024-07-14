import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize, root_scalar
import pandas as pd
import math

# Functions for b_r and b_0
def b_r(tau, lambda_r):
    return (1 / lambda_r) * (np.exp(-lambda_r * tau) - 1)

def b_0(tau, lambda_r, r_bar, sigma_r):
    C = 3 * sigma_r**2 / (4 * lambda_r**3)
    term1 = r_bar * ((np.exp(-lambda_r * tau) - 1) / lambda_r + tau)
    term2 = -sigma_r**2 * np.exp(-2 * lambda_r * tau) / (4 * lambda_r**3)
    term3 = sigma_r**2 * np.exp(-lambda_r * tau) / (lambda_r**3)
    term4 = sigma_r**2 * tau / (2 * lambda_r**2)
    return term1 + term2 + term3 + term4 + C

# Functions for phi_r, phi_delta, and phi_0
def phi_r(tau, lambda_r):
    return (1 - np.exp(-lambda_r * tau)) / lambda_r

def phi_delta(tau, lambda_delta):
    return (-1 + np.exp(-lambda_delta * tau)) / lambda_delta

def sigma_r_t(t):
    return np.sqrt(0.000529 * t * 10**-4)

def sigma_delta_t(t):
    return np.sqrt(0.000144 * t * 10**-4)

def rho_rdelta_t():
    return 0.00003312 / math.sqrt(0.000529 * 0.000144)

def rho_rTheta_t():
    return 0.44712 / math.sqrt(0.000529 * 576)

def rho_Thetadelta_t():
    return 0.08352 / math.sqrt(576 * 0.000144)

def rho_Odelta_t(t):
    return 0.08325 * t * 10**-4

def sigma_O_t(t):
    return np.sqrt(0.0576 * t)

def phi_0(tau, lambda_r, lambda_delta, r_bar, delta_bar):
    integrand = lambda s: (
        phi_r(s, lambda_r) * lambda_r * r_bar +
        phi_delta(s, lambda_delta) * lambda_delta * delta_bar +
        0.5 * (
            phi_r(s, lambda_r)**2 * sigma_r_t(s)**2 +
            phi_delta(s, lambda_delta)**2 * sigma_delta_t(s)**2 +
            phi_r(s, lambda_r) * rho_rTheta_t() * sigma_r_t(s) +
            phi_r(s, lambda_r) * phi_delta(s, lambda_delta) * rho_rdelta_t() * sigma_r_t(s) * sigma_delta_t(s) +
            rho_Thetadelta_t() * phi_delta(s, lambda_delta) * sigma_delta_t(s)
        )
    )
    return np.array([integrand(s) for s in np.linspace(0, tau, 100)]).sum() * (tau / 100)

def delta_t(t, delta_0, lambda_delta, delta_bar, sigma_delta):
    return delta_0 * np.exp(-lambda_delta * t) + delta_bar * (1 - np.exp(-lambda_delta * t)) + sigma_delta * np.sqrt((1 - np.exp(-2 * lambda_delta * t)) / (2 * lambda_delta))
