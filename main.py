import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from graph import GraphHandler

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TREE')
        self.setGeometry(100, 100, 1618, 1000)
        self.center()

        layout = QVBoxLayout()

        # 1. 创建输入框和按钮所在的水平布局
        input_layout = QHBoxLayout()

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText(" Enter a sentence (e.g., This is an example)")
        self.input_box.setFixedHeight(50)
        input_layout.addWidget(self.input_box)

        generate_button = QPushButton('Generate', self)
        generate_button.setFixedHeight(50)
        generate_button.setFixedWidth(200)
        generate_button.clicked.connect(self.generate_graph)
        input_layout.addWidget(generate_button)

        layout.addLayout(input_layout)

        # 3. 

        # 2.
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

        self.graph_handler = GraphHandler()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def generate_graph(self):
        '''展示图'''
        input_text = self.input_box.text()
        self.graph_handler.create_graph(input_text)
        self.graph_handler.show_graph()

        pixmap = QPixmap('image/graph.png')
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
