from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageHoverWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the QLabel for the image
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)  # Enable scaling
        self.image_label.hide()  # Hide initially

        # Create a layout for proper resizing
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.setLayout(layout)

    def enterEvent(self, event):
        self.image_label.show()

    def leaveEvent(self, event):
        self.image_label.hide()

if __name__ == "__main__":
    app = QApplication([])
    widget = ImageHoverWidget()
    widget.show()
    app.exec_()
