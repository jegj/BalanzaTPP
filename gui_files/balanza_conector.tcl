#############################################################################
# Generated by PAGE version 4.7
# in conjunction with Tcl version 8.6
#    Mar 18, 2016 04:10:21 PM


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top36
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra39
    set site_3_0 $base.fra40
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top36 {base} {
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m38" -background {#dee1d9} -highlightbackground {#dbd9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 566x356+376+154
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "SIO: Conector de Balanza"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    menu $top.m38 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    frame $top.fra39 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 115 \
        -highlightcolor black -width 525 
    vTcl:DefineAlias "$top.fra39" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra39
    label $site_3_0.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text ESTADO: 
    vTcl:DefineAlias "$site_3_0.lab45" "Label2" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes46 \
        -background {#d9d9d9} -foreground {#ee0809} -highlightcolor black \
        -text DESCONECTADO -width 101 
    vTcl:DefineAlias "$site_3_0.mes46" "estado_conexion_msg" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command iniciar_servidor -foreground {#000000} \
        -highlightcolor black -text Iniciar 
    vTcl:DefineAlias "$site_3_0.but47" "iniciar_button" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes49 \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {ARCHIVO CONFIGURACION:} -width 187 
    vTcl:DefineAlias "$site_3_0.mes49" "Message2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#009400} -highlightcolor black \
        -text OK 
    vTcl:DefineAlias "$site_3_0.lab50" "archivo_configuracion_msg" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes52 \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {CARACTER ESTABILIDAD USADO:} -width 205 
    vTcl:DefineAlias "$site_3_0.mes52" "Message4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text S 
    vTcl:DefineAlias "$site_3_0.lab53" "caracter_estabilidad_msg" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab45 \
        -in $site_3_0 -x 330 -y 20 -width 57 -height 19 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes46 \
        -in $site_3_0 -x 410 -y 10 -width 101 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 10 -y 20 -width 137 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes49 \
        -in $site_3_0 -x 210 -y 40 -width 187 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 448 -y 51 -width 21 -height 19 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes52 \
        -in $site_3_0 -x 180 -y 80 -width 205 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 442 -y 80 -width 36 -height 19 -anchor nw \
        -bordermode ignore 
    frame $top.fra40 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 195 \
        -highlightcolor black -width 525 
    vTcl:DefineAlias "$top.fra40" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra40
    text $site_3_0.tex43 \
        -background white -font TkTextFont -foreground black -height 146 \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black -width 506 \
        -wrap word 
    .top36.fra40.tex43 configure -font TkTextFont
    .top36.fra40.tex43 insert end text
    vTcl:DefineAlias "$site_3_0.tex43" "log_mensajes" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text MENSAJES: 
    vTcl:DefineAlias "$site_3_0.lab44" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tex43 \
        -in $site_3_0 -x 10 -y 40 -width 506 -height 146 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 10 -y 10 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra39 \
        -in $top -x 20 -y 10 -width 525 -height 115 -anchor nw \
        -bordermode ignore 
    place $top.fra40 \
        -in $top -x 20 -y 140 -width 525 -height 195 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top36

