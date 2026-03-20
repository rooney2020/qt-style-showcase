from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QStackedWidget, QComboBox, QSizePolicy,
)
from PyQt5.QtCore import Qt

from showcase.theme import global_style, scrollbar_style, combobox_style, style_combobox
from PyQt5.QtWidgets import QApplication
from showcase.constants import C, THEMES
from showcase.pages.buttons import ButtonsPage
from showcase.pages.inputs import InputsPage
from showcase.pages.containers import ContainersPage
from showcase.pages.lists import ListsPage
from showcase.pages.dialogs_page import DialogsPage
from showcase.pages.feedback import FeedbackPage
from showcase.pages.navigation import NavigationPage
from showcase.pages.typography import TypographyPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 组件样式展示 — Style Guide Showcase")
        self.setMinimumSize(1100, 750)
        self.resize(1280, 860)

        self._pages = []
        self._nav_buttons = []

        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setStyleSheet(f"""
            QFrame {{
                background: {C['mantle']};
                border-right: 1px solid {C['surface0']};
            }}
        """)
        sidebar.setFixedWidth(220)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(12, 16, 12, 16)
        sb_layout.setSpacing(4)

        logo = QLabel("🎨 Style Guide")
        logo.setStyleSheet(f"""
            font-size: 18px; font-weight: bold; color: {C['blue']};
            padding: 8px 8px 16px;
        """)
        sb_layout.addWidget(logo)

        nav_items = [
            ("🎨", "排版与颜色"),
            ("🔘", "按钮"),
            ("📝", "输入控件"),
            ("📦", "容器与卡片"),
            ("📋", "列表与表格"),
            ("💬", "弹窗与对话框"),
            ("🔔", "反馈与通知"),
            ("🧭", "导航组件"),
        ]

        for i, (icon, text) in enumerate(nav_items):
            btn = QPushButton(f" {icon}  {text}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda _, idx=i: self._switch_page(idx))
            self._nav_buttons.append(btn)
            sb_layout.addWidget(btn)

        sb_layout.addStretch()

        theme_label = QLabel("主题")
        theme_label.setStyleSheet(f"color: {C['subtext0']}; font-size: 12px; padding: 8px 8px 4px;")
        sb_layout.addWidget(theme_label)

        self._theme_combo = QComboBox()
        self._theme_combo.addItems(list(THEMES.keys()))
        style_combobox(self._theme_combo)
        self._theme_combo.currentTextChanged.connect(self._change_theme)
        sb_layout.addWidget(self._theme_combo)

        root_layout.addWidget(sidebar)

        self._stack = QStackedWidget()

        pages = [
            TypographyPage, ButtonsPage, InputsPage, ContainersPage,
            ListsPage, DialogsPage, FeedbackPage, NavigationPage,
        ]
        for PageClass in pages:
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setFrameShape(QFrame.NoFrame)
            scroll.setStyleSheet(f"QScrollArea {{ background: {C['crust']}; border: none; }}"
                                 + scrollbar_style(8))
            page = PageClass()
            page.setStyleSheet(f"background: transparent;")
            scroll.setWidget(page)
            self._stack.addWidget(scroll)
            self._pages.append(page)

        root_layout.addWidget(self._stack, 1)

        self.setStyleSheet(global_style())
        self._switch_page(0)

    def _switch_page(self, idx):
        self._stack.setCurrentIndex(idx)
        for i, btn in enumerate(self._nav_buttons):
            active = i == idx
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {C['surface0'] if active else 'transparent'};
                    color: {C['blue'] if active else C['subtext0']};
                    border: none; border-radius: 8px;
                    padding: 10px 12px; font-size: 13px;
                    text-align: left;
                    font-weight: {'bold' if active else 'normal'};
                }}
                QPushButton:hover {{
                    background: {C['surface0']};
                    color: {C['text']};
                }}
            """)

    def _change_theme(self, theme_name):
        if theme_name in THEMES:
            C.update(THEMES[theme_name])
            from main import apply_dark_palette
            apply_dark_palette(QApplication.instance())
            self.setStyleSheet(global_style())
            self._rebuild_pages()

    def _rebuild_pages(self):
        current_idx = self._stack.currentIndex()
        while self._stack.count() > 0:
            w = self._stack.widget(0)
            self._stack.removeWidget(w)
            w.deleteLater()
        self._pages.clear()

        page_classes = [
            TypographyPage, ButtonsPage, InputsPage, ContainersPage,
            ListsPage, DialogsPage, FeedbackPage, NavigationPage,
        ]
        for PageClass in page_classes:
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setFrameShape(QFrame.NoFrame)
            scroll.setStyleSheet(f"QScrollArea {{ background: {C['crust']}; border: none; }}"
                                 + scrollbar_style(8))
            page = PageClass()
            page.setStyleSheet(f"background: transparent;")
            scroll.setWidget(page)
            self._stack.addWidget(scroll)
            self._pages.append(page)

        sidebar = self.centralWidget().layout().itemAt(0).widget()
        sidebar.setStyleSheet(f"""
            QFrame {{
                background: {C['mantle']};
                border-right: 1px solid {C['surface0']};
            }}
        """)
        logo = sidebar.findChildren(QLabel)[0]
        logo.setStyleSheet(f"font-size: 18px; font-weight: bold; color: {C['blue']}; padding: 8px 8px 16px;")

        style_combobox(self._theme_combo)

        self._stack.setCurrentIndex(min(current_idx, self._stack.count() - 1))
        self._switch_page(self._stack.currentIndex())
