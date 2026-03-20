from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget,
    QMenu, QAction, QFrame, QScrollArea, QToolBar, QSizePolicy,
)
from PyQt5.QtCore import Qt

from showcase.theme import (
    tabwidget_style, menu_style, btn_secondary, btn_ghost,
    scrollbar_style, btn_primary,
)
from showcase.constants import C


class NavigationPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("导航组件 Navigation"))

        # --- Tab Widget ---
        layout.addWidget(self._section("标签页 QTabWidget"))
        tabs = QTabWidget()
        tabs.setStyleSheet(tabwidget_style())
        tabs.setMaximumHeight(200)

        for name, content in [
            ("概览", "这是概览标签页的内容区域。可以放置任何组件。"),
            ("详情", "这是详情标签页。展示更多信息。"),
            ("设置", "设置页面，用于配置各项参数。"),
            ("日志", "系统运行日志，记录操作历史。"),
        ]:
            page = QWidget()
            page_layout = QVBoxLayout(page)
            lbl = QLabel(content)
            lbl.setStyleSheet(f"color: {C['text']}; font-size: 13px; padding: 16px;")
            lbl.setAlignment(Qt.AlignCenter)
            page_layout.addWidget(lbl)
            tabs.addTab(page, name)
        layout.addWidget(tabs)

        # --- 右键菜单 ---
        layout.addWidget(self._section("右键菜单 QMenu"))
        menu_desc = QLabel("右键点击下方区域查看菜单，或点击按钮弹出菜单")
        menu_desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px;")
        layout.addWidget(menu_desc)

        row = QHBoxLayout()
        row.setSpacing(12)

        menu_btn = QPushButton("📋 点击弹出菜单")
        menu_btn.setStyleSheet(btn_secondary())
        menu_btn.setCursor(Qt.PointingHandCursor)

        self._demo_menu = QMenu(self)
        self._demo_menu.setStyleSheet(menu_style())
        for icon, text in [
            ("📁", "打开文件"), ("💾", "保存"), ("📤", "导出"),
        ]:
            self._demo_menu.addAction(f"{icon}  {text}")
        self._demo_menu.addSeparator()
        sub_menu = self._demo_menu.addMenu("🎨  主题")
        sub_menu.setStyleSheet(menu_style())
        for theme in ["Catppuccin Mocha", "Catppuccin Latte", "Nord", "Dracula", "One Dark"]:
            sub_menu.addAction(theme)
        self._demo_menu.addSeparator()
        self._demo_menu.addAction("⚙  设置")
        quit_action = self._demo_menu.addAction("🚪  退出")

        menu_btn.clicked.connect(lambda: self._demo_menu.exec_(
            menu_btn.mapToGlobal(menu_btn.rect().bottomLeft())))
        row.addWidget(menu_btn)

        ctx_area = QFrame()
        ctx_area.setStyleSheet(f"""
            QFrame {{
                background: {C['surface0']};
                border: 1px dashed {C['surface2']};
                border-radius: 8px;
                min-height: 60px;
            }}
        """)
        ctx_area.setContextMenuPolicy(Qt.CustomContextMenu)
        ctx_area.customContextMenuRequested.connect(
            lambda pos: self._demo_menu.exec_(ctx_area.mapToGlobal(pos)))
        ctx_lbl = QLabel("右键点击此区域")
        ctx_lbl.setStyleSheet(f"color: {C['overlay0']}; font-size: 13px; border: none;")
        ctx_lbl.setAlignment(Qt.AlignCenter)
        ctx_layout = QVBoxLayout(ctx_area)
        ctx_layout.addWidget(ctx_lbl)
        row.addWidget(ctx_area, 1)
        layout.addLayout(row)

        # --- 工具栏 ---
        layout.addWidget(self._section("工具栏 Toolbar"))
        toolbar_frame = QFrame()
        toolbar_frame.setStyleSheet(f"""
            QFrame {{
                background: {C['mantle']};
                border: 1px solid {C['surface0']};
                border-radius: 10px;
            }}
        """)
        tb_layout = QHBoxLayout(toolbar_frame)
        tb_layout.setContentsMargins(8, 6, 8, 6)
        tb_layout.setSpacing(4)

        logo = QLabel("⚡ StyleGuide")
        logo.setStyleSheet(f"color: {C['blue']}; font-size: 14px; font-weight: bold; border: none; padding: 0 8px;")
        tb_layout.addWidget(logo)
        tb_layout.addSpacing(16)

        for text in ["文件", "编辑", "视图", "工具", "帮助"]:
            btn = QPushButton(text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: transparent; color: {C['subtext0']};
                    border: none; border-radius: 6px;
                    padding: 6px 12px; font-size: 13px;
                }}
                QPushButton:hover {{ background: {C['surface0']}; color: {C['text']}; }}
            """)
            btn.setCursor(Qt.PointingHandCursor)
            tb_layout.addWidget(btn)

        tb_layout.addStretch()

        for emoji, tip in [("🔍", "搜索"), ("🔔", "通知"), ("⚙", "设置")]:
            btn = QPushButton(emoji)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: transparent; color: {C['text']};
                    border: none; border-radius: 20px;
                    min-width: 40px; max-width: 40px;
                    min-height: 40px; max-height: 40px;
                    font-size: 22px;
                    padding-bottom: 4px;
                }}
                QPushButton:hover {{ background: {C['surface0']}; }}
            """)
            btn.setToolTip(tip)
            btn.setCursor(Qt.PointingHandCursor)
            tb_layout.addWidget(btn)

        layout.addWidget(toolbar_frame)

        # --- 侧边栏 ---
        layout.addWidget(self._section("侧边导航 Sidebar"))
        sidebar_row = QHBoxLayout()
        sidebar_row.setSpacing(0)

        sidebar = QFrame()
        sidebar.setStyleSheet(f"""
            QFrame {{
                background: {C['mantle']};
                border: 1px solid {C['surface0']};
                border-radius: 10px 0 0 10px;
                min-width: 200px; max-width: 200px;
            }}
        """)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(8, 12, 8, 12)
        sb_layout.setSpacing(2)

        nav_items = [
            ("🏠", "首页", True),
            ("📊", "仪表盘", False),
            ("👥", "用户管理", False),
            ("📦", "项目", False),
            ("📝", "文档", False),
            ("⚙", "系统设置", False),
        ]
        for icon, text, active in nav_items:
            btn = QPushButton(f" {icon}  {text}")
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
            btn.setCursor(Qt.PointingHandCursor)
            sb_layout.addWidget(btn)
        sb_layout.addStretch()
        sidebar_row.addWidget(sidebar)

        content = QFrame()
        content.setStyleSheet(f"""
            QFrame {{
                background: {C['base']};
                border: 1px solid {C['surface0']};
                border-left: none;
                border-radius: 0 10px 10px 0;
            }}
        """)
        c_layout = QVBoxLayout(content)
        c_layout.setContentsMargins(24, 24, 24, 24)
        c_lbl = QLabel("内容区域\n\n侧边栏选中项的对应内容会在此区域展示。")
        c_lbl.setStyleSheet(f"color: {C['subtext0']}; font-size: 14px; border: none;")
        c_lbl.setAlignment(Qt.AlignCenter)
        c_layout.addWidget(c_lbl)
        sidebar_row.addWidget(content, 1)

        sidebar_container = QFrame()
        sidebar_container.setMaximumHeight(280)
        sc_layout = QHBoxLayout(sidebar_container)
        sc_layout.setContentsMargins(0, 0, 0, 0)
        sc_layout.addLayout(sidebar_row)
        layout.addWidget(sidebar_container)

        layout.addStretch()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
