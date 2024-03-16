from ImageEncrypter import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QPixmap, QImage
import sys, os
from encrypter import LogisticMapping
from PIL import Image

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.encrypter = LogisticMapping()

        self.loadImageButton.clicked.connect(self.loadImageFile)
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.saveImageButton.clicked.connect(self.saveImageFile)
        self.saveImageButton.setEnabled(False)

    
    def decrypt(self):
        if self.keyLineEdit.text() == "" or self.keyLineEdit.text() == None:
            self.outputImageLabel.setText("enter a valid key")
        else:
            self.outputImage = self.encrypter.LogisticDecryption(self.imagePath, self.keyLineEdit.text())
            self.outputImageLabel.setPixmap(self.pil2pixmap(self.outputImage))
            self.outputImageLabel.setScaledContents(True)
            self.encryptButton.setEnabled(False)
            self.saveImageButton.setEnabled(True)


    def encrypt(self):
        if self.keyLineEdit.text() == "" or self.keyLineEdit.text() == None:
            self.outputImageLabel.setText("enter a valid key")
        else:
            self.outputImage = self.encrypter.LogisticEncryption(self.imagePath, self.keyLineEdit.text())
            # qim = ImageQt.(self.encryptedImage)
            # pix = QPixmap.fromImage(qim)
            self.outputImageLabel.setPixmap(self.pil2pixmap(self.outputImage))
            self.outputImageLabel.setScaledContents(True)
            self.decryptButton.setEnabled(False)
            self.saveImageButton.setEnabled(True)



    def saveImageFile(self):
        fileName = QFileDialog.getSaveFileName(self, "Save File", "/home/untitled.png", "Images (*.png *.xpm *.jpg)")
        self.savePath = fileName[0]
        self.outputImage.save(self.savePath, 'png')
        self.outputImageNameLabel.setText(os.path.basename(self.savePath))




    def loadImageFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image", "/home", "Image Files (*.png *.jpg *.xpm *.bmp)")
        self.imagePath = fileName[0]
        self.loadedImageNameLabel.setText(os.path.basename(self.imagePath))
        self.loadImageLabel.setPixmap(QPixmap(self.imagePath))
        self.loadImageLabel.setScaledContents(True)
        self.encryptButton.setEnabled(True)
        self.decryptButton.setEnabled(True)

    def pil2pixmap(self, image):

        if image.mode == "RGB":
            r, g, b = image.split()
            image = Image.merge("RGB", (b, g, r))
        elif  image.mode == "RGBA":
            r, g, b, a = image.split()
            image = Image.merge("RGBA", (b, g, r, a))
        elif image.mode == "L":
            image = image.convert("RGBA")

        
        im2 = image.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, image.size[0], image.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        return pixmap



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())