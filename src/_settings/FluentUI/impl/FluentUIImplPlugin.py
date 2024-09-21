from PySide6.QtQml import qmlRegisterUncreatableMetaObject
from ...FluentUI.impl.Frameless import Frameless
from ...FluentUI.impl.Tools import Tools
from ...FluentUI.impl.FileWatcher import FileWatcher
from ...FluentUI.impl.TourBackgroundImpl import TourBackgroundImpl
from ...FluentUI.impl.ControlBackgroundImpl import ControlBackgroundImpl
from ...FluentUI.impl.InputBackgroundImpl import InputBackgroundImpl
from ...FluentUI.impl.RoundRectangle import RoundRectangle
from ...FluentUI.impl.LineNumberModel import LineNumberModel
from ...FluentUI.impl.TextCharFormat import TextCharFormat
from ...FluentUI.impl.SyntaxHighlighterImpl import SyntaxHighlighterImpl
from ...FluentUI.impl.ImageItem import ImageItem
from ...FluentUI.impl.DesktopCaptureItem import DesktopCaptureItem
from ...FluentUI.impl.TabBackgroundImpl import TabBackgroundImpl
from ...FluentUI.impl.WatermarkImpl import WatermarkImpl
from ...FluentUI.impl.QRCodeImpl import QRCodeImpl
from ...FluentUI.impl.StarterImpl import StarterImpl
from ...FluentUI.impl.Def import *
from ...FluentUI.impl.FluentUI import FluentUI
from ...FluentUI.impl.DataGridModel import DataGridModel
from ...FluentUI.impl.TreeDataGridModel import TreeDataGridModel

__uri__ = "FluentUI.impl"
__major__ = 1
__minor__ = 0


# noinspection PyTypeChecker,PyPep8Naming,PyUnresolvedReferences
def registerTypes():
    qmlRegisterUncreatableMetaObject(WindowEffectType.staticMetaObject, __uri__, __major__, __minor__,
                                     "WindowEffectType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(TabViewType.staticMetaObject, __uri__, __major__, __minor__, "TabViewType",
                                     "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(WindowType.staticMetaObject, __uri__, __major__, __minor__, "WindowType",
                                     "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(NavigationViewType.staticMetaObject, __uri__, __major__, __minor__,
                                     "NavigationViewType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(TimePickerType.staticMetaObject, __uri__, __major__, __minor__, "TimePickerType",
                                     "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(DatePickerType.staticMetaObject, __uri__, __major__, __minor__, "DatePickerType",
                                     "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(NumberBoxType.staticMetaObject, __uri__, __major__, __minor__, "NumberBoxType",
                                     "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(InfoBarType.staticMetaObject, __uri__, __major__, __minor__, "InfoBarType",
                                     "Access to enums & flags only")
