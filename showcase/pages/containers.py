from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QGroupBox,
    QGridLayout, QPushButton, QGraphicsDropShadowEffect,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from showcase.theme import (
    card_style, groupbox_style, btn_primary, btn_secondary, badge_style,
)
from showcase.constants import C


def _make_card(title, content_text, badge_text=None, badge_color='blue'):
    card = QFrame()
    card.setProperty("card", True)
    card.setStyleSheet(card_style())
    card_layout = QVBoxLayout(card)
    card_layout.setSpacing(8)
    card_layout.setContentsMargins(16, 16, 16, 16)

    top = QHBoxLayout()
    title_lbl = QLabel(title)
    title_lbl.setStyleSheet(f"color: {C['text']}; font-size: 14px; font-weight: bold; border: none;")
    top.addWidget(title_lbl)
    if badge_text:
        badge = QLabel(badge_text)
        badge.setStyleSheet(badge_style(badge_color))
        badge.setAlignment(Qt.AlignCenter)
        top.addWidget(badge)
    top.addStretch()
    card_layout.addLayout(top)

    desc = QLabel(content_text)
    desc.setWordWrap(True)
    desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px; border: none;")
    card_layout.addWidget(desc)

    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(24)
    shadow.setOffset(0, 4)
    shadow.setColor(QColor(0, 0, 0, 80))
    card.setGraphicsEffect(shadow)

    return card


class ContainersPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("容器与卡片 Containers"))

        # --- 卡片 ---
        layout.addWidget(self._section("卡片 Card"))
        grid = QGridLayout()
        grid.setSpacing(16)
        cards_data = [
            ("CPU 监控", "当前占用率 32%，温度 65°C", "运行中", "green"),
            ("网络状态", "上传 1.2 MB/s · 下载 5.8 MB/s", "在线", "blue"),
            ("磁盘空间", "已使用 156 GB / 512 GB (30%)", "正常", "teal"),
            ("内存使用", "8.2 GB / 16 GB (51%)", "警告", "yellow"),
            ("系统日志", "最近 24h 共 1,234 条日志", "3 错误", "red"),
            ("任务队列", "12 个任务排队中，2 个执行中", "繁忙", "peach"),
        ]
        for i, (title, desc, badge, color) in enumerate(cards_data):
            card = _make_card(title, desc, badge, color)
            grid.addWidget(card, i // 3, i % 3)
        layout.addLayout(grid)

        # --- 分组框 ---
        layout.addWidget(self._section("分组框 QGroupBox"))
        row = QHBoxLayout()
        row.setSpacing(16)

        gb1 = QGroupBox("基本设置")
        gb1.setStyleSheet(groupbox_style())
        gb1_layout = QVBoxLayout(gb1)
        for text in ["语言：简体中文", "时区：Asia/Shanghai", "主题：Catppuccin Mocha"]:
            lbl = QLabel(text)
            lbl.setStyleSheet(f"color: {C['text']}; font-size: 13px;")
            gb1_layout.addWidget(lbl)
        row.addWidget(gb1)

        gb2 = QGroupBox("高级选项")
        gb2.setStyleSheet(groupbox_style())
        gb2_layout = QVBoxLayout(gb2)
        for text in ["日志级别：DEBUG", "缓存大小：256 MB", "自动备份：每日 02:00"]:
            lbl = QLabel(text)
            lbl.setStyleSheet(f"color: {C['text']}; font-size: 13px;")
            gb2_layout.addWidget(lbl)
        row.addWidget(gb2)
        layout.addLayout(row)

        # --- Badge/标签 ---
        layout.addWidget(self._section("标签 Badge"))
        row2 = QHBoxLayout()
        row2.setSpacing(8)
        for text, color in [
            ("默认", "blue"), ("成功", "green"), ("警告", "yellow"),
            ("错误", "red"), ("信息", "teal"), ("装饰", "mauve"),
            ("次要", "peach"), ("淡雅", "lavender"),
        ]:
            b = QLabel(text)
            b.setStyleSheet(badge_style(color))
            b.setAlignment(Qt.AlignCenter)
            row2.addWidget(b)
        row2.addStretch()
        layout.addLayout(row2)

        # --- 分隔线 ---
        layout.addWidget(self._section("分隔线 Separator"))
        for _ in range(2):
            sep = QFrame()
            sep.setFrameShape(QFrame.HLine)
            sep.setStyleSheet(f"background: {C['surface0']}; max-height: 1px; border: none;")
            layout.addWidget(sep)

        layout.addStretch()

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
