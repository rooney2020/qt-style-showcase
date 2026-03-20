from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,
)
from PyQt5.QtCore import Qt

from showcase.theme import (
    btn_primary, btn_secondary, btn_danger, btn_success,
    btn_warning, btn_outline, btn_ghost, btn_icon,
)
from showcase.constants import C


class ButtonsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("按钮 Buttons"))

        layout.addWidget(self._section("实色按钮"))
        row = QHBoxLayout()
        row.setSpacing(12)
        for label, style_fn, tip in [
            ("主按钮 Primary", btn_primary, "主操作，如确认、提交"),
            ("次按钮 Secondary", btn_secondary, "普通操作"),
            ("危险 Danger", btn_danger, "删除、破坏性操作"),
            ("成功 Success", btn_success, "完成、通过"),
            ("警告 Warning", btn_warning, "警告类操作"),
        ]:
            btn = QPushButton(label)
            btn.setStyleSheet(style_fn())
            btn.setToolTip(tip)
            btn.setCursor(Qt.PointingHandCursor)
            row.addWidget(btn)
        row.addStretch()
        layout.addLayout(row)

        layout.addWidget(self._section("变体按钮"))
        row2 = QHBoxLayout()
        row2.setSpacing(12)
        btn_o = QPushButton("描边 Outline")
        btn_o.setStyleSheet(btn_outline())
        btn_o.setCursor(Qt.PointingHandCursor)
        row2.addWidget(btn_o)

        btn_g = QPushButton("幽灵 Ghost")
        btn_g.setStyleSheet(btn_ghost())
        btn_g.setCursor(Qt.PointingHandCursor)
        row2.addWidget(btn_g)

        for emoji in ["⚙", "🔔", "✏", "🗑", "➕"]:
            btn_i = QPushButton(emoji)
            btn_i.setStyleSheet(btn_icon())
            btn_i.setToolTip("图标按钮")
            btn_i.setCursor(Qt.PointingHandCursor)
            row2.addWidget(btn_i)
        row2.addStretch()
        layout.addLayout(row2)

        layout.addWidget(self._section("按钮尺寸"))
        row3 = QHBoxLayout()
        row3.setSpacing(12)
        for text, pad in [("小号 Small", "4px 12px"), ("中号 Medium", "8px 20px"), ("大号 Large", "12px 32px")]:
            btn = QPushButton(text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {C['blue']}; color: {C['crust']};
                    border: none; border-radius: 8px;
                    padding: {pad}; font-size: 13px; font-weight: bold;
                }}
                QPushButton:hover {{ background: {C['lavender']}; }}
            """)
            btn.setCursor(Qt.PointingHandCursor)
            row3.addWidget(btn)
        row3.addStretch()
        layout.addLayout(row3)

        layout.addWidget(self._section("禁用状态"))
        row4 = QHBoxLayout()
        row4.setSpacing(12)
        for label, style_fn in [
            ("主按钮 Disabled", btn_primary),
            ("次按钮 Disabled", btn_secondary),
        ]:
            btn = QPushButton(label)
            btn.setStyleSheet(style_fn())
            btn.setEnabled(False)
            row4.addWidget(btn)
        row4.addStretch()
        layout.addLayout(row4)

        layout.addWidget(self._section("按钮组"))
        row5 = QHBoxLayout()
        row5.setSpacing(0)
        group_btns = ["日", "周", "月", "年"]
        for i, text in enumerate(group_btns):
            btn = QPushButton(text)
            is_first = i == 0
            is_last = i == len(group_btns) - 1
            is_active = i == 1
            if is_first:
                radius = "10px 0 0 10px"
            elif is_last:
                radius = "0 10px 10px 0"
            else:
                radius = "0"
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {C['blue'] if is_active else C['surface0']};
                    color: {C['crust'] if is_active else C['text']};
                    border: none;
                    border-right: 1px solid {C['mantle'] if not is_last else 'transparent'};
                    border-radius: {radius};
                    padding: 10px 26px; font-size: 13px;
                    font-weight: {'bold' if is_active else 'normal'};
                }}
                QPushButton:hover {{
                    background: {C['lavender'] if is_active else C['surface1']};
                    color: {C['crust'] if is_active else C['text']};
                }}
            """)
            btn.setCursor(Qt.PointingHandCursor)
            row5.addWidget(btn)
        row5.addStretch()
        layout.addLayout(row5)

        layout.addStretch()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
