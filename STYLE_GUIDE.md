# PyQt5 通用样式规范

适用于所有基于 PyQt5 的项目，统一 UI 风格和交互体验。

> **样式展示 Demo**：`/home/tsdl/ssd/temp/projects/ingo/qt-style-showcase/`
> 运行 `python3 main.py` 可查看所有组件的实际渲染效果，支持实时切换主题。

## 主题系统

使用主题字典 `C` 提供所有颜色值。支持以下主题：

| 主题 | 风格 |
|---|---|
| Catppuccin Mocha | 暖色调深色（推荐默认） |
| Catppuccin Latte | 浅色 |
| Nord | 北极蓝色调 |
| Dracula | 经典紫色调深色 |
| One Dark | Atom 风格深色 |

### 颜色语义

| 颜色键 | 用途 | 示例场景 |
|---|---|---|
| `base` | 组件/对话框主背景 | 卡片背景、弹窗背景 |
| `mantle` | 次级背景 | 工具栏、标签栏、侧边栏 |
| `crust` | 最深背景 | 面板底色、窗口底色 |
| `surface0` | 输入框/分隔线背景 | QLineEdit 背景、菜单背景 |
| `surface1` | 悬停态/滚动条 | hover 状态、scrollbar handle |
| `surface2` | 选中态/强调边框 | active 状态、focused border |
| `overlay0` | 提示文字 | placeholder、辅助信息 |
| `text` | 主文字 | 所有正文内容 |
| `subtext0` | 次要文字 | 描述、标签、时间戳 |
| `blue` | 主强调色 | 焦点、链接、主按钮 |
| `green` | 成功/运行 | 完成状态、在线、CPU |
| `red` | 错误/删除 | 错误提示、危险按钮、删除 |
| `peach` | 上传/次级强调 | 上传进度、警告 |
| `teal` | 下载/第三强调 | 下载进度、信息 |
| `yellow` | 提醒 | 警告、便签默认色 |
| `mauve` | 装饰 | 标签、第四强调 |
| `lavender` | 装饰 | hover accent、第五强调 |

### 透明度背景

当需要组件背景支持透明度时，使用 RGBA 格式：

```python
def _bg(color_key, opacity=None):
    """将主题颜色转为带透明度的 RGBA"""
    hex_color = C[color_key]
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    a = opacity if opacity is not None else comp_opacity
    return f"rgba({r},{g},{b},{a})"
```

**规则**：
- 文字、图标、按钮文字 → 保持不透明
- 容器背景、分隔线、输入框背景 → 跟随透明度

---

## 滚动条

**必须使用统一函数**生成样式，不要手写。

```python
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
```

| 场景 | 宽度 |
|---|---|
| 默认 | 6px |
| 紧凑（小组件内） | 4px |
| 宽松（大列表） | 8px |

---

## 输入框

### 单行输入 QLineEdit

```python
f"""
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
```

### 多行文本 QTextEdit

```python
f"""
QTextEdit, QPlainTextEdit {{
    background: {C['surface0']}; color: {C['text']};
    border: 1px solid {C['surface1']}; border-radius: 8px;
    padding: 8px; font-size: 13px;
    selection-background-color: {C['blue']};
    selection-color: {C['crust']};
}}
QTextEdit:focus, QPlainTextEdit:focus {{ border-color: {C['blue']}; }}
"""
```

### 下拉选择 QComboBox

```python
f"""
QComboBox {{
    background: {C['surface0']}; color: {C['text']};
    border: 1px solid {C['surface1']}; border-radius: 8px;
    padding: 6px 12px; font-size: 13px; min-height: 20px;
}}
QComboBox:hover {{ border-color: {C['surface2']}; }}
QComboBox:focus {{ border-color: {C['blue']}; }}
QComboBox::drop-down {{
    subcontrol-origin: padding; subcontrol-position: top right;
    width: 28px; border: none; border-radius: 8px;
}}
QComboBox::down-arrow {{
    image: none; width: 0; height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid {C['text']};
}}
QComboBox QAbstractItemView {{
    background: {C['surface0']}; color: {C['text']};
    border: 1px solid {C['surface1']}; border-radius: 8px;
    selection-background-color: {C['surface1']};
    selection-color: {C['text']};
    outline: none; padding: 4px;
}}
QComboBox QAbstractItemView::item {{
    padding: 6px 12px; border-radius: 4px; margin: 1px;
}}
QComboBox QAbstractItemView::item:hover {{ background: {C['surface1']}; }}
"""
```

