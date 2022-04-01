# Instruções

Para usar os scripts instalar a biblioteca **python-osc**:

**pip install python-osc**

## Uso

- Abra os arquivos em editores e coloque nos locais indicados o IP e a PORTA para o sender e o receiver (se for o caso).

- Comando para ara executar o oscReceiver (apenas para testar se o sender esta funcionando):

**python3 oscReceiver**

- Comando para executar o oscSender:

**python3 oscSender**

No sender ao digitar **s seguido de enter** ele interrope o envio dos pacotes para o destino.
Para retomar o envio pressione **f seguido de enter**

## Uso do restMulti

Para simular varios sensores executar o comando:

**python3 restMulti Numero_de_sensores_desejados**

Para iniciar o comando de start do disparo sincrono dos oculus, pressione f no terminal. E para simular o encerramento pressione s.
