import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO para controle dos pinos GPIO do Raspberry Pi
from time import sleep  # Importa a função sleep da biblioteca time para pausas no código

red_pin = 23  # Define a variável red_pin como 23, que representa o número do pino GPIO a ser utilizado

GPIO.setwarnings(False)  # Desativa os avisos de configuração de GPIO (útil para evitar mensagens de erro)

GPIO.setmode(GPIO.BCM)  # Configura o modo de numeração dos pinos como BCM (Broadcom SOC channel)

GPIO.setup(red_pin, GPIO.OUT)  # Configura o pino definido como saída (OUT), permitindo enviar sinais elétricos

c = 0  # Inicializa a variável c com valor zero; será usada para controlar o tempo de espera

while True:  # Inicia um loop infinito
    GPIO.output(red_pin, True)  # Envia um sinal alto (True) para acender o LED conectado ao pino 23
    sleep(1.0 * c)  # Pausa por um tempo proporcional à variável c (inicialmente zero)
    
    GPIO.output(red_pin, False)  # Envia um sinal baixo (False) para apagar o LED
    sleep(1.0 * (1.0 - c))  # Pausa por um tempo proporcional à diferença entre 1.0 e c

    if c < 1.0:  # Verifica se c é menor que 1.0
        c = c + 0.1  # Incrementa c em 0.1 a cada iteração até atingir o valor máximo de 1.0