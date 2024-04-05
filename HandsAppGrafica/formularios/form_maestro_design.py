# FormularioMaestroDesign.py

import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formulario_abecedario import FormularioAbecedario
from formulario_numeros import FormularioNumeros
from formulario_saludos import FormularioSaludos
from formulario_info import FormularioInfo
from formularios.formulario_settings import FormularioSettings

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.perfil = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/Perfil.png", (100, 100))
        self.imagen_central = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/imagen_central.png", (400, 400))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

        self.formulario_abecedario = None
        self.formulario_numeros = None
        self.formulario_saludos = None
        self.formulario_info = None
        self.formulario_settings = None

    def config_window(self):
        self.title('HANDS')
        self.iconbitmap("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/logo.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="HANDS")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelInfo = tk.Label(
            self.barra_superior, text="AlonsoSC")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.buttonAbecedarios = tk.Button(self.menu_lateral, text="Abecedarios", font=font_awesome,
                                           command=self.abrir_abecedario)
        self.configurar_boton_menu(self.buttonAbecedarios, "Abecedarios", "\u005A", font_awesome, ancho_menu, alto_menu)

        self.buttonNumeros = tk.Button(self.menu_lateral, text="  \u2464    Numeros", anchor="w", font=font_awesome,
                                       bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                       command=self.abrir_numeros)
        self.configurar_boton_menu(self.buttonNumeros, "Numeros", "\u2464", font_awesome, ancho_menu, alto_menu)

        self.buttonSaludos = tk.Button(self.menu_lateral, text="  \uf085    Saludos", anchor="w", font=font_awesome,
                                       bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                       command=self.abrir_saludos)
        self.configurar_boton_menu(self.buttonSaludos, "Saludos", "\uf085", font_awesome, ancho_menu, alto_menu)

        self.buttonInfo = tk.Button(self.menu_lateral, text="  \uFFFD    Info", anchor="w", font=font_awesome,
                                    bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                    command=self.abrir_info)
        self.configurar_boton_menu(self.buttonInfo, "Info", "\uFFFD", font_awesome, ancho_menu, alto_menu)

        self.buttonSettings = tk.Button(self.menu_lateral, text="  \u2699    Settings", anchor="w", font=font_awesome,
                                        bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                        command=self.abrir_settings)
        self.configurar_boton_menu(self.buttonSettings, "Settings", "\u2699", font_awesome, ancho_menu, alto_menu)

    def controles_cuerpo(self):
        self.labelImagenCentral = tk.Label(self.cuerpo_principal, image=self.imagen_central, bg=COLOR_CUERPO_PRINCIPAL)
        self.labelImagenCentral.pack(expand=True)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_abecedario(self):
        self.withdraw()

        if self.formulario_abecedario is None:
            self.formulario_abecedario = FormularioAbecedario(self)
        else:
            self.formulario_abecedario.deiconify()

    def abrir_numeros(self):
        self.withdraw()

        if self.formulario_numeros is None:
            self.formulario_numeros = FormularioNumeros(self)
        else:
            self.formulario_numeros.deiconify()

    def abrir_saludos(self):
        self.withdraw()

        if self.formulario_saludos is None:
            self.formulario_saludos = FormularioSaludos(self)
        else:
            self.formulario_saludos.deiconify()

    def abrir_info(self):
        self.withdraw()

        if self.formulario_info is None:
            self.formulario_info = FormularioInfo(self)
        elif not self.formulario_info.winfo_exists():
            # Si el widget ya no existe, crea una nueva instancia
            self.formulario_info = FormularioInfo(self)

        self.formulario_info.deiconify()

    def abrir_settings(self):
        self.withdraw()

        if self.formulario_settings is None:
            self.formulario_settings = FormularioSettings(self)
        elif not self.formulario_settings.winfo_exists():
            # Si el widget ya no existe, crea una nueva instancia
            self.formulario_settings = FormularioSettings(self)

        self.formulario_settings.deiconify()

    def regresar_a_ventana_principal(self):
        if self.formulario_numeros is not None:
            self.formulario_numeros.destroy()
            self.formulario_numeros = None
        if self.formulario_abecedario is not None:
            self.formulario_abecedario.destroy()
            self.formulario_abecedario = None
        if self.formulario_saludos is not None:
            self.formulario_saludos.destroy()
            self.formulario_saludos = None
        if self.formulario_info is not None:
            self.formulario_info.destroy()
            self.formulario_info = None
        if self.formulario_settings is not None:
            self.formulario_settings.destroy()
            self.formulario_settings = None

        self.deiconify()

if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()

