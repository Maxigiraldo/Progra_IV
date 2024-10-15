import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

def on_button_click():
    label.setText("¡Hola, Mundo!")

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
window = QWidget()
window.setWindowTitle("Ejemplo PyQt")

# Crear un layout vertical
layout = QVBoxLayout()

# Crear un Label
label = QLabel("¡Bienvenido a PyQt!")
layout.addWidget(label)

# Crear un botón
button = QPushButton("Haz clic aquí")
button.clicked.connect(on_button_click)
layout.addWidget(button)

# Establecer el layout en la ventana
window.setLayout(layout)

# Mostrar la ventana
window.show()

# Ejecutar el bucle principal
sys.exit(app.exec_())
