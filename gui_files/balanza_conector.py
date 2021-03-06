# coding=utf-8
#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.7
# In conjunction with Tcl version 8.6
#    Mar 15, 2016 11:09:10 AM
import sys
import tkMessageBox

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import balanza_conector_support
from balanza_conector_controller import BalanzaConectorController

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = SIO_Conector_de_Balanza(root)
    balanza_conector_support.init(root, top)
    root.mainloop()

w = None
def create_SIO_Conector_de_Balanza(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = SIO_Conector_de_Balanza (w)
    balanza_conector_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_SIO_Conector_de_Balanza():
    global w
    w.destroy()
    w = None


def destroy_main_frame(top, text_widget, controller):
    msg = u"ADVERTENCIA: Al cerrar esta ventana no podra realizar pesajes automaticos con la aplicación web"
    resultado = tkMessageBox.askquestion("Salir", msg, icon='warning')
    if resultado == 'yes':
        controller.stop_socket_server(text_widget)
        top.destroy()


class SIO_Conector_de_Balanza:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("566x356+376+183")
        top.title("SIO: Conector de Balanza v1.0.0")
        top.configure(background="#dee1d9")
        top.configure(highlightbackground="#dbd9d9")
        top.configure(highlightcolor="black")

        self.menubar = Menu(top,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        controller = BalanzaConectorController(self)

        top.protocol("WM_DELETE_WINDOW", lambda: destroy_main_frame(top, self.log_mensajes, controller))

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.04, rely=0.03, relheight=0.32, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=525)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.63, rely=0.17, height=19, width=57)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''ESTADO:''')

        self.estado_conexion_msg = Message(self.Frame1)
        self.estado_conexion_msg.place(relx=0.78, rely=0.08, relheight=0.37
                , relwidth=0.20)
        self.estado_conexion_msg.configure(foreground="#ee0809")
        self.estado_conexion_msg.configure(text='''DESCONECTADO''')
        self.estado_conexion_msg.configure(width=101)

        self.iniciar_button = Button(self.Frame1)
        self.iniciar_button.place(relx=0.02, rely=0.17, height=27, width=137)
        self.iniciar_button.configure(activebackground="#d9d9d9")
        self.iniciar_button.configure(command=lambda: controller.start_socket_server(self.log_mensajes))
        self.iniciar_button.configure(text='''Iniciar/Reiniciar''')

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.4, rely=0.35, relheight=0.37, relwidth=0.36)
        self.Message2.configure(text='''ARCHIVO CONFIGURACION:''')
        self.Message2.configure(width=187)

        self.archivo_configuracion_msg = Label(self.Frame1)
        self.archivo_configuracion_msg.place(relx=0.85, rely=0.44, height=19
                , width=21)
        self.archivo_configuracion_msg.configure(activebackground="#f9f9f9")
        self.archivo_configuracion_msg.configure(text='''-''')

        self.Message4 = Message(self.Frame1)
        self.Message4.place(relx=0.34, rely=0.7, relheight=0.2, relwidth=0.39)
        self.Message4.configure(text='''CARACTER ESTABILIDAD USADO:''')
        self.Message4.configure(width=205)

        self.caracter_estabilidad_msg = Label(self.Frame1)
        self.caracter_estabilidad_msg.place(relx=0.84, rely=0.7, height=19
                , width=36)
        self.caracter_estabilidad_msg.configure(activebackground="#f9f9f9")
        self.caracter_estabilidad_msg.configure(text='''-''')

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.04, rely=0.39, relheight=0.55, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(width=525)

        self.log_mensajes = Text(self.Frame2)
        self.log_mensajes.place(relx=0.02, rely=0.21, relheight=0.75, relwidth=0.96)
        self.log_mensajes.configure(background="white")
        self.log_mensajes.configure(font="TkTextFont")
        self.log_mensajes.configure(selectbackground="#c4c4c4")
        self.log_mensajes.configure(width=666)
        self.log_mensajes.configure(wrap=WORD)
        self.log_mensajes.configure(state=DISABLED)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.02, rely=0.05, height=19, width=71)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''MENSAJES:''')

    def add_log_message(self, msg):
        """
        Metodo que agrega mensajes de log al textarea
        :param msg:
        :return:
        """
        self.log_mensajes.configure(state=NORMAL)
        self.log_mensajes.insert(INSERT, msg)
        self.log_mensajes.configure(state=DISABLED)
        self.log_mensajes.see(END)

    def establish_connection(self):
        """
        Metodo que cambia el estado de la interfaz cuando se conecta con la aplicacion web
        :return:
        """
        self.estado_conexion_msg.configure(foreground="#008542")
        self.estado_conexion_msg.configure(text='''CONECTADO''')

    def lose_connection(self):
        """
        Metodo que cambia el estado de la interfaz cuando se desconecta con la aplicacion web
        :return:
        """
        self.estado_conexion_msg.configure(foreground="#ee0809")
        self.estado_conexion_msg.configure(text='''DESCONECTADO''')

    def configuracion_correcta(self):
        """
        Metodo que cambia el estado de la interfaz cuando existe una configuracion correcta
        con la aplicacion web
        :return:
        """
        self.archivo_configuracion_msg.configure(activebackground="#f9f9f9")
        self.archivo_configuracion_msg.configure(foreground="#009400")
        self.archivo_configuracion_msg.configure(text='''OK''')

    def configuracion_incorrecta(self):
        """
        Metodo que cambia el estado de la interfaz cuando existe una configuracion incorrecta
        con la aplicacion web
        :return:
        """
        self.archivo_configuracion_msg.configure(activebackground="#f9f9f9")
        self.archivo_configuracion_msg.configure(foreground="#ff0000")
        self.archivo_configuracion_msg.configure(text='''ERROR''')

        self.add_log_message(
            'NO SE PUDO PROCESAR EL ARCHIVO [config.init]. REVISAR EL ARCHIVO Y LA CONFIGURACION ESPECIFICADA\n'
        )
        self.lose_connection()

    def set_caracter_estabilidad(self, car):
        """
        Metodo que setea el caracter de estabilidad en la interfaz
        :param car:
        :return:
        """
        self.caracter_estabilidad_msg.configure(text=car)

if __name__ == '__main__':
    vp_start_gui()



