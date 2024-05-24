from flask import Flask, render_template, request, jsonify
import cv2
import mediapipe as mp
from Funciones.condicionales import condicionalesLetras
from Funciones.normalizacionCords import obtenerAngulos
import threading

app = Flask(__name__)

lectura_actual = 0

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles

def detect_hands():
    global lectura_actual  # Declarar lectura_actual como global

    cap = cv2.VideoCapture(0)

    wCam, hCam = 1280, 720
    cap.set(3, wCam)
    cap.set(4, hCam)

    with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.75) as hands:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks is not None:
                angulosid = obtenerAngulos(results, width, height)[0]

                dedos = []
                # pulgar externo angle
                if angulosid[5] > 125:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # pulgar interno
                if angulosid[4] > 150:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # 4 dedos
                for id in range(0, 4):
                    if angulosid[id] > 90:
                        dedos.append(1)
                    else:
                        dedos.append(0)

                TotalDedos = dedos.count(1)
                condicionalesLetras(dedos, frame)

                pinky = obtenerAngulos(results, width, height)[1]
                pinkY = pinky[1] + pinky[0]
                resta = pinkY - lectura_actual
                lectura_actual = pinkY
                print(abs(resta), pinkY, lectura_actual)

                if dedos == [0, 0, 1, 0, 0, 0]:
                    if abs(resta) > 30:
                        print("jota en movimento")
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                        cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        
@app.route("/start_detection", methods=["POST"])
def start_detection():
    # Iniciar detección de manos en un hilo separado
    detect_thread = threading.Thread(target=detect_hands)
    detect_thread.start()

    return jsonify({"message": "Detección de manos iniciada"})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/abecedario")
def abecedario():
    return render_template("abecedario.html")

@app.route("/saludos")
def saludos():
    return render_template("saludos.html")

@app.route("/numeros")
def numeros():
    return render_template("numeros.html")

@app.route("/deteccion")
def deteccion():
    return render_template("deteccion.html")

@app.route("/index")
def inicio():
    return render_template("index.html")

if __name__ == "__main__": 
    app.run(debug=True)



##Colores en base a las imagenes del banco LSE
## #02735E
## #B4D9D2
## #1A2601
## #F2CAA7
## #D99379