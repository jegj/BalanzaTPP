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
    """
    Clase que instancia un servidor web socket en un hilo
    """
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
    """
    Clase que instancia el servidor web socket y ejecuta las acciones recibidas por la aplicacion web
    """
    main_frame = None
    balanza = None

    def initialize(self, main_frame):
        """
        Metodo que setea el objecto que tiene la instacia de la interfaz en un variable accesible
        para el servidor web socket
        :param main_frame:
        :return:
        """
        self.main_frame = main_frame

    def check_origin(self, origin):
        return True

    @staticmethod
    def prepare_data(data):
        """
        Metodo que prepara la data para enviarla a la aplicacion web
        :param data:
        :return:
        """
        return json.dumps(data)

    def open(self):
        """
        Metodo que se ejcuta cuando hay una conexion abierta entre el servidor web socket y la
        aplicacion web
        :return:
        """
        logger.info(u'CONEXION ESTABLECIDA CON LA APLICACION DE ESCRITORIO')
        self.main_frame.add_log_message("CONEXION ESTABLECIDA CON LA APLICACION WEB...\n")
        self.main_frame.establish_connection()
        self.balanza = BalanzaHandler()
        if self.balanza.configuracion_correcta():
            self.main_frame.configuracion_correcta()
            self.main_frame.set_caracter_estabilidad(self.balanza.get_caracter_estabilidad())
        else:
            self.main_frame.configuracion_incorrecta()

        data = self.balanza.format_json_data(first_time=True)
        self.write_message(WSHandler.prepare_data(data))

    def on_message(self, message):
        """
        Metodo que se ejecuta cuando el servidor recibe un mensaje por parte de la aplicacion web
        :param message:
        :return:
        """
        logger.info(u'MESANJE RECIBIDO DESDE EL BROWSER')
        self.main_frame.add_log_message("CALCULANDO PESO POR PETICION DE LA APLICACION WEB...\n")
        self.balanza.process_json_data(message)
        data = self.balanza.format_json_data()
        self.write_message(self.prepare_data(data))

    def on_close(self):
        """
        Metodo que se ejecuta cuando se cierra la conexion con la aplicacion web
        :return:
        """
        logger.info(u'CONEXION CERRADA')
        self.main_frame.add_log_message("CERRRANDO CONEXION CON LA APLICACION WEB...\n")
        self.main_frame.lose_connection()
