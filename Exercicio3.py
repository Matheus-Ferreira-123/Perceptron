# Importando biblioteca
from sklearn.linear_model import Perceptron

# Dados de entrada
X = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [0,0,1,0], [1,1,1,1], [0,1,0,0], [1,0,0,1], [0,0,0,1]]

# Saídas desejadas
Y = [0, 1, 0, 1, 1, 0, 0, 0]

# Criando e treinando o perceptron
modelo = Perceptron()
modelo.fit(X, Y)

# Testando o modelo
print("Previsões:")
testes = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [0,0,1,0], [1,1,1,1], [0,1,0,0], [1,0,0,1], [0,0,0,1]]
for teste in testes:
  previsao = modelo.predict([teste])
  print(f"Cansado do Trabalho: {teste[0]}, Ingredientes em Casa: {teste[1]}, restaurante aberto:{teste[2]},Dia do pagamento recente:{teste[3]} => ir ao restaurante? {'Sim' if previsao[0] == 1 else 'Não'}")