### 数字输入 QSpinBox / QDoubleSpinBox

```python
f"""
QSpinBox, QDoubleSpinBox {{
    background: {C['surface0']}; color: {C['text']};
    border: 1px solid {C['surface1']}; border-radius: 8px;
    padding: 6px 12px; font-size: 13px;
}}
QSpinBox:focus, QDoubleSpinBox:focus {{ border-color: {C['blue']}; }}
QSpinBox::up-button, QDoubleSpinBox::up-button {{
    subcontrol-origin: border; subcontrol-position: top right;
    width: 24px; border: none;
}}
QSpinBox::down-button, QDoubleSpinBox::down-button {{
    subcontrol-origin: border; subcontrol-position: bottom right;
    width: 24px; border: none;
}}
"""
```

---

## 选择控件

### 复选框 QCheckBox

```python
f"""
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
}}
QCheckBox::indicator:checked:hover {{ background: {C['lavender']}; border-color: {C['lavender']}; }}
QCheckBox:disabled {{ color: {C['overlay0']}; }}
"""
```

### 单选框 QRadioButton

```python
f"""
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
    background: {C['blue']}; border-color: {C['blue']};
}}
"""
```

### 滑块 QSlider

```python
f"""
QSlider::groove:horizontal {{
    height: 6px; background: {C['surface0']}; border-radius: 3px;
}}
QSlider::handle:horizontal {{
    width: 18px; height: 18px; margin: -6px 0;
    background: {C['blue']}; border-radius: 9px;
}}
QSlider::handle:horizontal:hover {{ background: {C['lavender']}; }}
QSlider::sub-page:horizontal {{
    background: {C['blue']}; border-radius: 3px;
}}
"""
```

---

## 按钮

### 主按钮（强调操作）
```python
f"""
QPushButton {{
    background: {C['blue']}; color: {C['crust']};
    border: none; border-radius: 8px;
    padding: 8px 20px; font-size: 13px; font-weight: bold;
}}
QPushButton:hover {{ background: {C['lavender']}; }}
QPushButton:pressed {{ background: {C['sapphire']}; }}
QPushButton:disabled {{ background: {C['surface1']}; color: {C['overlay0']}; }}
"""
```

### 次按钮（普通操作）
```python
f"""
QPushButton {{
    background: {C['surface0']}; color: {C['text']};
    border: none; border-radius: 8px;
    padding: 8px 16px; font-size: 13px;
}}
QPushButton:hover {{ background: {C['surface1']}; }}
QPushButton:pressed {{ background: {C['surface2']}; }}
QPushButton:disabled {{ background: {C['mantle']}; color: {C['overlay0']}; }}
"""
```

### 危险按钮（删除/破坏性操作）
```python
f"""
QPushButton {{
    background: {C['red']}; color: {C['crust']};
    border: none; border-radius: 8px;
    padding: 8px 16px; font-size: 13px; font-weight: bold;
}}
QPushButton:hover {{ background: {C['maroon']}; }}
QPushButton:pressed {{ background: {C['flamingo']}; }}
"""
```

### 成功按钮
```python
f"""
QPushButton {{
    background: {C['green']}; color: {C['crust']};
    border: none; border-radius: 8px;
    padding: 8px 16px; font-size: 13px; font-weight: bold;
}}
QPushButton:hover {{ background: {C['teal']}; }}
"""
```

### 警告按钮
```python
f"""
QPushButton {{
    background: {C['yellow']}; color: {C['crust']};
    border: none; border-radius: 8px;
    padding: 8px 16px; font-size: 13px; font-weight: bold;
}}
QPushButton:hover {{ background: {C['peach']}; }}
"""
```

### 描边按钮（Outline）
```python
f"""
QPushButton {{
    background: transparent; color: {C['blue']};
    border: 1px solid {C['blue']}; border-radius: 8px;
    padding: 8px 16px; font-size: 13px;
}}
QPushButton:hover {{ background: rgba(137,180,250,0.1); }}
QPushButton:pressed {{ background: rgba(137,180,250,0.2); }}
"""
```

### 幽灵按钮（Ghost）
```python
f"""
QPushButton {{
    background: transparent; color: {C['text']};
    border: none; border-radius: 8px;
    padding: 8px 16px; font-size: 13px;
}}
QPushButton:hover {{ background: {C['surface0']}; }}
QPushButton:pressed {{ background: {C['surface1']}; }}
"""
```

