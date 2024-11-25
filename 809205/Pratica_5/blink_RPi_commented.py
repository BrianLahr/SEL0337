import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO para controle dos pinos GPIO do Raspberry Pi
from time import sleep  # Importa a função sleep da biblioteca time para pausas no código

red_pin = 23  # Define a variável red_pin como 23, que representa o número do pino GPIO a ser utilizado

GPIO.setwarnings(False)  # Desativa os avisos de configuração de GPIO (útil para evitar mensagens de erro)

GPIO.setmode(GPIO.BCM)  # Configura o modo de numeração dos pinos como BCM (Broadcom SOC channel)

GPIO.setup(red_pin, GPIO.OUT)  # Configura o pino definido como saída (OUT), permitindo enviar sinais elétricos

while True:  # Inicia um loop infinito
    GPIO.output(red_pin, True)  # Envia um sinal alto (True) para acender o LED conectado ao pino 23
    sleep(0.5)  # Pausa por 0,5 segundos, mantendo o LED aceso
    
    GPIO.output(red_pin, False)  # Envia um sinal baixo (False) para apagar o LED
    sleep(0.5)  # Pausa por mais 0,5 segundos, mantendo o LED apagado