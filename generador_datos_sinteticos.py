import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Decay:
	noise = lambda self, arr,x:np.random.randn(arr.shape[0])*x
	def __init__ (self, timeframe=20, concentracion_inicial=1):
		self.tiempo=np.linspace(.001,timeframe*2, 70)
		self.constante=((1/timeframe)*1.1 - (1/timeframe)*.9) * np.random.random() + 1/timeframe*.9
		self.sigma=.01
		self.concentracion_inicial=concentracion_inicial
	def orden_cero(self):
		cinetica = self.concentracion_inicial - self.constante*self.tiempo + self.noise(self.tiempo,self.sigma)
		return np.hstack([self.tiempo[cinetica>0].reshape(-1,1),cinetica[cinetica>0].reshape(-1,1)])
	def orden_uno(self):
		cinetica = self.concentracion_inicial * np.exp(-self.constante*self.tiempo) + self.noise(self.tiempo, self.sigma)
		return np.hstack([self.tiempo[cinetica>0].reshape(-1,1),cinetica[cinetica>0].reshape(-1,1)])
	def orden_dos(self):
		cinetica= (self.constante*self.tiempo + (1/self.concentracion_inicial))**(-1) + self.noise(self.tiempo, self.sigma)
		return np.hstack([self.tiempo[cinetica>0].reshape(-1,1),cinetica[cinetica>0].reshape(-1,1)])
	
def main():
	decay=Decay()
	kins=[decay.orden_cero(), decay.orden_uno(), decay.orden_dos()]
	choice=np.random.choice(range(len(kins)))
	chosen_kin=kins.pop(choice)
	df=pd.DataFrame(chosen_kin, columns=['tiempo (m)', 'concentración'])
	return df,choice


if __name__ == '__main__':
	main()