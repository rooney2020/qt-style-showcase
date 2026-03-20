import os

from showcase.constants import C

_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


def _asset(name):
    return os.path.join(_ASSETS_DIR, name).replace("\\", "/")


def _hex_to_rgba(hex_color, alpha=1.0):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    return f"rgba({r},{g},{b},{alpha})"


def _bg(color_key, opacity=None):
    hex_color = C[color_key]
    a = opacity if opacity is not None else 1.0
    return _hex_to_rgba(hex_color, a)


def scrollbar_style(width=6):
    return f"""
    QScrollBar:vertical {{
        background: transparent; width: {width}px; margin: 0;
    }}
    QScrollBar::handle:vertical {{
        background: {C['surface1']}; min-height: 20px;
        border-radius: {width // 2}px;
    }}
    QScrollBar::handle:vertical:hover {{ background: {C['surface2']}; }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: transparent; }}
    QScrollBar:horizontal {{
        background: transparent; height: {width}px; margin: 0;
    }}
    QScrollBar::handle:horizontal {{
        background: {C['surface1']}; min-width: 20px;
        border-radius: {width // 2}px;
    }}
    QScrollBar::handle:horizontal:hover {{ background: {C['surface2']}; }}
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background: transparent; }}
    """


def tooltip_style():
    return f"""
    QToolTip {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 6px;
        padding: 6px 10px; font-size: 12px;
    }}
    """


def lineedit_style():
    return f"""
    QLineEdit {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 8px;
        padding: 6px 12px; font-size: 13px;
        selection-background-color: {C['blue']};
        selection-color: {C['crust']};
    }}
    QLineEdit:focus {{ border-color: {C['blue']}; }}
    QLineEdit:disabled {{ color: {C['overlay0']}; background: {C['mantle']}; }}
    """


def textedit_style():
    return f"""
    QTextEdit, QPlainTextEdit {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 8px;
        padding: 8px; font-size: 13px;
        selection-background-color: {C['blue']};
        selection-color: {C['crust']};
    }}
    QTextEdit:focus, QPlainTextEdit:focus {{ border-color: {C['blue']}; }}
    """


def _combobox_popup_style():
    """QSS for the popup view - must be set via view().setStyleSheet()"""
    return f"""
    QAbstractItemView {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 6px;
        selection-background-color: {C['surface1']};
        selection-color: {C['text']};
        outline: none; padding: 4px;
    }}
    QAbstractItemView::item {{
        padding: 6px 12px; border-radius: 4px;
        min-height: 22px;
    }}
    QAbstractItemView::item:hover {{
        background: {C['surface1']};
    }}
    QAbstractItemView::item:selected {{
        background: {C['surface1']};
    }}
    """


def combobox_style():
    return f"""
    QComboBox {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 8px;
        padding: 6px 30px 6px 12px; font-size: 13px;
        min-height: 20px;
    }}
    QComboBox:hover {{ border-color: {C['surface2']}; }}
    QComboBox:focus {{ border-color: {C['blue']}; }}
    QComboBox::drop-down {{
        subcontrol-origin: padding; subcontrol-position: center right;
        width: 28px; border: none;
    }}
    QComboBox::down-arrow {{
        image: url({_asset('arrow-down.svg')});
        width: 12px; height: 12px;
    }}
    QComboBox QAbstractItemView {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']};
        border-radius: 6px;
        selection-background-color: {C['surface1']};
        selection-color: {C['text']};
        outline: none; padding: 4px;
    }}
    QComboBox QAbstractItemView::item {{
        padding: 6px 12px;
        min-height: 22px;
    }}
    QComboBox QAbstractItemView::item:hover {{
        background: {C['surface1']};
    }}
    QComboBox QAbstractItemView::item:selected {{
        background: {C['surface1']};
    }}
    QComboBox QFrame {{
        background: {C['surface0']};
        border: 1px solid {C['surface1']};
        border-radius: 6px;
    }}
    """


def style_combobox(combo):
    """Apply styling to a QComboBox, including its popup container."""
    from PyQt5.QtWidgets import QComboBox as _QCB
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtCore import QTimer

    combo.setStyleSheet(combobox_style())
    if combo.view():
        combo.view().setStyleSheet(_combobox_popup_style())

    def _apply_popup_style():
        view = combo.view()
        if not view:
            return
        container = view.parent()
        if container and container is not combo:
            pal = container.palette()
            pal.setColor(QPalette.Window, QColor(C['surface0']))
            pal.setColor(QPalette.Base, QColor(C['surface0']))
            pal.setColor(QPalette.Text, QColor(C['text']))
            container.setPalette(pal)
            container.setAutoFillBackground(True)
            view.setStyleSheet(_combobox_popup_style())

    def _show():
        _QCB.showPopup(combo)
        QTimer.singleShot(0, _apply_popup_style)

    combo.showPopup = _show


