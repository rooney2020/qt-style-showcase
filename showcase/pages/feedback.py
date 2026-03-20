from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame,
    QGraphicsDropShadowEffect, QGraphicsOpacityEffect, QScrollArea,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve

from showcase.theme import btn_primary, btn_secondary, btn_danger, btn_outline
from showcase.constants import C


class _Toast(QFrame):
    def __init__(self, parent, msg, color_key='blue', icon="ℹ️"):
        super().__init__(parent)
        self.setStyleSheet(f"""
            QFrame {{
                background: {C['base']};
                border: 1px solid {C[color_key]};
                border-left: 4px solid {C[color_key]};
                border-radius: 8px;
            }}
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)

        icon_lbl = QLabel(icon)
        icon_lbl.setStyleSheet(f"font-size: 18px; border: none; color: {C[color_key]};")
        layout.addWidget(icon_lbl)

        text_lbl = QLabel(msg)
        text_lbl.setStyleSheet(f"color: {C['text']}; font-size: 13px; border: none;")
        text_lbl.setWordWrap(True)
        layout.addWidget(text_lbl, 1)

        close_btn = QPushButton("✕")
        close_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent; color: {C['overlay0']};
                border: none; font-size: 14px; padding: 4px;
                min-width: 24px; max-width: 24px;
            }}
            QPushButton:hover {{ color: {C['text']}; }}
        """)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self._fade_out)
        layout.addWidget(close_btn)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(16)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)

        self.setMaximumWidth(450)

    def _fade_out(self):
        self._opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._opacity)
        self._anim = QPropertyAnimation(self._opacity, b"opacity")
        self._anim.setDuration(200)
        self._anim.setStartValue(1.0)
        self._anim.setEndValue(0.0)
        self._anim.setEasingCurve(QEasingCurve.OutQuad)
        self._anim.finished.connect(self.deleteLater)
        self._anim.start()


class FeedbackPage(QWidget):
    def __init__(self):
        super().__init__()
        self._toast_container = None

        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        layout.addWidget(self._heading("反馈与通知 Feedback"))

        # --- Toast ---
        layout.addWidget(self._section("消息通知 Toast"))
        desc = QLabel("点击按钮触发不同类型的 Toast 通知")
        desc.setStyleSheet(f"color: {C['subtext0']}; font-size: 13px;")
        layout.addWidget(desc)

        row = QHBoxLayout()
        row.setSpacing(12)
        for text, color, icon in [
            ("信息通知", "blue", "ℹ️"),
            ("成功通知", "green", "✅"),
            ("警告通知", "yellow", "⚠️"),
            ("错误通知", "red", "❌"),
        ]:
            btn = QPushButton(f"{icon} {text}")
            btn.setStyleSheet(btn_outline())
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda _, t=text, c=color, i=icon: self._show_toast(t, c, i))
            row.addWidget(btn)
        row.addStretch()
        layout.addLayout(row)

        self._toast_area = QVBoxLayout()
        self._toast_area.setSpacing(8)
        layout.addLayout(self._toast_area)

        # --- 静态 Toast 展示 ---
        layout.addWidget(self._section("Toast 样式预览"))
        for msg, color, icon in [
            ("操作成功！数据已保存到数据库。", "green", "✅"),
            ("请注意：系统将在 5 分钟后自动重启。", "yellow", "⚠️"),
            ("上传失败：文件大小超过限制（最大 10MB）。", "red", "❌"),
            ("新版本 v2.1.0 已可用，点击查看更新日志。", "blue", "ℹ️"),
        ]:
            toast = _Toast(self, msg, color, icon)
            layout.addWidget(toast)

        # --- 状态标签 ---
        layout.addWidget(self._section("状态标签 Status"))
        row2 = QHBoxLayout()
        row2.setSpacing(12)
        statuses = [
            ("● 在线", "green"), ("● 离线", "red"), ("● 空闲", "yellow"),
            ("● 勿扰", "mauve"), ("● 忙碌", "peach"),
        ]
        for text, color in statuses:
            lbl = QLabel(text)
            lbl.setStyleSheet(f"""
                QLabel {{
                    color: {C[color]}; background: transparent;
                    font-size: 13px; font-weight: bold;
                    padding: 4px 12px; border: 1px solid {C[color]};
                    border-radius: 12px;
                }}
            """)
            row2.addWidget(lbl)
        row2.addStretch()
        layout.addLayout(row2)

        # --- Loading 指示 ---
        layout.addWidget(self._section("加载指示"))
        self._loading_dots = QLabel("加载中")
        self._loading_dots.setStyleSheet(f"color: {C['blue']}; font-size: 14px;")
        layout.addWidget(self._loading_dots)
        self._dot_count = 0
        self._dot_timer = QTimer(self)
        self._dot_timer.timeout.connect(self._update_dots)
        self._dot_timer.start(500)

        layout.addStretch()

    def _show_toast(self, text, color, icon):
        toast = _Toast(self, f"{text} — {icon} 这是一条动态生成的通知消息。", color, icon)
        self._toast_area.addWidget(toast)
        QTimer.singleShot(4000, lambda: toast._fade_out() if toast.parent() else None)

    def _update_dots(self):
        self._dot_count = (self._dot_count + 1) % 4
        self._loading_dots.setText("加载中" + "." * self._dot_count)

    def _heading(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {C['text']}; margin-bottom: 4px;")
        return lbl

    def _section(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {C['blue']}; margin-top: 8px;")
        return lbl
