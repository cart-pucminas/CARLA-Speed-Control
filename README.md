# Projeto de Controle de Velocidade de Veículo Autônomo com Detecção de Placas de Trânsito

Este projeto propõe uma solução para o controle de velocidade de um veículo autônomo utilizando computação visual para detecção e classificação de imagens de sinalização de trânsito. A solução foi desenvolvida no simulador CARLA, uma plataforma de simulação para testes de veículos autônomos, e utiliza redes neurais treinadas com o modelo YOLO para detectar e classificar placas de trânsito.

## Objetivo

O principal objetivo deste projeto é implementar um sistema de controle de velocidade que responda de forma rápida e assertiva às sinalizações de trânsito, garantindo uma direção mais segura. A solução foi integrada ao algoritmo de piloto automático do CARLA e validada em um mapa da cidade 01 do simulador, com diferentes rotas e placas de sinalização ao longo do trajeto.

## Funcionalidades

- **Detecção e Classificação de Placas de Trânsito:** Utilização do modelo YOLO para identificar e classificar as placas de trânsito.
- **Controle de Velocidade:** O sistema ajusta a velocidade do veículo autônomo com base nas placas de trânsito detectadas durante o trajeto.
- **Integração com o CARLA:** A solução é integrada ao simulador CARLA, permitindo a execução de testes realistas em ambientes virtuais.
- **Modo de Validação:** Comparação do desempenho do sistema de controle de velocidade com o piloto automático do CARLA, com o módulo ativo e desativado.

## Tecnologias Utilizadas

- **YOLO (You Only Look Once):** Modelo de rede neural para detecção de objetos em tempo real, utilizado para detectar as placas de trânsito.
- **CARLA:** Simulador de código aberto para testes de veículos autônomos, utilizado como plataforma para a validação dos experimentos.
- **Python:** Linguagem de programação utilizada para desenvolvimento e treinamento dos modelos de redes neurais.
- **OpenCV:** Biblioteca para manipulação e processamento de imagens.

## Como Executar

### Pré-requisitos

1. **CARLA Simulator:** Você pode baixar o CARLA [aqui](https://carla.org/). Siga as instruções de instalação para a plataforma de sua escolha.
2. **Dependências Python:** As bibliotecas necessárias para o treinamento e execução do código são:
   - `torch` (PyTorch)
   - `opencv-python`
   - `numpy`
   - `yolov5` (ou outro modelo YOLO para detecção de objetos)
   - `carla` (para interação com o simulador)

### Passos para Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/projeto-veiculo-autonomo.git
cd projeto-veiculo-autonomo
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Treinamento do Modelo YOLO:**
   Caso deseje treinar o modelo YOLO, siga os passos no arquivo `train_yolo.py`. Para detecção e classificação das placas de trânsito, será necessário usar um conjunto de dados de placas de trânsito (disponível em fontes públicas ou personalizado).

4. **Configuração do Simulador CARLA:**
   Inicie o simulador CARLA em uma instância local ou em um servidor. Para rodar o simulador em um modo de teste, utilize os scripts fornecidos no repositório para interagir com o simulador.

5. **Executando o Sistema de Controle de Velocidade:**
   Após a configuração, execute o script de controle de velocidade, integrando a detecção de placas de trânsito com o módulo de piloto automático do CARLA:

```bash
python src/autopilot/main.py
```

6. **Validação dos Resultados:**
   Durante a execução, o veículo autônomo ajustará sua velocidade conforme as placas de trânsito detectadas ao longo das rotas. A comparação entre o piloto automático com o módulo de controle ativo e inativo será exibida.

## Estrutura do Repositório

```
/src
│
├── /autopilot/
│
├── /Plate_Classification/
│
├── /Plate_Detector/
|
│
├── Makefile                #
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

Caso tenha dúvidas ou queira discutir melhorias, fique à vontade para abrir uma *issue* ou entrar em contato diretamente!


```bash
./download.sh
```

### Dependencies
1. Install Pyenv
```bash
curl https://pyenv.run | bash
```
2. TBD


### How to use our carla environment
run the following command in the root directory of the project
```bash
./carla_env.sh
```

### How to execute CARLA Simulator
run the following command in the root directory of the project
```bash
./Simulator/CarlaUE4.sh -fps=10 -quality-level=Low  -RenderOffScreen
```
or
```bash
./Simulator/CarlaUE4.sh -fps=10 -quality-level=Low
```

### Setup Scenarios for CARLA
run the following command in the root directory of the project
```bash
pyenv activate carla-env
./Simulator/PythonAPI/examples/generate_traffic.py -n 80
./Simulator/PythonAPI/examples/dynamic_weather.py
./spawn_npc.py -n 80
./Simulator/PythonAPI/examples/manual_control.py
```

### Common Erros

```bash
sudo apt install libomp5l libjpeg9 libtiff5-dev
cd /usr/lib/x86_64-linux-gnu/
sudo ln -s libtiff.so.6 libtiff.so.5
```
