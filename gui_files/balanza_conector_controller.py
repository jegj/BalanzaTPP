__author__ = 'javier'

import logging
from socket_server.web_socket import *
from threading import Event as EventTh

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BalanzaConectorController(object):

    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.socket_server = None
        self.stop_threads = EventTh()
        application = tornado.web.Application([(r'/ws', WSHandler, dict(main_frame=self.main_frame))])
        application.listen(9090)

    def start_socket_server(self, text_widget):
        logger.info(u'INICIANDO HILO DE EJECUCION DE WEB SOCKET SERVER')
        if self.socket_server is None:
            self.stop_threads.clear()
            self.socket_server = Server()
            self.socket_server.start()
            self.main_frame.add_log_message("INICIANDO CONEXION CON BALANZA...\n")

    def stop_socket_server(self, text_widget):
        logger.info(u'PARANDO HILO DE EJECUCION DE WEB SOCKET SERVER')
        if self.socket_server is not None:
            self.stop_threads.set()
            self.socket_server.stop_tornado_server()
            self.socket_server.join()
            self.socket_server = None
            self.main_frame.add_log_message("DETENIENDO CONEXION CON BALANZA...\n")

    def restart_socket_server(self, text_widget):
        logger.info(u'REINICIANDO HILO DE EJECUCION DE WEB SOCKET SERVER')
        if self.socket_server is not None:
            self.stop_socket_server(text_widget)
            self.start_socket_server(text_widget)
