import pygetwindow as gw
import win32gui
import win32con

def set_window_position(window_title, x, y, width, height):
    """
    设置窗口的位置和大小。
    :param window_title: 窗口标题（部分匹配）
    :param x: 窗口的左上角 X 坐标
    :param y: 窗口的左上角 Y 坐标
    :param width: 窗口宽度
    :param height: 窗口高度
    """
    # 查找窗口句柄
    try:
        window = next(w for w in gw.getWindowsWithTitle(window_title) if w.title)
        hwnd = window._hWnd
        
        # 设置窗口位置和大小
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, 0)
    except StopIteration:
        print(f"未找到标题包含 '{window_title}' 的窗口")
