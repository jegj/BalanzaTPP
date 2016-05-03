# coding=utf-8
__author__ = 'javier'

import logging
import os
import serial
import json
import random
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONFIG_FILE_PATH = 'config/config.init'


class BalanzaHandler(object):

    balanza_handler_instance = None
    status = None
    msg = None
    data = None
    _configuracion_ok = False
    _archivo_configuracion = None
    _PUERTO_COM = None
    _CARACTER_ESTABILIDAD = None
    _TIMEOUT = None
    _STOPBITS = None
    _BYTESIZE = None
    _PRODUCTION = None

    def __init__(self):
        try:
            self._configuracion_ok = False
            if getattr(sys, 'frozen', False):
                self._archivo_configuracion = 'config.init'
            elif __file__:
                parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                self._archivo_configuracion = os.path.join(parent_dir, CONFIG_FILE_PATH)

            logger.info(self._archivo_configuracion)
            self.status = u'OK'
            self.set_variables_configuracion()
            logger.info(u'CREANDO OBJECTO DE CONEXION CON BALANZA')

        except Exception, e:
            logger.error(u'ERROR DE CONEXION CON LA BALANZA: %s', e)
            self.balanza_handler_instance = None
            self.status = u'ERROR'
            self.msg = u'Error Conexion con la balanza' + str(e)
            self.data = None

    def set_variables_configuracion(self):
        """
        Metodo que lee el archivo de configuracion e intenta setearlo
        :return:
        """
        try:
            with open(self._archivo_configuracion, "r") as archivo:
                for linea in archivo:
                    tokens = linea.split(' ')
                    var_str = tokens[0].strip()
                    val_str = tokens[1].strip()
                    self.set_variable(var_str, val_str)
            self._configuracion_ok = True
        except Exception as e:
            print '==>,', e
            logger.error(u'ERROR LEYENDO ARCHIVO DE CONFIGURACION %s'. e)
            self._configuracion_ok = False

    def configuracion_correcta(self):
        return self._configuracion_ok

    def get_caracter_estabilidad(self):
        return self._CARACTER_ESTABILIDAD

    def set_variable(self, index, val):
        """
        Metodo que setea las variables especificadas en el archivo de configuracion
        :param index:
        :param val:
        :return:
        """
        if index == 'STBL':
            self._CARACTER_ESTABILIDAD = val
            logger.info(u'STBL: %s', self._CARACTER_ESTABILIDAD)
        elif index == 'COM_PORT':
            self._PUERTO_COM = val
            logger.info(u'COM_PORT: %s', self._PUERTO_COM)
        elif index == 'TMOUT':
            self._TIMEOUT = int(val)
            logger.info(u'TMOUT: %s', self._TIMEOUT)
        elif index == 'STOP':
            self._STOPBITS = int(val)
            logger.info(u'STOP: %s', self._STOPBITS)
        elif index == 'BYTESIZE':
            self._BYTESIZE = int(val)
            logger.info(u'BYTESIZE: %s', self._BYTESIZE)
        elif index == 'PRODUCTION':
            self._PRODUCTION = int(val)
            logger.info(u'PRODUCTION: %s', self._PRODUCTION)

    def capturar_peso(self):
        """
        Metodo que realiza la conexion con el puerto y captura el peso
        :return:
        """
        if self._configuracion_ok:
            if self._PRODUCTION:
                cont = 0
                if self.balanza_handler_instance is None:
                    self.balanza_handler_instance = serial.Serial(
                        self._PUERTO_COM,
                        9600,
                        timeout=self._TIMEOUT,
                        parity=serial.PARITY_EVEN,
                        stopbits=self._STOPBITS,
                        bytesize=self._BYTESIZE
                    )
                str_data = ''

                while True:
                    str_data += str(self.balanza_handler_instance.readline())
                    index_s = str_data.rfind(self._CARACTER_ESTABILIDAD)
                    if index_s >= 0:
                        index_kg = str_data.find('kg', index_s + 1)
                        if index_kg >= 0:
                            self.data = str_data[index_s + 2:index_kg]
                            break
                    else:
                        cont += 1
                        if cont == 10000:
                            self.data = '0'
                            break
            else:
                self.data = random.randint(1, 60000)
        else:
            self.msg = u'La aplicación de Escritorio no pudo leer el archivo de configuracion config.init'
            self.status = u'ERROR'

        self.balanza_handler_instance = None

    def format_json_data(self, first_time=False):
        """
        Metodo que prepara la respuesta para la aplicacion web
        :param first_time:
        :return:
        """
        data = {
            'status': self.status,
            'msg': self.msg,
            'data': self.data
        }

        if first_time:
            data['first_time'] = True

        return data

    def process_json_data(self, data):
        """
        Metodo que recibe la data de la aplicacion web y ejecuta el comando especificado
        :param data:
        :return:
        """
        command = json.loads(data)
        #   COMANDO PARA CAPTURAR PESO
        if command['order'] == 'WEIGH':
            logger.info(u'CAPTURANDO PESO POR ORDEN DEL APLICACION WEB...')
            self.capturar_peso()
