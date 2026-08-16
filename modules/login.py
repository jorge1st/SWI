from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from db_manager import DBManager

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DBManager()
        self.setWindowTitle("Inicio de Sesión")
        try:
            from modules.ui_scaling import scale_px

            self.setFixedSize(scale_px(400), scale_px(320))
        except Exception:
            self.setFixedSize(400, 320)
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                border: 3px solid #BCA7E8;
                border-radius: 15px;
            }
            QLabel {
                font-family: 'Segoe UI';
                font-size: 18px;
                font-weight: bold;
                color: #7A5ACB;
            }
            QLineEdit {
                border: 2px solid #C5B4E3;
                border-radius: 8px;
                padding: 6px 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #7A5ACB;
                color: white;
                font-size: 15px;
                font-weight: bold;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #967DDB;
            }
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("INICIO DE SESIÓN")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")
        layout.addWidget(self.user_input)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_input)

        self.login_btn = QPushButton("Ingresar")
        self.login_btn.clicked.connect(self.verificar_login)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.user_input.text().strip()
        clave = self.pass_input.text().strip()
        if self.db.verificar_usuario(usuario, clave):
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")


