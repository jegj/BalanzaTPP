__author__ = 'javier'

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import logging
from threading import Thread
from balanza_handler.balanza_handler import BalanzaHandler, json


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
    balanza = None

    def initialize(self, main_frame):
        self.main_frame = main_frame

    def check_origin(self, origin):
        return True

    @staticmethod
    def prepare_data(data):
        return json.dumps(data)

    def open(self):
        logger.info(u'CONEXION ESTABLECIDA CON LA APLICACION DE ESCRITORIO')
        self.main_frame.add_log_message("CONEXION ESTABLECIDA CON LA APLICACION WEB...\n")
        self.main_frame.establish_connection()
        self.balanza = BalanzaHandler()
        data = self.balanza.format_json_data(first_time=True)
        self.write_message(WSHandler.prepare_data(data))

    def on_message(self, message):
        logger.info(u'MESANJE RECIBIDO DESDE EL BROWSER')
        self.main_frame.add_log_message("PETICION DE LA APLICACION WEB...\n")
        self.balanza.process_json_data(message)
        data = self.balanza.format_json_data()
        self.write_message(self.prepare_data(data))

    def on_close(self):
        logger.info(u'CONEXION CERRADA')
        self.main_frame.add_log_message("CERRRANDO CONEXION CON LA APLICACION WEB...\n")
        self.main_frame.lose_connection()


