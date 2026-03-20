from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialog,
    QLineEdit, QComboBox, QCheckBox, QFormLayout, QFrame,
    QGraphicsDropShadowEffect,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from showcase.theme import (
    btn_primary, btn_secondary, btn_danger, btn_outline,
    dialog_style, lineedit_style, combobox_style, checkbox_style,
    scrollbar_style, style_combobox,
)
from showcase.constants import C


class _SampleDialog(QDialog):
    def __init__(self, parent, title="示例对话框", msg="这是一个自定义主题对话框"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(420)
        self.setStyleSheet(dialog_style() + scrollbar_style())

        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        heading = QLabel(title)
        heading.setObjectName("heading")
        layout.addWidget(heading)

        desc = QLabel(msg)
        desc.setWordWrap(True)
        desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px;")
        layout.addWidget(desc)

        form = QFormLayout()
        form.setSpacing(12)

        name_edit = QLineEdit()
        name_edit.setPlaceholderText("请输入名称")
        name_edit.setStyleSheet(lineedit_style())
        form.addRow("名称", name_edit)

        type_combo = QComboBox()
        type_combo.addItems(["类型 A", "类型 B", "类型 C"])
        style_combobox(type_combo)
        form.addRow("类型", type_combo)

        chk = QCheckBox("启用高级选项")
        chk.setStyleSheet(checkbox_style())
        form.addRow("", chk)

        layout.addLayout(form)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet(f"background: {C['surface0']}; max-height: 1px; border: none;")
        layout.addWidget(sep)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        cancel_btn = QPushButton("取消")
        cancel_btn.setObjectName("cancelBtn")
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(cancel_btn)

        ok_btn = QPushButton("确认")
        ok_btn.setObjectName("okBtn")
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.clicked.connect(self.accept)
        btn_row.addWidget(ok_btn)
        layout.addLayout(btn_row)


class _ConfirmDialog(QDialog):
    def __init__(self, parent, title="确认操作", msg="确定要执行此操作吗？", danger=False):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(380)
        self.setStyleSheet(dialog_style())

        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        icon_text = "⚠️" if danger else "ℹ️"
        icon_label = QLabel(icon_text)
        icon_label.setStyleSheet("font-size: 36px;")
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        heading = QLabel(title)
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignCenter)
        layout.addWidget(heading)

        desc = QLabel(msg)
        desc.setWordWrap(True)
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px;")
        layout.addWidget(desc)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(12)
        btn_row.addStretch()

        cancel_btn = QPushButton("取消")
        cancel_btn.setObjectName("cancelBtn")
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(cancel_btn)

        confirm_btn = QPushButton("确认删除" if danger else "确认")
        if danger:
            confirm_btn.setStyleSheet(btn_danger())
        else:
            confirm_btn.setObjectName("okBtn")
        confirm_btn.setCursor(Qt.PointingHandCursor)
        confirm_btn.clicked.connect(self.accept)
        btn_row.addWidget(confirm_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)


class DialogsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("弹窗与对话框 Dialogs"))

        layout.addWidget(self._section("对话框类型"))
        desc = QLabel("点击按钮查看不同类型的对话框效果")
        desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px;")
        layout.addWidget(desc)

        row = QHBoxLayout()
        row.setSpacing(12)

        btn1 = QPushButton("📝 表单对话框")
        btn1.setStyleSheet(btn_primary())
        btn1.setCursor(Qt.PointingHandCursor)
        btn1.clicked.connect(self._show_form_dialog)
        row.addWidget(btn1)

        btn2 = QPushButton("ℹ 信息确认框")
        btn2.setStyleSheet(btn_secondary())
        btn2.setCursor(Qt.PointingHandCursor)
        btn2.clicked.connect(self._show_info_dialog)
        row.addWidget(btn2)

        btn3 = QPushButton("⚠ 危险确认框")
        btn3.setStyleSheet(btn_danger())
        btn3.setCursor(Qt.PointingHandCursor)
        btn3.clicked.connect(self._show_danger_dialog)
        row.addWidget(btn3)

        row.addStretch()
        layout.addLayout(row)

        # --- 内嵌对话框示例 ---
        layout.addWidget(self._section("内嵌预览"))
        preview = QLabel("（下方展示对话框的静态预览）")
        preview.setStyleSheet(f"color: {C['overlay0']}; font-size: 12px;")
        layout.addWidget(preview)

        embed_frame = QFrame()
        embed_frame.setStyleSheet(f"""
            QFrame {{
                background: {C['base']};
                border: 1px solid {C['surface0']};
                border-radius: 16px;
            }}
            QLabel {{
                color: {C['text']}; border: none; background: transparent;
            }}
        """)
        embed_layout = QVBoxLayout(embed_frame)
        embed_layout.setSpacing(12)
        embed_layout.setContentsMargins(24, 24, 24, 24)

        h = QLabel("✨ 新建项目")
        h.setStyleSheet(f"font-size: 18px; font-weight: bold; color: {C['blue']}; border: none;")
        embed_layout.addWidget(h)

        d = QLabel("请填写项目基本信息，完成后点击确认创建。")
        d.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px; border: none;")
        embed_layout.addWidget(d)

        form = QFormLayout()
        form.setSpacing(10)
        for label_text, placeholder in [
            ("项目名称", "输入项目名称"),
            ("描述", "简要描述项目用途"),
        ]:
            lbl = QLabel(label_text)
            lbl.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px; border: none; background: transparent;")
            le = QLineEdit()
            le.setPlaceholderText(placeholder)
            le.setStyleSheet(lineedit_style())
            form.addRow(lbl, le)

        lang_lbl = QLabel("语言")
        lang_lbl.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px; border: none; background: transparent;")
        cb = QComboBox()
        cb.addItems(["Python", "C++", "JavaScript", "Rust"])
        style_combobox(cb)
        form.addRow(lang_lbl, cb)
        embed_layout.addLayout(form)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet(f"background: {C['surface0']}; max-height: 1px; border: none;")
        embed_layout.addWidget(sep)

        brow = QHBoxLayout()
        brow.addStretch()
        cb_btn = QPushButton("取消")
        cb_btn.setStyleSheet(btn_secondary())
        cb_btn.setCursor(Qt.PointingHandCursor)
        brow.addWidget(cb_btn)
        ok_btn = QPushButton("创建项目")
        ok_btn.setStyleSheet(btn_primary())
        ok_btn.setCursor(Qt.PointingHandCursor)
        brow.addWidget(ok_btn)
        embed_layout.addLayout(brow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(32)
        shadow.setOffset(0, 8)
        shadow.setColor(QColor(0, 0, 0, 100))
        embed_frame.setGraphicsEffect(shadow)
        embed_frame.setMaximumWidth(500)
        layout.addWidget(embed_frame)

        layout.addStretch()

    def _show_form_dialog(self):
        dlg = _SampleDialog(self, "新建组件", "请填写组件的基本信息。")
        dlg.exec_()

    def _show_info_dialog(self):
        dlg = _ConfirmDialog(self, "保存更改", "当前有未保存的更改，是否保存？")
        dlg.exec_()

    def _show_danger_dialog(self):
        dlg = _ConfirmDialog(
            self, "删除项目",
            "此操作不可恢复，项目所有数据将被永久删除。",
            danger=True,
        )
        dlg.exec_()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
