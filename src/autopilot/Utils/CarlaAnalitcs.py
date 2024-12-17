import glob
import os
import time
from matplotlib import pyplot as plt
import json

class CarlaAnalytics:
  '''
  This class is responsible for the analytics of the Carla simulation

  ---- O que eu espero que essa classa faça ----

  - armazene quantas veses cada placa de transito foi identificada
  - plote um grafico com a quantidade de cada placa de transito identificada 
  - Armazena a velocidade em cada frame
  - Plota um grafico com a velocidade em cada frame

  '''
  def __init__(self):
  #    'back',
  # 'speed_30',
  # 'speed_60',
  # 'speed_90',
  # 'stop'

    # Cada execucao gera uma nova pasta run_{index}
    # O index é auto incrementado
    self.run_index = len(glob.glob("_output/analytics/run_*"))
    self.run_folder = f'_output/analytics/run_{self.run_index}'
    os.makedirs(self.run_folder, exist_ok=True)


    # um data analytics com dois campos {traffic_signs: {placa1: quantidade1, placa2: quantidade2, ...}, speed: [velocidade1, velocidade2, ...]}
    # esse json é salvo no final da execucao
    self.data_analytics = {
      'traffic_signs': {
        'back': 0,
        'speed_30': 0,
        'speed_60': 0,
        'speed_90': 0,
        'stop': 0
      },
      'speed': [],
      "initial_time": 0.0,
      "final_time": 0.0,
      "time": 0.0
    }


  def update_traffic_signs(self, traffic_sign):
    '''
    Atualiza a quantidade de cada placa de transito identificada
    '''
    self.data_analytics['traffic_signs'][traffic_sign] += 1

  def plot_traffic_signs(self):
    '''
    Salva um grafico com a quantidade de cada placa de transito identificada
    Coloca a quantidade de cada placa de transito acima da barra
    Salva no json {placa1: quantidade1, placa2: quantidade2, ...}
    '''

    plt.figure()
    plt.title('Placas de transito identificadas')
    plt.xlabel('Placas de transito')
    plt.ylabel('Quantidade')

    for i, value in enumerate(self.data_analytics['traffic_signs'].values()):
      plt.text(i, value, str(value), ha='center')

    plt.bar(self.data_analytics['traffic_signs'].keys(), self.data_analytics['traffic_signs'].values())
    plt.savefig(f'{self.run_folder}/traffic_signs_analysis.png')
    plt.close()

  def update_speed(self, speed):
    '''
    Atualiza a lista de velocidades
    '''
    self.data_analytics['speed'].append(speed)

  def plot_speed(self):
    '''
    Salva um grafico com a velocidade em cada frame na pasta _output/analytics
    O nome da imagem é auto incrementado
    Salva um JSON com as informações da velocidade {speed: [velocidade1, velocidade2, ...]}
    '''

    file_name = f'{self.run_folder}/speed_analysis'

    plt.figure(figsize=(10, 6))
    plt.plot(self.data_analytics['speed'], label="Velocidade (km/h)", color="blue")
    plt.title("Velocidade do veículo durante o percurso")
    plt.xlabel("Tempo (frames)")
    plt.ylabel("Velocidade (km/h)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{file_name}.png')
    plt.close()

  def set_initial_time(self):
    '''
    Atualiza o tempo de execução para now
    '''
    self.data_analytics['initial_time'] = int(time.time() * 1000)

  def set_final_time(self):
    '''
    Atualiza o tempo de execução
    '''
    self.data_analytics['final_time'] = int(time.time() * 1000)

  def save_data_analytics(self):
    '''
    Salva o JSON com as informações da execução e os gráficos
    '''
    try:
      self.plot_speed()
      self.plot_traffic_signs()
      self.data_analytics['time'] = self.data_analytics['final_time'] - self.data_analytics['initial_time']
      with open(f'{self.run_folder}/data_analytics.json', 'w') as f:
        json_data = json.dumps(self.data_analytics, indent=4)
        f.write(json_data)
      print('Data analytics saved successfully')
    except Exception as e:
      print(f'Error saving data analytics: {e}')
