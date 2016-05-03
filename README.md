# BalanzaTPP

## Synopsis

BalanzaTPP es un aplicativo python que maneja el control de pesos de una balanza conectado a una maquina
que usa los puerto COM disponible en la maquina. La aplicación puede ser configurable por medio de un archivo
donde se puede especificar:

* Caracter de estabilidad que usa la balanza
* Puerto COM donde se encuentra instalada
* Timeout de respuesta de la balanza
* Bit de parada
* El tamaño de la palabra que usa la balanza en sus comunicaciones
* Flag de produccion

## Instalacion

Para poder utilizar la aplicación es necesario tener instalado lo siguiente:

* python 2.7.6

Paquetes
--------------------
* tkinter
* tornado ~ 4.2.1
* pyserial ~ 2.7
* PyInstaller ~ 3.1.1 [Solo para generar ejecutables]