import numpy as np
from numpy.linalg import eig

def market_equilibrium(market_share = [.4, .6], switch_prob = [[.8, .2],[.1, .9]]):
	# x = np.array(market_share)
	# switch_prob = np.array(switch_prob)
	# S, U = eig(switch_prob.T)
	# stationary = np.array(U[:, np.where(np.abs(S - 1.) < 1e-8)[0][0]].flat)
	# stationary = stationary / np.sum(stationary)	
	# return np.round(stationary, 2)
	for i in range(30):
		market_share = np.dot(market_share, switch_prob)
	return market_share


if __name__ == "__main__":
	print(market_equilibrium())