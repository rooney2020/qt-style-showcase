from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QGridLayout,
    QScrollArea,
)
from PyQt5.QtCore import Qt

from showcase.constants import C
from showcase.theme import scrollbar_style


class TypographyPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("排版与颜色 Typography & Colors"))

        # --- 字体层级 ---
        layout.addWidget(self._section("文字层级"))
        for size, weight, color, text in [
            (28, "bold", C['text'], "H1 标题 — 主标题"),
            (22, "bold", C['text'], "H2 标题 — 页面标题"),
            (18, "bold", C['blue'], "H3 标题 — 区域标题"),
            (16, "600", C['text'], "H4 标题 — 小节标题"),
            (14, "normal", C['text'], "正文 Body — 默认段落文字 13-14px"),
            (13, "normal", C['subtext0'], "辅助文字 Caption — 描述、说明 12-13px"),
            (11, "normal", C['overlay0'], "提示文字 Hint — placeholder、脚注 11px"),
        ]:
            lbl = QLabel(text)
            lbl.setStyleSheet(f"font-size: {size}px; font-weight: {weight}; color: {color};")
            layout.addWidget(lbl)

        # --- 等宽字体 ---
        layout.addWidget(self._section("等宽字体"))
        mono = QLabel("const result = await fetch('/api/data');\nconsole.log(result.json());")
        mono.setStyleSheet(f"""
            font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
            font-size: 13px; color: {C['green']};
            background: {C['crust']}; padding: 12px 16px;
            border: 1px solid {C['surface0']}; border-radius: 8px;
        """)
        mono.setMaximumWidth(500)
        layout.addWidget(mono)

        # --- 主题色板 ---
        layout.addWidget(self._section("主题色板"))
        color_grid = QGridLayout()
        color_grid.setSpacing(8)

        colors = [
            ("base", C['base']), ("mantle", C['mantle']), ("crust", C['crust']),
            ("surface0", C['surface0']), ("surface1", C['surface1']), ("surface2", C['surface2']),
            ("overlay0", C['overlay0']), ("text", C['text']), ("subtext0", C['subtext0']),
            ("blue", C['blue']), ("sky", C['sky']), ("teal", C['teal']),
            ("green", C['green']), ("red", C['red']), ("peach", C['peach']),
            ("lavender", C['lavender']), ("yellow", C['yellow']), ("mauve", C['mauve']),
            ("maroon", C['maroon']), ("flamingo", C['flamingo']), ("rosewater", C['rosewater']),
            ("pink", C['pink']), ("sapphire", C['sapphire']),
        ]

        for i, (name, hex_val) in enumerate(colors):
            r, g, b = int(hex_val[1:3], 16), int(hex_val[3:5], 16), int(hex_val[5:7], 16)
            is_light = (r * 0.299 + g * 0.587 + b * 0.114) > 128
            text_color = C['crust'] if is_light else C['text']

            swatch = QFrame()
            swatch.setStyleSheet(f"""
                QFrame {{
                    background: {hex_val};
                    border-radius: 8px;
                    min-height: 60px; min-width: 100px;
                }}
            """)
            sw_layout = QVBoxLayout(swatch)
            sw_layout.setAlignment(Qt.AlignCenter)
            name_lbl = QLabel(name)
            name_lbl.setStyleSheet(f"color: {text_color}; font-size: 12px; font-weight: bold; background: transparent;")
            name_lbl.setAlignment(Qt.AlignCenter)
            sw_layout.addWidget(name_lbl)
            hex_lbl = QLabel(hex_val)
            hex_lbl.setStyleSheet(f"color: {text_color}; font-size: 10px; background: transparent; opacity: 0.8;")
            hex_lbl.setAlignment(Qt.AlignCenter)
            sw_layout.addWidget(hex_lbl)

            row_idx = i // 6
            col_idx = i % 6
            color_grid.addWidget(swatch, row_idx, col_idx)

        layout.addLayout(color_grid)

        # --- 间距参考 ---
        layout.addWidget(self._section("间距与圆角参考"))
        spacing_data = [
            ("小元素圆角", "6px", 6),
            ("中等区域圆角", "8px", 8),
            ("大区域/卡片圆角", "12px", 12),
            ("对话框圆角", "16px", 16),
        ]
        row = QHBoxLayout()
        row.setSpacing(16)
        for label, val, radius in spacing_data:
            box = QFrame()
            box.setStyleSheet(f"""
                QFrame {{
                    background: {C['surface0']};
                    border: 2px solid {C['blue']};
                    border-radius: {radius}px;
                    min-width: 130px; min-height: 90px;
                }}
            """)
            box_layout = QVBoxLayout(box)
            box_layout.setAlignment(Qt.AlignCenter)
            box_layout.setContentsMargins(8, 12, 8, 12)
            r_lbl = QLabel(val)
            r_lbl.setStyleSheet(f"color: {C['blue']}; font-size: 18px; font-weight: bold; background: transparent; border: none;")
            r_lbl.setAlignment(Qt.AlignCenter)
            box_layout.addWidget(r_lbl)
            t_lbl = QLabel(label)
            t_lbl.setStyleSheet(f"color: {C['subtext0']}; font-size: 12px; background: transparent; border: none;")
            t_lbl.setAlignment(Qt.AlignCenter)
            t_lbl.setWordWrap(True)
            box_layout.addWidget(t_lbl)
            row.addWidget(box)
        row.addStretch()
        layout.addLayout(row)

        layout.addStretch()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
