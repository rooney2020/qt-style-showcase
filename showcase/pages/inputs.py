from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
    QComboBox, QCheckBox, QRadioButton, QSlider, QSpinBox, QDoubleSpinBox,
    QProgressBar, QButtonGroup, QDateEdit, QTimeEdit, QFrame,
)
from PyQt5.QtCore import Qt, QTimer

from showcase.theme import (
    lineedit_style, textedit_style, combobox_style, checkbox_style,
    radiobutton_style, slider_style, progressbar_style, spinbox_style,
    style_combobox,
)
from showcase.constants import C


class InputsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("输入控件 Inputs"))

        # --- 输入框 ---
        layout.addWidget(self._section("文本输入框 QLineEdit"))
        for placeholder, enabled in [
            ("请输入内容…", True),
            ("已禁用的输入框", False),
        ]:
            le = QLineEdit()
            le.setPlaceholderText(placeholder)
            le.setEnabled(enabled)
            le.setStyleSheet(lineedit_style())
            le.setMaximumWidth(400)
            layout.addWidget(le)

        le_pwd = QLineEdit()
        le_pwd.setPlaceholderText("密码输入")
        le_pwd.setEchoMode(QLineEdit.Password)
        le_pwd.setStyleSheet(lineedit_style())
        le_pwd.setMaximumWidth(400)
        layout.addWidget(le_pwd)

        # --- 多行文本 ---
        layout.addWidget(self._section("多行文本 QTextEdit"))
        te = QTextEdit()
        te.setPlaceholderText("在此输入多行内容…")
        te.setStyleSheet(textedit_style())
        te.setMaximumHeight(100)
        te.setMaximumWidth(500)
        layout.addWidget(te)

        # --- 下拉框 ---
        layout.addWidget(self._section("下拉选择 QComboBox"))
        row = QHBoxLayout()
        cb = QComboBox()
        cb.addItems(["Catppuccin Mocha", "Catppuccin Latte", "Nord", "Dracula", "One Dark"])
        style_combobox(cb)
        cb.setMaximumWidth(250)
        row.addWidget(cb)

        cb2 = QComboBox()
        cb2.setEditable(True)
        cb2.addItems(["可编辑选项 1", "可编辑选项 2", "可编辑选项 3"])
        style_combobox(cb2)
        cb2.setMaximumWidth(250)
        row.addWidget(cb2)
        row.addStretch()
        layout.addLayout(row)


        # --- 复选框 ---
        layout.addWidget(self._section("复选框 QCheckBox"))
        row2 = QHBoxLayout()
        row2.setSpacing(20)
        for text, checked, enabled in [
            ("未选中", False, True),
            ("已选中", True, True),
            ("已禁用", False, False),
        ]:
            chk = QCheckBox(text)
            chk.setChecked(checked)
            chk.setEnabled(enabled)
            chk.setStyleSheet(checkbox_style())
            row2.addWidget(chk)
        row2.addStretch()
        layout.addLayout(row2)

        # --- 单选框 ---
        layout.addWidget(self._section("单选框 QRadioButton"))
        row3 = QHBoxLayout()
        row3.setSpacing(20)
        group = QButtonGroup(self)
        for i, text in enumerate(["选项 A", "选项 B", "选项 C"]):
            rb = QRadioButton(text)
            if i == 0:
                rb.setChecked(True)
            rb.setStyleSheet(radiobutton_style())
            group.addButton(rb)
            row3.addWidget(rb)
        row3.addStretch()
        layout.addLayout(row3)

        # --- 滑块 ---
        layout.addWidget(self._section("滑块 QSlider"))
        row4 = QHBoxLayout()
        sl = QSlider(Qt.Horizontal)
        sl.setRange(0, 100)
        sl.setValue(40)
        sl.setStyleSheet(slider_style())
        sl.setMaximumWidth(400)
        self._slider_label = QLabel("40")
        self._slider_label.setStyleSheet(f"color: {C['text']}; font-size: 13px; min-width: 30px;")
        sl.valueChanged.connect(lambda v: self._slider_label.setText(str(v)))
        row4.addWidget(sl)
        row4.addWidget(self._slider_label)
        row4.addStretch()
        layout.addLayout(row4)

        # --- 数字输入 ---
        layout.addWidget(self._section("数字输入 QSpinBox"))
        row5 = QHBoxLayout()
        row5.setSpacing(12)
        sp = QSpinBox()
        sp.setRange(0, 100)
        sp.setValue(42)
        sp.setStyleSheet(spinbox_style())
        sp.setMaximumWidth(150)
        row5.addWidget(sp)

        dsp = QDoubleSpinBox()
        dsp.setRange(0, 1)
        dsp.setSingleStep(0.1)
        dsp.setValue(0.5)
        dsp.setStyleSheet(spinbox_style())
        dsp.setMaximumWidth(150)
        row5.addWidget(dsp)
        row5.addStretch()
        layout.addLayout(row5)

        # --- 进度条 ---
        layout.addWidget(self._section("进度条 QProgressBar"))
        self._prog = QProgressBar()
        self._prog.setRange(0, 100)
        self._prog.setValue(0)
        self._prog.setStyleSheet(progressbar_style())
        self._prog.setMaximumWidth(400)
        self._prog.setTextVisible(False)
        layout.addWidget(self._prog)

        prog_colors = [
            (C['green'], "成功进度"),
            (C['peach'], "上传进度"),
            (C['red'], "错误进度"),
        ]
        for color, tip in prog_colors:
            p = QProgressBar()
            p.setRange(0, 100)
            p.setValue(65)
            p.setStyleSheet(f"""
                QProgressBar {{
                    background: {C['surface0']}; border: none;
                    border-radius: 6px; height: 12px;
                }}
                QProgressBar::chunk {{
                    background: {color}; border-radius: 6px;
                }}
            """)
            p.setMaximumWidth(400)
            p.setTextVisible(False)
            p.setToolTip(tip)
            layout.addWidget(p)

        self._prog_timer = QTimer(self)
        self._prog_timer.timeout.connect(self._tick_progress)
        self._prog_timer.start(80)

        layout.addStretch()

    def _tick_progress(self):
        v = (self._prog.value() + 1) % 101
        self._prog.setValue(v)

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