### 图标按钮（圆形）
```python
f"""
QPushButton {{
    background: {C['surface0']}; color: {C['text']};
    border: none; border-radius: 20px;
    min-width: 40px; max-width: 40px;
    min-height: 40px; max-height: 40px;
    font-size: 22px;
    padding-bottom: 4px;  /* 补偿 emoji baseline 偏移 */
}}
QPushButton:hover {{ background: {C['surface1']}; }}
QPushButton:pressed {{ background: {C['surface2']}; }}
"""
```

> ⚠️ 使用 emoji 作为图标时存在 baseline 偏移问题，详见「已知问题」。推荐使用 SVG 图标。

### 按钮尺寸

| 尺寸 | padding |
|---|---|
| Small | 4px 12px |
| Medium（默认） | 8px 20px |
| Large | 12px 32px |

### 按钮组

按钮组中的按钮使用 `border-radius` 控制首尾圆角：
- 首个按钮：`8px 0 0 8px`
- 中间按钮：`0`
- 最后按钮：`0 8px 8px 0`

---

## 进度条

```python
f"""
QProgressBar {{
    background: {C['surface0']}; border: none;
    border-radius: 6px; height: 12px;
    text-align: center; color: {C['text']}; font-size: 10px;
}}
QProgressBar::chunk {{
    background: {C['blue']}; border-radius: 6px;
}}
"""
```

不同语义色：
- 成功：`C['green']`
- 上传：`C['peach']`
- 错误：`C['red']`

---

## 卡片/组件

```python
f"""
QFrame[card="true"] {{
    background: {C['base']};
    border: 1px solid {C['surface0']};
    border-radius: 12px;
}}
QFrame[card="true"]:hover {{ border-color: {C['surface2']}; }}
"""
```

阴影效果：
```python
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(24)
shadow.setOffset(0, 4)
shadow.setColor(QColor(0, 0, 0, 80))
widget.setGraphicsEffect(shadow)
```

使用方法：
```python
card = QFrame()
card.setProperty("card", True)
card.setStyleSheet(card_style())
```

---

## 标签 Badge

```python
def badge_style(color_key='blue'):
    return f"""
    QLabel {{
        background: {C[color_key]}; color: {C['crust']};
        border-radius: 4px; font-size: 11px; font-weight: bold;
        padding: 2px 8px;
    }}
    """
```

可用颜色：`blue`、`green`、`yellow`、`red`、`teal`、`mauve`、`peach`、`lavender`

---

## 分组框

```python
f"""
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
```

---

## 列表与表格

### 列表 QListWidget

```python
f"""
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
    background: rgba(137,180,250,0.2);
    color: {C['text']};
}}
"""
```

### 表格 QTableWidget

```python
f"""
QTableWidget {{
    background: {C['base']}; color: {C['text']};
    border: 1px solid {C['surface0']}; border-radius: 8px;
    gridline-color: {C['surface0']}; font-size: 13px;
    selection-background-color: rgba(137,180,250,0.2);
    selection-color: {C['text']};
    outline: none;
}}
QTableWidget::item {{ padding: 6px 10px; }}
QTableWidget::item:hover {{ background: {C['surface0']}; }}
QHeaderView::section {{
    background: {C['mantle']}; color: {C['subtext0']};
    border: none; border-bottom: 1px solid {C['surface0']};
    padding: 8px 10px; font-size: 12px; font-weight: bold;
}}
"""
```

### 树形控件 QTreeWidget

```python
f"""
QTreeWidget {{
    background: {C['base']}; color: {C['text']};
    border: 1px solid {C['surface0']}; border-radius: 8px;
    outline: none; font-size: 13px;
}}
QTreeWidget::item {{
    padding: 4px 8px; border-radius: 4px;
}}
QTreeWidget::item:hover {{ background: {C['surface0']}; }}
QTreeWidget::item:selected {{
    background: rgba(137,180,250,0.2);
    color: {C['text']};
}}
"""
```

---

## 标签页

```python
f"""
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
```

---

## 菜单

### 右键菜单 QMenu

```python
f"""
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
```

### 菜单栏 QMenuBar

```python
f"""
QMenuBar {{
    background: {C['mantle']}; color: {C['text']};
    border: none; font-size: 13px; padding: 2px;
}}
QMenuBar::item {{
    padding: 6px 12px; border-radius: 6px;
}}
QMenuBar::item:selected {{ background: {C['surface0']}; }}
"""
```

