from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QHeaderView,
    QAbstractItemView,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from showcase.theme import (
    listwidget_style, table_style, treewidget_style, scrollbar_style,
    _hex_to_rgba,
)
from showcase.constants import C


class ListsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("列表与表格 Lists & Tables"))

        row = QHBoxLayout()
        row.setSpacing(16)

        # --- 列表 ---
        left = QVBoxLayout()
        left.addWidget(self._section("列表 QListWidget"))
        lw = QListWidget()
        lw.setStyleSheet(listwidget_style() + scrollbar_style(6))
        items = [
            "📁 项目文件", "📄 README.md", "🐍 main.py",
            "🎨 theme.py", "⚙ settings.json", "📦 requirements.txt",
            "📂 src/", "📂 tests/", "📂 docs/",
        ]
        for text in items:
            lw.addItem(QListWidgetItem(text))
        lw.setMaximumHeight(300)
        lw.setMaximumWidth(300)
        left.addWidget(lw)
        left.addStretch()
        row.addLayout(left)

        # --- 树形控件 ---
        right = QVBoxLayout()
        right.addWidget(self._section("树形控件 QTreeWidget"))
        tw = QTreeWidget()
        tw.setHeaderLabels(["名称", "大小", "类型"])
        tw.setStyleSheet(treewidget_style() + scrollbar_style(6))
        tw.setMaximumHeight(300)
        tw.setMaximumWidth(400)
        tw.setAlternatingRowColors(False)
        tw.setIndentation(15)

        root1 = QTreeWidgetItem(tw, ["📂 src", "—", "目录"])
        QTreeWidgetItem(root1, ["main.py", "2.4 KB", "Python"])
        QTreeWidgetItem(root1, ["theme.py", "8.1 KB", "Python"])
        sub = QTreeWidgetItem(root1, ["📂 pages", "—", "目录"])
        QTreeWidgetItem(sub, ["buttons.py", "3.2 KB", "Python"])
        QTreeWidgetItem(sub, ["inputs.py", "4.5 KB", "Python"])

        root2 = QTreeWidgetItem(tw, ["📂 tests", "—", "目录"])
        QTreeWidgetItem(root2, ["test_theme.py", "1.1 KB", "Python"])
        QTreeWidgetItem(root2, ["test_widgets.py", "2.0 KB", "Python"])

        root3 = QTreeWidgetItem(tw, ["📄 README.md", "0.8 KB", "Markdown"])
        root4 = QTreeWidgetItem(tw, ["📄 requirements.txt", "0.1 KB", "Text"])

        tw.expandAll()
        tw.setUniformRowHeights(True)
        pal = tw.palette()
        pal.setColor(QPalette.Highlight, QColor(137, 180, 250, 50))
        pal.setColor(QPalette.HighlightedText, QColor(C['text']))
        tw.setPalette(pal)
        tw.header().setSectionResizeMode(0, QHeaderView.Stretch)
        right.addWidget(tw)
        right.addStretch()
        row.addLayout(right)
        layout.addLayout(row)

        # --- 表格 ---
        layout.addWidget(self._section("表格 QTableWidget"))
        table = QTableWidget(6, 5)
        table.setHorizontalHeaderLabels(["ID", "名称", "状态", "进度", "操作时间"])
        table.setStyleSheet(table_style() + scrollbar_style(6))
        table.setMaximumHeight(250)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.verticalHeader().setVisible(False)

        data = [
            ("001", "数据导入", "✅ 完成", "100%", "2025-01-15 14:30"),
            ("002", "模型训练", "🔄 运行中", "67%", "2025-01-15 15:00"),
            ("003", "报告生成", "⏳ 排队", "0%", "2025-01-15 15:30"),
            ("004", "数据清洗", "✅ 完成", "100%", "2025-01-14 10:00"),
            ("005", "API 部署", "❌ 失败", "45%", "2025-01-14 16:20"),
            ("006", "性能测试", "🔄 运行中", "82%", "2025-01-15 09:00"),
        ]
        for r, row_data in enumerate(data):
            for c, val in enumerate(row_data):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(r, c, item)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(table)

        layout.addStretch()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