def checkbox_style():
    return f"""
    QCheckBox {{
        color: {C['text']}; font-size: 13px; spacing: 8px;
    }}
    QCheckBox::indicator {{
        width: 18px; height: 18px; border-radius: 4px;
        border: 2px solid {C['surface2']};
        background: {C['surface0']};
    }}
    QCheckBox::indicator:hover {{ border-color: {C['blue']}; }}
    QCheckBox::indicator:checked {{
        background: {C['blue']}; border-color: {C['blue']};
        image: url({_asset('check.svg')});
    }}
    QCheckBox::indicator:checked:hover {{ background: {C['lavender']}; border-color: {C['lavender']}; }}
    QCheckBox:disabled {{ color: {C['overlay0']}; }}
    """


def radiobutton_style():
    return f"""
    QRadioButton {{
        color: {C['text']}; font-size: 13px; spacing: 8px;
    }}
    QRadioButton::indicator {{
        width: 18px; height: 18px; border-radius: 9px;
        border: 2px solid {C['surface2']};
        background: {C['surface0']};
    }}
    QRadioButton::indicator:hover {{ border-color: {C['blue']}; }}
    QRadioButton::indicator:checked {{
        background: qradialgradient(
            cx:0.5, cy:0.5, radius:0.4,
            fx:0.5, fy:0.5,
            stop:0 {C['crust']}, stop:0.4 {C['crust']},
            stop:0.5 {C['blue']}, stop:1.0 {C['blue']}
        );
        border-color: {C['blue']};
    }}
    QRadioButton::indicator:checked:hover {{
        background: qradialgradient(
            cx:0.5, cy:0.5, radius:0.4,
            fx:0.5, fy:0.5,
            stop:0 {C['crust']}, stop:0.4 {C['crust']},
            stop:0.5 {C['lavender']}, stop:1.0 {C['lavender']}
        );
        border-color: {C['lavender']};
    }}
    """


def slider_style():
    return f"""
    QSlider {{
        min-height: 28px;
    }}
    QSlider::groove:horizontal {{
        height: 6px; background: {C['surface0']};
        border-radius: 3px;
    }}
    QSlider::handle:horizontal {{
        width: 20px; height: 20px; margin: -7px 0;
        background: {C['blue']}; border-radius: 10px;
    }}
    QSlider::handle:horizontal:hover {{ background: {C['lavender']}; }}
    QSlider::sub-page:horizontal {{
        background: {C['blue']}; border-radius: 3px;
    }}
    QSlider::groove:vertical {{
        width: 6px; background: {C['surface0']};
        border-radius: 3px;
    }}
    QSlider::handle:vertical {{
        width: 20px; height: 20px; margin: 0 -7px;
        background: {C['blue']}; border-radius: 10px;
    }}
    QSlider::handle:vertical:hover {{ background: {C['lavender']}; }}
    QSlider::sub-page:vertical {{
        background: {C['blue']}; border-radius: 3px;
    }}
    """


def progressbar_style():
    return f"""
    QProgressBar {{
        background: {C['surface0']}; border: none;
        border-radius: 6px; height: 12px;
        text-align: center; color: {C['text']}; font-size: 10px;
    }}
    QProgressBar::chunk {{
        background: {C['blue']}; border-radius: 6px;
    }}
    """


def spinbox_style():
    return f"""
    QSpinBox, QDoubleSpinBox {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 8px;
        padding: 6px 12px; font-size: 13px;
    }}
    QSpinBox:focus, QDoubleSpinBox:focus {{ border-color: {C['blue']}; }}
    QSpinBox::up-button, QDoubleSpinBox::up-button {{
        subcontrol-origin: border; subcontrol-position: top right;
        width: 24px; border: none;
        background: transparent;
    }}
    QSpinBox::down-button, QDoubleSpinBox::down-button {{
        subcontrol-origin: border; subcontrol-position: bottom right;
        width: 24px; border: none;
        background: transparent;
    }}
    QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {{
        image: url({_asset('arrow-up.svg')});
        width: 10px; height: 10px;
    }}
    QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {{
        image: url({_asset('arrow-down.svg')});
        width: 10px; height: 10px;
    }}
    QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover {{
        background: {C['surface1']};
    }}
    QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {{
        background: {C['surface1']};
    }}
    """


def tabwidget_style():
    return f"""
    QTabWidget::pane {{
        background: {C['base']}; border: 1px solid {C['surface0']};
        border-radius: 8px; top: -1px;
    }}
    QTabBar::tab {{
        background: {C['mantle']}; color: {C['subtext0']};
        border: none; padding: 10px 20px; font-size: 13px;
        margin-right: 2px; border-radius: 8px 8px 0 0;
    }}
    QTabBar::tab:hover {{ background: {C['surface0']}; color: {C['text']}; }}
    QTabBar::tab:selected {{
        background: {C['base']}; color: {C['blue']};
        font-weight: bold;
    }}
    """


