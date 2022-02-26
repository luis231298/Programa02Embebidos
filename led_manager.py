# !/usr/bin/env python3
# ## ###############################################
#
# LUPL_led_manager.py
# Controls leds in the GPIO
#
# Autor: José Luis Luna Pérez
# Original by: Mauricio Matamoros
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#Se importan las librerias que ocupara el programa
import RPi.GPIO as GPIO
from time import sleep
#Se inicializa la virtual board 
import virtualboard
#LLamamos a Rpi.GPIO para que nos permitan activar los pines que ocuparemos.
GPIO.setmode(GPIO.BOARD)

# Iniciamos las salidas que llevan al 7 segmentos
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

# Declaramos los pines que ocuparemos y estos los iniciamos apagados
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)#8 Usado para ping pong y marquesinas
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)#7
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)#6
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)#5
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)#4
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)#3
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)#2
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)#1

def leds(num):
    #usamos if con los numeros como condicion encendera segun el boton
    #presionado en la web
    if num == 1:
        GPIO.output(10, GPIO.HIGH)
    elif num == 2:
        GPIO.output(12, GPIO.HIGH)
    elif num == 3:
        GPIO.output(16, GPIO.HIGH)
    elif num == 4:
        GPIO.output(18, GPIO.HIGH)
    elif num == 5:
        GPIO.output(22, GPIO.HIGH) 
    elif num == 6:
        GPIO.output(24, GPIO.HIGH)
    elif num == 7:
        GPIO.output(26, GPIO.HIGH)
	#reiniciamos los leds (apagandolos)
    sleep(0.4)
    GPIO.output(10, GPIO.LOW) 
    GPIO.output(12, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