---

## 对话框

```python
def dialog_style():
    return f"""
    QDialog {{ background: {C['base']}; color: {C['text']}; border-radius: 16px; }}
    QLabel {{ color: {C['text']}; }}
    QLabel#heading {{ font-size: 18px; font-weight: bold; color: {C['blue']}; }}
    /* 包含 lineedit_style(), combobox_style(), checkbox_style() */
    QPushButton#okBtn {{ /* 主按钮样式 */ }}
    QPushButton#cancelBtn {{ /* 次按钮样式 */ }}
    """
```

**对话框类型**：
- **表单对话框**：包含输入字段、下拉框等，用于收集用户信息
- **信息确认框**：带 ℹ️ 图标，用于确认普通操作
- **危险确认框**：带 ⚠️ 图标和红色确认按钮，用于破坏性操作

---

## 消息通知 Toast

```python
# Toast 结构：左侧彩色边框 + 图标 + 消息文字 + 关闭按钮
QFrame {{
    background: {C['base']};
    border: 1px solid {C[color_key]};
    border-left: 4px solid {C[color_key]};
    border-radius: 8px;
}}
```

| 类型 | 颜色键 | 图标 |
|---|---|---|
| 信息 | `blue` | ℹ️ |
| 成功 | `green` | ✅ |
| 警告 | `yellow` | ⚠️ |
| 错误 | `red` | ❌ |

Toast 应支持自动消失（4 秒）和手动关闭，使用 `QGraphicsOpacityEffect` + `QPropertyAnimation` 做淡出效果。

---

## 状态标签

```python
QLabel {{
    color: {C[color]}; background: transparent;
    font-size: 13px; font-weight: bold;
    padding: 4px 12px; border: 1px solid {C[color]};
    border-radius: 12px;
}}
```

| 状态 | 颜色 |
|---|---|
| 在线 | `green` |
| 离线 | `red` |
| 空闲 | `yellow` |
| 勿扰 | `mauve` |
| 忙碌 | `peach` |

---

## 工具提示

```python
f"""
QToolTip {{
    background: {C['surface0']}; color: {C['text']};
    border: 1px solid {C['surface1']}; border-radius: 6px;
    padding: 6px 10px; font-size: 12px;
}}
"""
```

---

## 字体

| 用途 | 字体优先级 |
|---|---|
| 等宽 | `JetBrains Mono` → `Fira Code` → `Consolas` → `monospace` |
| 中文 | `Noto Sans CJK SC` → `Microsoft YaHei` → `sans-serif` |
| 通用 | 系统默认 |

**默认字号**：
- 正文：13px
- 标题：16-18px（H3-H4）、22px（H2）、28px（H1）
- 辅助文字：11-12px
- 组件标题栏：13px bold
- Badge：11px bold

---

## 间距规范

| 项目 | 值 |
|---|---|
| 组件内边距 | 10-12px |
| 元素间距 | 6-8px |
| 标题区域高度 | 32px |
| 小元素圆角 | 6px |
| 中等区域圆角 | 8px |
| 大区域/卡片圆角 | 12px |
| 对话框圆角 | 16px |
| 按钮圆角 | 8px |
| 图标按钮圆角 | 16px（圆形） |
| 列表项圆角 | 6px |
| 菜单项圆角 | 4px |
| Badge 圆角 | 4px |
| 状态标签圆角 | 12px（胶囊形） |

---

## 图标

| 来源 | 适用场景 |
|---|---|
| `QIcon.fromTheme()` | 系统操作（锁屏、文件管理器、媒体控制等） |
| Emoji | 简单标识（组件类型标签、导航项） |
| SVG 文件 | 应用图标、品牌标识 |

使用 `QIcon.fromTheme()` 时提供 fallback 文本：
```python
icon = QIcon.fromTheme("media-playback-start")
if icon.isNull():
    button.setText("▶")
else:
    button.setIcon(icon)
```

---

## 动画

| 动画 | 时长 | 缓动 |
|---|---|---|
| hover 过渡 | CSS transition（由 Qt 内置处理） | — |
| 展开/折叠 | 200-300ms | `QEasingCurve.OutCubic` |
| 弹出/消失 | 150-250ms | `QEasingCurve.OutQuad` |
| Toast 淡出 | 200ms | `QEasingCurve.OutQuad` |

---

## 全局样式入口