def table_style():
    return f"""
    QTableWidget, QTableView {{
        background: {C['base']}; color: {C['text']};
        border: 1px solid {C['surface0']}; border-radius: 8px;
        gridline-color: {C['surface0']}; font-size: 13px;
        selection-background-color: {_hex_to_rgba(C['blue'], 0.2)};
        selection-color: {C['text']};
        outline: none;
    }}
    QTableWidget::item, QTableView::item {{
        padding: 6px 10px;
    }}
    QTableWidget::item:hover, QTableView::item:hover {{
        background: {C['surface0']};
    }}
    QHeaderView::section {{
        background: {C['mantle']}; color: {C['subtext0']};
        border: none; border-bottom: 1px solid {C['surface0']};
        padding: 8px 10px; font-size: 12px; font-weight: bold;
    }}
    QHeaderView::section:hover {{ color: {C['text']}; }}
    """


def listwidget_style():
    return f"""
    QListWidget {{
        background: {C['base']}; color: {C['text']};
        border: 1px solid {C['surface0']}; border-radius: 8px;
        outline: none; font-size: 13px; padding: 4px;
    }}
    QListWidget::item {{
        padding: 8px 12px; border-radius: 6px; margin: 1px;
    }}
    QListWidget::item:hover {{ background: {C['surface0']}; }}
    QListWidget::item:selected {{
        background: {_hex_to_rgba(C['blue'], 0.2)};
        color: {C['text']};
    }}
    """


def treewidget_style():
    sel_bg = _hex_to_rgba(C['blue'], 0.2)
    return f"""
    QTreeWidget, QTreeView {{
        background: {C['base']}; color: {C['text']};
        border: 1px solid {C['surface0']};
        outline: none; font-size: 13px;
    }}
    QTreeWidget::item, QTreeView::item {{
        padding: 4px 8px;
    }}
    QTreeWidget::item:hover, QTreeView::item:hover {{
        background: {C['surface0']};
    }}
    QTreeWidget::item:selected, QTreeView::item:selected {{
        background: {sel_bg};
        color: {C['text']};
    }}
    QTreeWidget::branch {{
        background: {C['base']};
    }}
    QTreeWidget::branch:selected,
    QTreeView::branch:selected,
    QTreeWidget::branch:has-siblings:selected,
    QTreeWidget::branch:!has-siblings:selected,
    QTreeWidget::branch:has-children:selected,
    QTreeWidget::branch:!has-children:selected,
    QTreeWidget::branch:adjoins-item:selected,
    QTreeWidget::branch:!adjoins-item:selected,
    QTreeWidget::branch:has-siblings:adjoins-item:selected,
    QTreeWidget::branch:!has-siblings:adjoins-item:selected,
    QTreeWidget::branch:has-children:!has-siblings:closed:selected,
    QTreeWidget::branch:closed:has-children:has-siblings:selected,
    QTreeWidget::branch:open:has-children:!has-siblings:selected,
    QTreeWidget::branch:open:has-children:has-siblings:selected {{
        background: {sel_bg};
    }}
    QTreeWidget::branch:hover {{
        background: {C['surface0']};
    }}
    QHeaderView::section {{
        background: {C['mantle']}; color: {C['subtext0']};
        border: none; border-bottom: 1px solid {C['surface0']};
        padding: 6px 10px; font-size: 12px; font-weight: bold;
    }}
    """

def menu_style():
    return f"""
    QMenu {{
        background: {C['surface0']}; color: {C['text']};
        border: 1px solid {C['surface1']}; border-radius: 8px;
        padding: 6px 4px; font-size: 13px;
    }}
    QMenu::item {{
        padding: 8px 28px 8px 16px; border-radius: 4px; margin: 1px 4px;
    }}
    QMenu::item:selected {{ background: {C['surface1']}; }}
    QMenu::item:disabled {{ color: {C['overlay0']}; }}
    QMenu::separator {{ height: 1px; background: {C['surface1']}; margin: 4px 8px; }}
    """


def menubar_style():
    return f"""
    QMenuBar {{
        background: {C['mantle']}; color: {C['text']};
        border: none; font-size: 13px; padding: 2px;
    }}
    QMenuBar::item {{
        padding: 6px 12px; border-radius: 6px;
    }}
    QMenuBar::item:selected {{ background: {C['surface0']}; }}
    """


