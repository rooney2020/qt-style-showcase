import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from showcase.constants import C
from showcase.main_window import MainWindow


def apply_dark_palette(app):
    """Set application-wide dark palette based on current theme colors."""
    pal = QPalette()
    pal.setColor(QPalette.Window, QColor(C['base']))
    pal.setColor(QPalette.WindowText, QColor(C['text']))
    pal.setColor(QPalette.Base, QColor(C['surface0']))
    pal.setColor(QPalette.AlternateBase, QColor(C['mantle']))
    pal.setColor(QPalette.Text, QColor(C['text']))
    pal.setColor(QPalette.Button, QColor(C['surface0']))
    pal.setColor(QPalette.ButtonText, QColor(C['text']))
    pal.setColor(QPalette.Highlight, QColor(C['blue']))
    pal.setColor(QPalette.HighlightedText, QColor(C['crust']))
    pal.setColor(QPalette.ToolTipBase, QColor(C['surface0']))
    pal.setColor(QPalette.ToolTipText, QColor(C['text']))
    pal.setColor(QPalette.PlaceholderText, QColor(C['overlay0']))
    pal.setColor(QPalette.Link, QColor(C['blue']))
    pal.setColor(QPalette.LinkVisited, QColor(C['lavender']))
    app.setPalette(pal)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("PyQt5 Style Guide Showcase")
    app.setStyle(QStyleFactory.create("Fusion"))
    apply_dark_palette(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
