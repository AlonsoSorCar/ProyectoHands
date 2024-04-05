import tkinter as tk
from tkinter import Label, font, Button
from PIL import Image, ImageTk
import requests
from io import BytesIO
import util.util_imagenes as util_img
from util import util_ventana


class FormularioAbecedario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.perfil = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/Perfil.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo_abecedario()

    def config_window(self):
        self.title('HANDS - Abecedario')
        self.iconbitmap("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/logo.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg="#1f2329", height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg="#2a3138", width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg="#f1faff")
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

        self.cuerpo_principal.grid_rowconfigure(0, weight=1)
        self.cuerpo_principal.grid_columnconfigure(0, weight=1)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="HANDS - Abecedario")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg="#1f2329", pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.labelInfo = tk.Label(self.barra_superior, text="AlonsoSC")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg="#1f2329", padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg="#2a3138")
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        self.buttonNumeroInicio = tk.Button(self.menu_lateral, text="  \uf015    Inicio", anchor="w", font=font_awesome,
                                            bd=0, bg="#2a3138", fg="white", width=ancho_menu, height=alto_menu,
                                            command=self.regresar_a_ventana_principal)
        self.buttonNumeroInicio.pack(side=tk.TOP)

        self.buttonNumeroNumeros = tk.Button(self.menu_lateral, text="  \u2464    Numeros", anchor="w",
                                             font=font_awesome,
                                             bd=0, bg="#2a3138", fg="white", width=ancho_menu,
                                             height=alto_menu,
                                             command=self.navegar_a_numeros)
        self.buttonNumeroNumeros.pack(side=tk.TOP)

        self.buttonNumeroSaludos = tk.Button(self.menu_lateral, text="  \uf085    Saludos", anchor="w",
                                             font=font_awesome,
                                             bd=0, bg="#2a3138", fg="white", width=ancho_menu,
                                             height=alto_menu,
                                             command=self.abrir_saludos)
        self.buttonNumeroSaludos.pack(side=tk.TOP)

        self.buttonNumeroInfo = tk.Button(self.menu_lateral, text="  \uFFFD    Info", anchor="w", font=font_awesome,
                                          bd=0, bg="#2a3138", fg="white", width=ancho_menu, height=alto_menu
                                          , command=self.abrir_info)
        self.buttonNumeroInfo.pack(side=tk.TOP)

        self.buttonNumeroSettings = tk.Button(self.menu_lateral, text="  \u2699    Settings", anchor="w",
                                              font=font_awesome,
                                              bd=0, bg="#2a3138", fg="white", width=ancho_menu,
                                              height=alto_menu,
                                              command=self.abrir_settings)
        self.buttonNumeroSettings.pack(side=tk.TOP)

    def controles_cuerpo_abecedario(self):
        self.imagenes = [
            "LSE_a.png",
            "LSE_b.png",
            "LSE_c.png",
            "LSE_d.png",
            "LSE_e.png",
            "LSE_f.png",
            "LSE_g.png",
            "LSE_h.png",
            "LSE_i.png",
            "LSE_j.png",
            "LSE_k.png",
            "LSE_l.png",
            "LSE_m.png",
            "LSE_n.png",
            "LSE_o.png",
            "LSE_p.png",
            "LSE_q.png",
            "LSE_r.png",
            "LSE_s.png",
            "LSE_t.png",
            "LSE_u.png",
            "LSE_v.png",
            "LSE_w.png",
            "LSE_x.png",
            "LSE_y.png",
            "LSE_z.png"
        ]

        # Crear un Frame para la cuadrícula de botones
        cuadricula_frame = tk.Frame(self.cuerpo_principal, bg="#f1faff")
        cuadricula_frame.pack(fill=tk.BOTH, expand=True)

        num_columnas = 5
        contador = 0

        for imagen in self.imagenes:
            url = f"https://raw.githubusercontent.com/AlonsoSorCar/ImagenesHands/main/{imagen}"
            img = self.get_remote_image(url)
            if img:
                row = contador // num_columnas
                col = contador % num_columnas

                # Crear un botón con la imagen como icono
                button = Button(cuadricula_frame, image=img, bg="#f1faff", bd=0,
                                command=lambda idx=contador: self.abrir_galeria(idx))
                button.image = img
                button.grid(row=row, column=col, padx=5, pady=5)

                contador += 1

    def regresar_a_ventana_principal(self):
        self.destroy()
        self.parent.regresar_a_ventana_principal()

    def navegar_a_numeros(self):
        self.withdraw()
        from formularios.formulario_numeros import FormularioNumeros
        self.ventana_numeros = FormularioNumeros(self)
        self.ventana_numeros.grab_set()
        self.ventana_numeros.focus_set()
        self.parent.wait_window(self.ventana_numeros)

    def abrir_info(self):
        self.withdraw()
        from formularios.formulario_info import FormularioInfo
        if self.formulario_info is None:
            self.formulario_info = FormularioInfo(self)
        elif not self.formulario_info.winfo_exists():
            self.formulario_info = FormularioInfo(self)

        self.formulario_info.deiconify()

    def abrir_saludos(self):
        self.withdraw()

        if self.formulario_saludos is None:
            from formularios.formulario_saludos import FormularioSaludos
            self.formulario_saludos = FormularioSaludos(self)
        else:
            self.formulario_saludos.deiconify()

    def abrir_settings(self):
        self.withdraw()

        if self.formulario_settings is None:
            from formularios.formulario_settings import FormularioSettings
            self.formulario_settings = FormularioSettings(self)
        else:
            self.formulario_settings.deiconify()

    def get_remote_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.thumbnail((100, 100))
                img = ImageTk.PhotoImage(img)
                return img
            else:
                print(f"No se pudo descargar la imagen de {url}")
                return None
        except Exception as e:
            print(f"Error al obtener la imagen de {url}: {e}")
            return None

    def abrir_galeria(self, index):
        popup = tk.Toplevel(self)
        popup.title("Galería de Imágenes")
        img = self.get_remote_image(f"https://raw.githubusercontent.com/AlonsoSorCar/ImagenesHands/main/{self.imagenes[index]}")
        if img:
            label = Label(popup, image=img)
            label.image = img
            label.pack()

    def print_boton_clickado(self, index):
        print(f"Botón {index} clickado")


# Para probar el formulario
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioAbecedario(root)
    root.mainloop()