def groupbox_style():
    return f"""
    QGroupBox {{
        background: {C['base']}; color: {C['text']};
        border: 1px solid {C['surface0']}; border-radius: 12px;
        margin-top: 12px; padding: 16px 12px 12px;
        font-size: 13px; font-weight: bold;
    }}
    QGroupBox::title {{
        subcontrol-origin: margin; subcontrol-position: top left;
        left: 16px; padding: 0 8px;
        color: {C['blue']};
    }}
    """


def dialog_style():
    return f"""
    QDialog {{
        background: {C['base']}; color: {C['text']};
        border-radius: 16px;
    }}
    QLabel {{ color: {C['text']}; }}
    QLabel#heading {{ font-size: 18px; font-weight: bold; color: {C['blue']}; }}
    {lineedit_style()}
    {combobox_style()}
    {checkbox_style()}
    QPushButton#okBtn {{
        background: {C['blue']}; color: {C['crust']};
        border: none; border-radius: 8px;
        padding: 8px 20px; font-size: 13px; font-weight: bold;
    }}
    QPushButton#okBtn:hover {{ background: {C['lavender']}; }}
    QPushButton#cancelBtn {{
        background: {C['surface0']}; color: {C['text']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px;
    }}
    QPushButton#cancelBtn:hover {{ background: {C['surface1']}; }}
    """


def card_style():
    return f"""
    QFrame[card="true"] {{
        background: {C['base']};
        border: 1px solid {C['surface0']};
        border-radius: 12px;
    }}
    QFrame[card="true"]:hover {{ border-color: {C['surface2']}; }}
    """


def btn_primary():
    return f"""
    QPushButton {{
        background: {C['blue']}; color: {C['crust']};
        border: none; border-radius: 8px;
        padding: 8px 20px; font-size: 13px; font-weight: bold;
    }}
    QPushButton:hover {{ background: {C['lavender']}; }}
    QPushButton:pressed {{ background: {C['sapphire']}; }}
    QPushButton:disabled {{ background: {C['surface1']}; color: {C['overlay0']}; }}
    """


def btn_secondary():
    return f"""
    QPushButton {{
        background: {C['surface0']}; color: {C['text']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px;
    }}
    QPushButton:hover {{ background: {C['surface1']}; }}
    QPushButton:pressed {{ background: {C['surface2']}; }}
    QPushButton:disabled {{ background: {C['mantle']}; color: {C['overlay0']}; }}
    """


def btn_danger():
    return f"""
    QPushButton {{
        background: {C['red']}; color: {C['crust']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px; font-weight: bold;
    }}
    QPushButton:hover {{ background: {C['maroon']}; }}
    QPushButton:pressed {{ background: {C['flamingo']}; }}
    """


def btn_success():
    return f"""
    QPushButton {{
        background: {C['green']}; color: {C['crust']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px; font-weight: bold;
    }}
    QPushButton:hover {{ background: {C['teal']}; }}
    """


def btn_warning():
    return f"""
    QPushButton {{
        background: {C['yellow']}; color: {C['crust']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px; font-weight: bold;
    }}
    QPushButton:hover {{ background: {C['peach']}; }}
    """


def btn_outline():
    return f"""
    QPushButton {{
        background: transparent; color: {C['blue']};
        border: 1px solid {C['blue']}; border-radius: 8px;
        padding: 8px 16px; font-size: 13px;
    }}
    QPushButton:hover {{ background: {_hex_to_rgba(C['blue'], 0.1)}; }}
    QPushButton:pressed {{ background: {_hex_to_rgba(C['blue'], 0.2)}; }}
    """


def btn_ghost():
    return f"""
    QPushButton {{
        background: transparent; color: {C['text']};
        border: none; border-radius: 8px;
        padding: 8px 16px; font-size: 13px;
    }}
    QPushButton:hover {{ background: {C['surface0']}; }}
    QPushButton:pressed {{ background: {C['surface1']}; }}
    """


def btn_icon():
    return f"""
    QPushButton {{
        background: {C['surface0']}; color: {C['text']};
        border: none; border-radius: 20px;
        min-width: 40px; max-width: 40px;
        min-height: 40px; max-height: 40px;
        font-size: 22px;
        padding-bottom: 4px;
    }}
    QPushButton:hover {{ background: {C['surface1']}; }}
    QPushButton:pressed {{ background: {C['surface2']}; }}
    """


def badge_style(color_key='blue'):
    return f"""
    QLabel {{
        background: {C[color_key]}; color: {C['crust']};
        border-radius: 4px; font-size: 11px; font-weight: bold;
        padding: 2px 8px;
    }}
    """


def global_style():
    return f"""
    * {{
        font-family: 'Noto Sans CJK SC', 'Microsoft YaHei', sans-serif;
    }}
    QMainWindow {{
        background: {C['crust']};
    }}
    {tooltip_style()}
    {scrollbar_style(6)}
    {menu_style()}
    {menubar_style()}
    """