每个项目应在 `QApplication` 或 `QMainWindow` 上设置全局样式：
```python
def global_style():
    return f"""
    * {{ font-family: 'Noto Sans CJK SC', 'Microsoft YaHei', sans-serif; }}
    QMainWindow {{ background: {C['crust']}; }}
    {tooltip_style()}
    {scrollbar_style(6)}
    {menu_style()}
    {menubar_style()}
    """
```

---


## 平台兼容性（重要）

### 必须使用 Fusion 风格

在 Linux 桌面环境中，Qt 默认使用原生平台风格（GTK、KDE 等），这些原生风格可能**完全忽略自定义 QSS**，导致组件样式不一致。

```python
from PyQt5.QtWidgets import QApplication, QStyleFactory

app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create("Fusion"))  # 必须在创建任何窗口之前设置
```

### 必须设置全局 QPalette

仅靠 QSS 无法完全控制所有弹出窗口（如 QComboBox popup、QMenu）的背景色。必须在 QApplication 级别设置暗色调色板：

```python
from PyQt5.QtGui import QPalette, QColor

def apply_dark_palette(app):
    pal = QPalette()
    pal.setColor(QPalette.Window, QColor(C['base']))
    pal.setColor(QPalette.WindowText, QColor(C['text']))
    pal.setColor(QPalette.Base, QColor(C['surface0']))
    pal.setColor(QPalette.AlternateBase, QColor(C['mantle']))
    pal.setColor(QPalette.Text, QColor(C['text']))
    pal.setColor(QPalette.Button, QColor(C['surface0']))
    pal.setColor(QPalette.ButtonText, QColor(C['text']))
    pal.setColor(QPalette.Highlight, QColor(C['blue']))
    pal.setColor(QPalette.HighlightedText, QColor(C['crust']))
    pal.setColor(QPalette.ToolTipBase, QColor(C['surface0']))
    pal.setColor(QPalette.ToolTipText, QColor(C['text']))
    pal.setColor(QPalette.PlaceholderText, QColor(C['overlay0']))
    app.setPalette(pal)

apply_dark_palette(app)  # 在创建窗口之前调用
```

### 主题切换

切换主题时需要**同时更新全局 QPalette**，且所有组件页面应当**重建**（仅 `setStyleSheet()` 不够）：

```python
def _change_theme(self, theme_name):
    C.update(THEMES[theme_name])
    apply_dark_palette(QApplication.instance())
    self.setStyleSheet(global_style())
    self._rebuild_all_pages()  # 销毁旧组件，重新创建
```

---


## 已知问题与注意事项

### QComboBox 下拉列表（popup）样式化

**这是 Qt 在 Linux 上的已知难题。** QComboBox 的 popup 容器 (`QComboBoxPrivateContainer`) 是一个独立的顶层窗口，QSS 父子选择器对它无效。

**推荐做法**：
1. 使用 Fusion 风格 + 全局 QPalette（最基本的保障）
2. 通过 `style_combobox()` 辅助函数设置 view 的 QSS 和 container 的 QPalette
3. 对 popup container 使用 `view().parent()` 获取并设置 QPalette

**已知限制**：
- `QComboBox QFrame` 等 QSS 选择器对 popup 容器**无效**
- 设置 `FramelessWindowHint` 会导致 popup **无法展开**
- `WA_TranslucentBackground` 在某些窗口管理器上无效
- `view().parent()` 在 ComboBox 初始化时可能返回错误的 widget

**建议**：对于需要精确控制下拉样式的场景，考虑使用自定义 QListWidget 替代 QComboBox。

### Emoji 作为图标按钮文字

**问题**：emoji 字符在 QPushButton 中渲染时通常**偏下**，且 font-size 越大偏移越明显。

**原因**：emoji 字体的 baseline 与常规文字不同，Qt 按 baseline 对齐导致视觉偏移。

**缓解方案**：
```python
f"""
QPushButton {{
    font-size: 22px;
    padding-bottom: 4px;  /* 向上补偿 emoji 偏移 */
}}
"""
```

**更好的方案**：使用 SVG 图标文件代替 emoji，通过 `QIcon` 加载：
```python
btn.setIcon(QIcon("assets/settings.svg"))
btn.setIconSize(QSize(20, 20))
```

### QTreeWidget 选中行 branch 区域背景不连续

**问题**：选中 TreeWidget 某行时，名称列左侧的缩进区域（branch 区域）可能没有选中背景色。

