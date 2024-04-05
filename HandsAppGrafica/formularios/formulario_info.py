import tkinter as tk
from tkinter import font
import cv2
import mediapipe as mp
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from traduccion_lengua_senas.Funciones.condicionales import condicionalesLetras
from traduccion_lengua_senas.Funciones.normalizacionCords import obtenerAngulos

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles

class FormularioInfo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.perfil = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/Perfil.png", (100, 100))
        self.imagen_info = util_img.leer_imagen("C:/2DAM/ProyectoDAM/HandsAppGrafica/imagenes/imagen_central.png", (400, 400))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo_info()

        self.formulario_abecedario = None
        self.formulario_numeros = None
        self.formulario_saludos = None

        self.cap = cv2.VideoCapture(0)
        wCam, hCam = 1280, 720
        self.cap.set(3, wCam)
        self.cap.set(4, hCam)

        with mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=2,  # Cambia el número máximo de manos aquí
                min_detection_confidence=0.75) as self.hands:
            self.detectar_manos()

    def config_window(self):
        self.title('HANDS - Información')
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

        self.labelTitulo = tk.Label(self.barra_superior, text="HANDS - Información")
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
                                        bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                                        command=self.abrir_settings)
        self.buttonSettings.pack(side=tk.TOP)

    def controles_cuerpo_info(self):
        self.labelImagenInfo = tk.Label(self.cuerpo_principal, image=self.imagen_info,
                                        bg=COLOR_CUERPO_PRINCIPAL)
        self.labelImagenInfo.pack(expand=True)

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

        if self.formulario_numeros is None:
            from formularios.formulario_numeros import FormularioNumeros
            self.formulario_numeros = FormularioNumeros(self)
        else:
            self.formulario_numeros.deiconify()

    def abrir_saludos(self):
        self.withdraw()

        if self.formulario_saludos is None:
            from formularios.formulario_saludos import FormularioSaludos
            self.formulario_saludos = FormularioSaludos(self)
        else:
            self.formulario_saludos.deiconify()

    def abrir_abecedario(self):
        self.withdraw()

        if self.formulario_abecedario is None:
            from formularios.formulario_abecedario import FormularioAbecedario
            self.formulario_abecedario = FormularioAbecedario(self)
        else:
            self.formulario_abecedario.deiconify()

    def abrir_settings(self):
        self.withdraw()
        self.parent.abrir_settings()

    def detectar_manos(self):
        global lectura_actual  # Definir como global al inicio de la función
        lectura_actual = 0  # Inicializar la variable
        while True:
            ret, frame = self.cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)
            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    angulosid = obtenerAngulos(results, width, height)[0]
                    pinky = obtenerAngulos(results, width, height)[1]

                    dedos = []
                    if angulosid[5] > 125:
                        dedos.append(1)
                    else:
                        dedos.append(0)

                    if angulosid[4] > 150:
                        dedos.append(1)
                    else:
                        dedos.append(0)

                    for id in range(0, 4):
                        if angulosid[id] > 90:
                            dedos.append(1)
                        else:
                            dedos.append(0)

                    TotalDedos = dedos.count(1)

                    pinkY = pinky[1] + pinky[0]
                    resta = pinkY - lectura_actual
                    lectura_actual = pinkY

                    print(abs(resta), pinkY, lectura_actual)

                    if abs(resta) > 30:
                        print("jota en movimento")
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                        cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
                        print("J")

                    # Llama a la función para detectar letras con los dedos
                    dedos_detectados = condicionalesLetras(dedos, frame)
                    print("Dedos detectados:", dedos_detectados)

                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()


# Para probar el formulario
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioInfo(root)
    root.mainloop()
