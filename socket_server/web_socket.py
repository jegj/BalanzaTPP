__author__ = 'javier'
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
# import serial
# import json
import logging
from threading import Thread


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Server(Thread):
    instance = None

    def __init__(self):
        Thread.__init__(self)
        self.instance = tornado.ioloop.IOLoop.instance()

    def run(self):
        logger.info(u'CREANDO SERVIDOR DE WEBSOCKETS')
        self.instance.start()

    def stop_tornado_server(self):
        logger.info(u'CERRANDO SERVIDOR DE WEBSOCKETS')
        self.instance.stop()


class WSHandler(tornado.websocket.WebSocketHandler):
    main_frame = None

    def initialize(self, main_frame):
        self.main_frame = main_frame

    def check_origin(self, origin):
        return True

    def open(self):
        logger.info(u'CONEXION ESTABLECIDA CON LA APLICACION DE ESCRITORIO')
        self.main_frame.add_log_message("CONEXION ESTABLECIDA CON LA APLICACION WEB...\n")
        self.write_message('The server says: Hello. Connection was accepted.')
        self.main_frame.establish_connection()

    def on_message(self, message):
        logger.info(u'MESANJE RECIBIDO DESDE EL BROWSER')
        self.main_frame.add_log_message("CAPTURAND PESO...\n")
        self.write_message('i have data!')

    def on_close(self):
        logger.info(u'CONEXION CERRADA')
        self.main_frame.add_log_message("CERRRANDO CONEXION CON LA APLICACION WEB...\n")
        # self.write_message('bye! from the server!')


# class BalanzaHandler(object):
#     balanza_handler_instance = None
#     status = None
#     msg = None
#     data = None
#     debug = None
#     _archivo_configuracion = None
#     # --------------------------------#
#     _PUERTO_COM = None
#     _CARACTER_ESTABILIDAD = None
#     _TIMEOUT = None
#     _STOPBITS = None
#     _BYTESIZE = None
#
#     def __init__(self, debug_t=False):
#         try:
#             self.archivo_configuracion = 'balanza.init'
#             self.debug = debug_t
#             self.status = u'OK'
#             self.set_variables_configuracion()
#             logger.info(u'SE ESTABLECIO CONEXION CON LA BALANZA')
#
#         except Exception, e:
#             if self.debug:
#                 self.status = u'OK'
#             else:
#                 logger.error(u'ERROR DE CONEXION CON LA BALANZA: %s', e)
#                 self.balanza_handler_instance = None
#                 self.status = u'ERROR'
#                 self.msg = u'Error Conexion con la balanza' + str(e)
#                 self.data = None
#
#     def set_variables_configuracion(self):
#         archivo = open("balanza.init", "r")
#         for linea in archivo:
#             tokens = linea.split(' ')
#             var_str = tokens[0].strip()
#             val_str = tokens[1].strip()
#             self.set_variable(var_str, val_str)
#
#     def set_variable(self, index, val):
#         if index == 'STBL':
#             self._CARACTER_ESTABILIDAD = val
#         elif index == 'COM_PORT':
#             self._PUERTO_COM = val
#         elif index == 'TMOUT':
#             self._TIMEOUT = int(val)
#         elif index == 'STOP':
#             self._STOPBITS = int(val)
#         elif index == 'BYTESIZE':
#             self._BYTESIZE = int(val)
#
#     def capturar_peso(self):
#         cont = 0
#         if self.balanza_handler_instance is None:
#             self.balanza_handler_instance = serial.Serial(
#                 self._PUERTO_COM,
#                 9600,
#                 timeout=self._TIMEOUT,
#                 parity=serial.PARITY_EVEN,
#                 stopbits=self._STOPBITS,
#                 bytesize=self._BYTESIZE
#             )
#         str_data = ''
#
#         while True:
#             str_data += str(self.balanza_handler_instance.readline())
#             index_s = str_data.rfind(self._CARACTER_ESTABILIDAD)
#             if index_s >= 0:
#                 index_kg = str_data.find('kg', index_s + 1)
#                 if index_kg >= 0:
#                     self.data = str_data[index_s + 2:index_kg]
#                     break
#             else:
#                 cont += 1
#                 if cont == 10000:
#                     self.data = '0'
#                     break
#
#         self.balanza_handler_instance = None
#
#     def format_json_data(self):
#         data = {
#             'status': self.status,
#             'msg': self.msg,
#             'data': self.data
#         }
#
#         return data
#
#     def process_json_data(self, data):
#         command = json.loads(data)
#         if command['order'] == 'WEIGH':
#             logger.info(u'CAPTURANDO PESO POR ORDEN DEL APLICACION WEB...')
#             self.capturar_peso()