**原因**：QSS 的 `::item:selected` 只影响 item 区域，不包括 branch 区域。

**修复**：需要为所有 branch 状态组合添加 `selected` 样式：
```python
f"""
QTreeWidget::branch:selected,
QTreeWidget::branch:has-siblings:selected,
QTreeWidget::branch:!has-siblings:selected,
QTreeWidget::branch:has-children:selected,
QTreeWidget::branch:!has-children:selected,
QTreeWidget::branch:adjoins-item:selected,
QTreeWidget::branch:!adjoins-item:selected {{
    background: rgba(137,180,250,0.2);
}}
"""
```

同时通过 QPalette 设置 Highlight 颜色辅助统一：
```python
pal = tree_widget.palette()
pal.setColor(QPalette.Highlight, QColor(137, 180, 250, 50))
pal.setColor(QPalette.HighlightedText, QColor(C['text']))
tree_widget.setPalette(pal)
```

**建议**：去掉 `::item` 的 `border-radius` 以避免视觉间断。

### QCheckBox/QRadioButton 选中标记

**问题**：默认的选中标记在深色主题中可能不可见或样式不一致。

**修复**：
- **QCheckBox**：使用 SVG 图标显示勾选标记
  ```python
  QCheckBox::indicator:checked {{
      background: {C['blue']}; border-color: {C['blue']};
      image: url(assets/check.svg);
  }}
  ```
- **QRadioButton**：使用 `qradialgradient` 绘制中心圆点
  ```python
  QRadioButton::indicator:checked {{
      background: qradialgradient(
          cx:0.5, cy:0.5, radius:0.4, fx:0.5, fy:0.5,
          stop:0 {C['crust']}, stop:0.4 {C['crust']},
          stop:0.5 {C['blue']}, stop:1.0 {C['blue']}
      );
      border-color: {C['blue']};
  }}
  ```

### QSpinBox / QComboBox 箭头图标

**问题**：深色主题中默认箭头不可见。

**修复**：使用自定义 SVG 图标：
```python
QComboBox::down-arrow {{ image: url(assets/arrow-down.svg); width: 12px; height: 12px; }}
QSpinBox::up-arrow {{ image: url(assets/arrow-up.svg); width: 10px; height: 10px; }}
QSpinBox::down-arrow {{ image: url(assets/arrow-down.svg); width: 10px; height: 10px; }}
```

### QSlider handle 被截断

**问题**：handle 超出 groove 但容器没有足够空间导致被裁剪。

**修复**：给 QSlider 设置最小高度，handle 使用负 margin：
```python
f"""
QSlider {{ min-height: 28px; }}
QSlider::handle:horizontal {{
    width: 20px; height: 20px; margin: -7px 0;
    background: {C['blue']}; border-radius: 10px;
}}
"""
```

### QFormLayout 中的 Label 样式继承

**问题**：父容器的 QSS 可能影响 QFormLayout 的 label 显示（如颜色不可见）。

**修复**：显式创建 QLabel 并设置样式，不依赖 `addRow(str, widget)` 的自动 label：
```python
lbl = QLabel("项目名称")
lbl.setStyleSheet(f"color: {C['subtext0']}; border: none; background: transparent;")
form.addRow(lbl, input_widget)
```

---

## 禁止事项

- ❌ 不要使用原生 QMessageBox、QInputDialog，使用自定义主题对话框
- ❌ 不要硬编码颜色值，必须使用 `C['key']` 或 `_bg('key')`
- ❌ 不要使用 Windows 风格的方角，最小圆角 6px
- ❌ 不要在深色主题中使用纯白/纯黑，使用主题提供的 `text`/`crust`
- ❌ 不要手写滚动条样式，使用 `scrollbar_style()` 函数
- ❌ 不要使用未定义的颜色键，所有颜色必须来自主题字典 `C`
- ❌ 不要忘记设置 `app.setStyle(QStyleFactory.create("Fusion"))`，否则 Linux 上 QSS 可能不生效
- ❌ 不要忘记设置全局 QPalette，否则 popup/下拉列表可能显示为白色背景
- ❌ 不要使用 `FramelessWindowHint` 修改 ComboBox popup 窗口，会导致无法展开
- ❌ 不要依赖 `QFormLayout.addRow(str, widget)` 的自动 label，应显式创建 QLabel 并设置样式
- ❌ 不要在按钮中直接使用 emoji 作为图标时忽略 baseline 偏移补偿

---
