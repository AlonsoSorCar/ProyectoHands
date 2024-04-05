import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.formulario_numeros import FormularioNumeros


class FormularioSettings(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.perfil = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/Perfil.png", (100, 100))
        self.imagen_settings = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/imagen_central.png", (400, 400))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo_settings()

        self.formulario_abecedario = None
        self.formulario_saludos = None
        self.formulario_numeros = None

    def config_window(self):
        self.title('HANDS - Settings')
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

        self.labelTitulo = tk.Label(self.barra_superior, text="HANDS - Settings")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", command=self.toggle_panel)
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.buttonSettings = tk.Button(self.barra_superior, text="\u2699", font=font_awesome,
                                        bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonSettings.pack(side=tk.RIGHT)

        self.labelInfo = tk.Label(self.barra_superior, text="AlonsoSC")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.buttonInicio = tk.Button(self.menu_lateral, text="  \uf015    Inicio", anchor="w", font=font_awesome,
                                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                      command=self.regresar_a_ventana_principal)
        self.buttonInicio.pack(side=tk.TOP)

        self.buttonAbecedario = tk.Button(self.menu_lateral, text="  \u005A    Abecedario", anchor="w",
                                          font=font_awesome, bd=0, bg=COLOR_MENU_LATERAL, fg="white",
                                          width=ancho_menu, height=alto_menu, command=self.abrir_abecedario)
        self.buttonAbecedario.pack(side=tk.TOP)

        self.buttonNumeros = tk.Button(self.menu_lateral, text="  \u2464    Numeros", anchor="w", font=font_awesome,
                                       bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                       command=self.abrir_numeros)
        self.buttonNumeros.pack(side=tk.TOP)

        self.buttonSaludos = tk.Button(self.menu_lateral, text="  \uf085    Saludos", anchor="w", font=font_awesome,
                                       bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                       command=self.abrir_saludos)
        self.buttonSaludos.pack(side=tk.TOP)

        self.buttonSettings = tk.Button(self.menu_lateral, text="  \u2699    Settings", anchor="w", font=font_awesome,
                                        bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        self.buttonSettings.pack(side=tk.TOP)

    def controles_cuerpo_settings(self):
        self.labelImagenSettings = tk.Label(self.cuerpo_principal, image=self.imagen_settings,
                                           bg=COLOR_CUERPO_PRINCIPAL)
        self.labelImagenSettings.pack(expand=True)

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def regresar_a_ventana_principal(self):
        self.destroy()
        self.parent.deiconify()

    def abrir_numeros(self):
        self.withdraw()
        self.parent.abrir_numeros()

    def abrir_saludos(self):
        self.withdraw()

        if self.formulario_saludos is None:
            from formularios.formulario_saludos import FormularioSaludos
            self.formulario_saludos = FormularioSaludos(self)
        else:
            self.formulario_saludos.deiconify()


    def abrir_numeros(self):
        self.withdraw()

        if self.formulario_numeros is None:
            self.formulario_numeros = FormularioNumeros(self)
        else:
            self.formulario_numeros.deiconify()

    def abrir_abecedario(self):
        self.withdraw()

        if self.formulario_abecedario is None:
            from formularios.formulario_abecedario import FormularioAbecedario
            self.formulario_abecedario = FormularioAbecedario(self)
        else:
            self.formulario_abecedario.deiconify()

# Para probar el formulario
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioSettings(root)
    root.mainloop()
