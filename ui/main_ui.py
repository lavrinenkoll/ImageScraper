
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(903, 472)
        Dialog.setStyleSheet(u"\n"
"QMainWindow {\n"
"	background-color:#08020f;\n"
"}\n"
"QDialog {\n"
"	background-color:#08020f;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#08020f;\n"
"}")

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 901, 471))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet(u"\n"
"QMainWindow {\n"
"	background-color:#08020f;\n"
"}\n"
"QDialog {\n"
"	background-color:#08020f;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#08020f;\n"
"}\n"
"QTextEdit {\n"
"	background-color:#000000;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"	selection-background-color:#f39c12;\n"
"	background-color:#000000;\n"
"	border: 1px solid #FF00FF;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"	border: 1px transparent;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #000000;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #480fa3;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #000000;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #FF00FF;\n"
"	border-bott"
                        "om-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 2px;\n"
"	background-color: #000000;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #FF00FF;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #480fa3;\n"
"	padding-bottom: 1px;\n"
"	background-color: #000000;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding-bottom: 1px;\n"
"	background-color: #000000;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
""
                        "	border-left-color: transparent;\n"
"	border-bottom-color: #480fa3;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #000000;\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #480fa3;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: #000000;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#000000;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"	color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"	color: #480fa3;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
""
                        "	border-radius: 10px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	background-color:#000000;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #480fa3;\n"
"	border-radius: 5px;\n"
"}\n"
"QMenu{\n"
"	background-color:#000000;\n"
"}\n"
"QMenuBar {\n"
"	background:rgb(0, 0, 0);\n"
"	color: #a9b7c6;\n"
"}\n"
"QMenuBar::item {\n"
"  	spacing: 3px; \n"
"	padding: 1px 4px;\n"
"  	background: transparent;\n"
"}\n"
"QMenuBar::item:selected { \n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #480fa3;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 0px;\n"
"	background-color: #000000;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: #480fa3;\n"
"	border-bottom-color: transparent;\n"
"	border-l"
                        "eft-width: 2px;\n"
"	color: #FFFFFF;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color:#000000;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(77,77,77);\n"
"		background-color:#000000;\n"
"		border-style: solid;\n"
"		border-width: 1px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
""
                        "	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding: 3px;\n"
"	margin-left:3px;\n"
"	background-color:#08020f;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #480fa3;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-bottom: 2px;\n"
"	margin-left:3px;\n"
"	background-color:#08020f;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#000000;\n"
"}\n"
"QCheckBox::indicator:ch"
                        "ecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #480fa3;\n"
"	color: #a9b7c6;\n"
"	background-color: #480fa3;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #480fa3;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #480fa3;\n"
"	color: #a9b7c6;\n"
"	background-color: #480fa3;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #480fa3;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#34e8eb;\n"
"}\n"
"QS"
                        "pinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QDateEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color:#000000;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color:#000000;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"	color: #a9b7c6;	\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color"
                        ": #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: #480fa3;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: #480fa3;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	height: 14px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #480fa3;\n"
""
                        "}\n"
"QSlider::sub-page:vertical {\n"
"    background: #480fa3;\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	background: rgb(0,0,0);\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(0,0,0);\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(230, 126, 34);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(0,0,0);\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"  	width: 20px;\n"
""
                        "  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  	border: 1px solid;\n"
"  	border-color: grey;\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: right;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"  	width: 20px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:h"
                        "orizontal:hover {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  	border: 1px solid;\n"
"  	border-color: grey;\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: left;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"  	border: 1px transparent grey;\n"
"  	border-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
" 	background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	border: 1px transparent grey;\n"
"	border-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
" 	background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
" 	background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"	max-w"
                        "idth: 20px;\n"
"	background: rgb(0,0,0);\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"  	height: 20px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  	border: 1px solid;\n"
"  	border-color: grey;\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: bottom;\n"
"  	subcontrol-origin: "
                        "margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"  	height: 20px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  	border: 1px solid;\n"
"  	border-color: rgb(0,0,0);\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  	border: 1px solid;\n"
"  	border-color: grey;\n"
"	border-radius: 8px;\n"
"  	background: rgb(230, 126, 34);\n"
"  	height: 16px;\n"
"  	width: 16px;\n"
"  	subcontrol-position: top;\n"
"  	subcontrol-origin: margin;\n"
"}\n"
"	QScrollBar::handle:vertical {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:1, y2:"
                        "0, stop:0 rgba(255, 0, 0, 0), stop:0.7 rgba(255, 0, 0, 0), stop:0.71 rgb(230, 126, 34), stop:1 rgb(230, 126, 34));\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(0,0,0);\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(230, 126, 34);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(0,0,0);\n"
"	min-heigth: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"	border: 1px transparent grey;\n"
"	border-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
" 	background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"  	border: 1px transparent grey;\n"
"  	border-radius: 3px;\n"
"  	width: 6px;\n"
"  	height: 6px;\n"
" 	background: rgb(0,0,0);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  	background: none;\n"
"}\n"
"/*\n"
"Neon Style Sheet for QT Applications (QpushButton)\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 24/10/2020, 15:42.\n"
"Available a"
                        "t: https://github.com/GTRONICK/QSS/blob/master/NeonButtons.qss\n"
"*/\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #221c3d;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #FFFFFF;\n"
"	padding: 2px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #480fa3, stop:0.4 #480fa3, stop:0.5 #221c3d, stop:1 #221c3d);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #221c3d, stop:0.5 #221c3d, stop:0.6 #480fa3, stop:1 #480fa3);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #480fa3, stop:0.3 #480fa3, stop:0.7 #221c3d, stop:1 #221c3d);\n"
"    border-right-color: qlineargradient(spread:pad, x1:"
                        "0, y1:1, x2:0, y2:0, stop:0 #480fa3, stop:0.3 #480fa3, stop:0.7 #221c3d, stop:1 #221c3d);\n"
"	border-width: 2px;\n"
"    border-radius: 1px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #914dff, stop:0.4 #914dff, stop:0.5 #221c3d, stop:1 #221c3d);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #221c3d, stop:0.5 #221c3d, stop:0.6 #914dff, stop:1 #914dff);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #914dff, stop:0.3 #914dff, stop:0.7 #221c3d, stop:1 #221c3d);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #914dff, stop:0.3 #914dff, stop:0.7 #221c3d, stop:1 #221c3d);\n"
"	border-width: 2px;\n"
"    border-radius: 1px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_7 = QWidget(self.tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 891, 452))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.label_4 = QLabel(self.verticalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_search_main = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_search_main.setObjectName(u"lineEdit_search_main")

        self.verticalLayout_4.addWidget(self.lineEdit_search_main)

        self.label_5 = QLabel(self.verticalLayoutWidget_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkBox_google_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_google_main.setObjectName(u"checkBox_google_main")

        self.horizontalLayout_8.addWidget(self.checkBox_google_main)

        self.spinBox_google_main = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_google_main.setObjectName(u"spinBox_google_main")
        self.spinBox_google_main.setMaximum(999)

        self.horizontalLayout_8.addWidget(self.spinBox_google_main)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.checkBox_bing_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_bing_main.setObjectName(u"checkBox_bing_main")

        self.horizontalLayout_9.addWidget(self.checkBox_bing_main)

        self.spinBox_bing_main = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_bing_main.setObjectName(u"spinBox_bing_main")
        self.spinBox_bing_main.setMaximum(999)

        self.horizontalLayout_9.addWidget(self.spinBox_bing_main)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.label_7 = QLabel(self.verticalLayoutWidget_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.checkBox_savefile = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_savefile.setObjectName(u"checkBox_savefile")

        self.verticalLayout_4.addWidget(self.checkBox_savefile)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_path_to_file = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_path_to_file.setObjectName(u"lineEdit_path_to_file")

        self.horizontalLayout_11.addWidget(self.lineEdit_path_to_file)

        self.pushButton_path_directory_file_main = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_path_directory_file_main.setObjectName(u"pushButton_path_directory_file_main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_path_directory_file_main.sizePolicy().hasHeightForWidth())
        self.pushButton_path_directory_file_main.setSizePolicy(sizePolicy4)
        self.pushButton_path_directory_file_main.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_11.addWidget(self.pushButton_path_directory_file_main)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.line = QFrame(self.verticalLayoutWidget_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.verticalLayoutWidget_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.lineEdit_path_directory_img_main = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_path_directory_img_main.setObjectName(u"lineEdit_path_directory_img_main")

        self.horizontalLayout_12.addWidget(self.lineEdit_path_directory_img_main)

        self.pushButton_path_directory_img_main = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_path_directory_img_main.setObjectName(u"pushButton_path_directory_img_main")
        sizePolicy4.setHeightForWidth(self.pushButton_path_directory_img_main.sizePolicy().hasHeightForWidth())
        self.pushButton_path_directory_img_main.setSizePolicy(sizePolicy4)
        self.pushButton_path_directory_img_main.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_12.addWidget(self.pushButton_path_directory_img_main)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.line_3 = QFrame(self.verticalLayoutWidget_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.verticalLayoutWidget_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.checkBox_normalization_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_normalization_main.setObjectName(u"checkBox_normalization_main")

        self.horizontalLayout_4.addWidget(self.checkBox_normalization_main, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_4 = QFrame(self.verticalLayoutWidget_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label_9 = QLabel(self.verticalLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_deletedsave_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_deletedsave_main.setObjectName(u"checkBox_deletedsave_main")

        self.verticalLayout_6.addWidget(self.checkBox_deletedsave_main)

        self.checkBox_one_color_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_one_color_main.setObjectName(u"checkBox_one_color_main")

        self.verticalLayout_6.addWidget(self.checkBox_one_color_main)

        self.checkBox_small_images_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_small_images_main.setObjectName(u"checkBox_small_images_main")

        self.verticalLayout_6.addWidget(self.checkBox_small_images_main)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.spinBox_small_width_main = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_small_width_main.setObjectName(u"spinBox_small_width_main")
        self.spinBox_small_width_main.setMaximum(9999999)

        self.horizontalLayout_13.addWidget(self.spinBox_small_width_main)

        self.spinBox_small_heigth_main = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_small_heigth_main.setObjectName(u"spinBox_small_heigth_main")
        self.spinBox_small_heigth_main.setMaximum(9999999)

        self.horizontalLayout_13.addWidget(self.spinBox_small_heigth_main)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.checkBox_dublicates_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_dublicates_main.setObjectName(u"checkBox_dublicates_main")

        self.verticalLayout_6.addWidget(self.checkBox_dublicates_main)


        self.verticalLayout.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_2 = QFrame(self.verticalLayoutWidget_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_catalog_needed_main = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_catalog_needed_main.setObjectName(u"checkBox_catalog_needed_main")

        self.verticalLayout_7.addWidget(self.checkBox_catalog_needed_main)

        self.radioButton_catalog_size_auto_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_catalog_size_auto_main.setObjectName(u"radioButton_catalog_size_auto_main")

        self.verticalLayout_7.addWidget(self.radioButton_catalog_size_auto_main)

        self.radioButton_catalog_size_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_catalog_size_main.setObjectName(u"radioButton_catalog_size_main")

        self.verticalLayout_7.addWidget(self.radioButton_catalog_size_main)

        self.label_11 = QLabel(self.verticalLayoutWidget_7)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_sizes_main = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_sizes_main.setObjectName(u"lineEdit_sizes_main")

        self.verticalLayout_7.addWidget(self.lineEdit_sizes_main)

        self.radioButton_catalog_file_sizes_auto_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_catalog_file_sizes_auto_main.setObjectName(u"radioButton_catalog_file_sizes_auto_main")

        self.verticalLayout_7.addWidget(self.radioButton_catalog_file_sizes_auto_main)

        self.radioButton_catalog_file_sizes_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_catalog_file_sizes_main.setObjectName(u"radioButton_catalog_file_sizes_main")

        self.verticalLayout_7.addWidget(self.radioButton_catalog_file_sizes_main)

        self.label_12 = QLabel(self.verticalLayoutWidget_7)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_sizes_files_main = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_sizes_files_main.setObjectName(u"lineEdit_sizes_files_main")

        self.verticalLayout_7.addWidget(self.lineEdit_sizes_files_main)

        self.radioButton_tags_resnet_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_tags_resnet_main.setObjectName(u"radioButton_tags_resnet_main")

        self.verticalLayout_7.addWidget(self.radioButton_tags_resnet_main)

        self.radioButton_tags_mob_main = QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_tags_mob_main.setObjectName(u"radioButton_tags_mob_main")

        self.verticalLayout_7.addWidget(self.radioButton_tags_mob_main)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 10, 10)
        self.pushButton_start_main = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_start_main.setObjectName(u"pushButton_start_main")

        self.horizontalLayout_14.addWidget(self.pushButton_start_main)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_3 = QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 891, 441))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label_31 = QLabel(self.verticalLayoutWidget_3)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_search_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_search_2.setObjectName(u"lineEdit_search_2")

        self.verticalLayout_2.addWidget(self.lineEdit_search_2)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.checkBox_google_2 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_google_2.setObjectName(u"checkBox_google_2")

        self.horizontalLayout_2.addWidget(self.checkBox_google_2)

        self.spinBox_google_2 = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_google_2.setObjectName(u"spinBox_google_2")
        self.spinBox_google_2.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spinBox_google_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.checkBox_bing_2 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_bing_2.setObjectName(u"checkBox_bing_2")

        self.horizontalLayout_3.addWidget(self.checkBox_bing_2)

        self.spinBox_bing_2 = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_bing_2.setObjectName(u"spinBox_bing_2")
        self.spinBox_bing_2.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_bing_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 136))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_savefile_2 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_savefile_2.setObjectName(u"checkBox_savefile_2")

        self.verticalLayout_3.addWidget(self.checkBox_savefile_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_path_to_file_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_path_to_file_2.setObjectName(u"lineEdit_path_to_file_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_path_to_file_2)

        self.pushButton_path_directory_file_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_path_directory_file_2.setObjectName(u"pushButton_path_directory_file_2")
        sizePolicy4.setHeightForWidth(self.pushButton_path_directory_file_2.sizePolicy().hasHeightForWidth())
        self.pushButton_path_directory_file_2.setSizePolicy(sizePolicy4)
        self.pushButton_path_directory_file_2.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_path_directory_file_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_3.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_saveimgs_2 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_saveimgs_2.setObjectName(u"checkBox_saveimgs_2")

        self.verticalLayout_3.addWidget(self.checkBox_saveimgs_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_path_directory_img_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_path_directory_img_2.setObjectName(u"lineEdit_path_directory_img_2")

        self.horizontalLayout_10.addWidget(self.lineEdit_path_directory_img_2)

        self.pushButton_path_directory_img_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_path_directory_img_2.setObjectName(u"pushButton_path_directory_img_2")
        sizePolicy4.setHeightForWidth(self.pushButton_path_directory_img_2.sizePolicy().hasHeightForWidth())
        self.pushButton_path_directory_img_2.setSizePolicy(sizePolicy4)
        self.pushButton_path_directory_img_2.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_10.addWidget(self.pushButton_path_directory_img_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.pushButton_start_parsing = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_start_parsing.setObjectName(u"pushButton_start_parsing")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_start_parsing.sizePolicy().hasHeightForWidth())
        self.pushButton_start_parsing.setSizePolicy(sizePolicy6)

        self.verticalLayout_12.addWidget(self.pushButton_start_parsing)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget = QWidget(self.tab_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 81, 891, 374))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_14 = QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.checkBox_deletedsave_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_deletedsave_3.setObjectName(u"checkBox_deletedsave_3")

        self.verticalLayout_9.addWidget(self.checkBox_deletedsave_3)

        self.checkBox_one_color_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_one_color_3.setObjectName(u"checkBox_one_color_3")

        self.verticalLayout_9.addWidget(self.checkBox_one_color_3)

        self.checkBox_small_images_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_small_images_3.setObjectName(u"checkBox_small_images_3")

        self.verticalLayout_9.addWidget(self.checkBox_small_images_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.spinBox_small_width_3 = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_small_width_3.setObjectName(u"spinBox_small_width_3")
        self.spinBox_small_width_3.setMaximum(9999999)

        self.horizontalLayout_16.addWidget(self.spinBox_small_width_3)

        self.spinBox_small_heigth_3 = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_small_heigth_3.setObjectName(u"spinBox_small_heigth_3")
        self.spinBox_small_heigth_3.setMaximum(9999999)

        self.horizontalLayout_16.addWidget(self.spinBox_small_heigth_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.checkBox_dublicates_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_dublicates_3.setObjectName(u"checkBox_dublicates_3")

        self.verticalLayout_9.addWidget(self.checkBox_dublicates_3)

        self.pushButton_clear_set_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_clear_set_3.setObjectName(u"pushButton_clear_set_3")

        self.verticalLayout_9.addWidget(self.pushButton_clear_set_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_19 = QLabel(self.horizontalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_11.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_normalize_set = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_normalize_set.setObjectName(u"pushButton_normalize_set")

        self.verticalLayout_11.addWidget(self.pushButton_normalize_set)

        self.label_20 = QLabel(self.horizontalLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_11.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_uncatalog_set = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_uncatalog_set.setObjectName(u"pushButton_uncatalog_set")

        self.horizontalLayout_7.addWidget(self.pushButton_uncatalog_set)

        self.pushButton_uncatalog_set_recursive_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_uncatalog_set_recursive_2.setObjectName(u"pushButton_uncatalog_set_recursive_2")

        self.horizontalLayout_7.addWidget(self.pushButton_uncatalog_set_recursive_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_15 = QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.radioButton_catalog_size_auto_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_catalog_size_auto_3.setObjectName(u"radioButton_catalog_size_auto_3")

        self.verticalLayout_10.addWidget(self.radioButton_catalog_size_auto_3)

        self.radioButton_catalog_size_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_catalog_size_3.setObjectName(u"radioButton_catalog_size_3")

        self.verticalLayout_10.addWidget(self.radioButton_catalog_size_3)

        self.label_16 = QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_sizes_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_sizes_3.setObjectName(u"lineEdit_sizes_3")

        self.verticalLayout_10.addWidget(self.lineEdit_sizes_3)

        self.radioButton_catalog_file_sizes_auto_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_catalog_file_sizes_auto_3.setObjectName(u"radioButton_catalog_file_sizes_auto_3")

        self.verticalLayout_10.addWidget(self.radioButton_catalog_file_sizes_auto_3)

        self.radioButton_catalog_file_sizes_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_catalog_file_sizes_3.setObjectName(u"radioButton_catalog_file_sizes_3")

        self.verticalLayout_10.addWidget(self.radioButton_catalog_file_sizes_3)

        self.label_17 = QLabel(self.horizontalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_sizes_files_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_sizes_files_3.setObjectName(u"lineEdit_sizes_files_3")

        self.verticalLayout_10.addWidget(self.lineEdit_sizes_files_3)

        self.radioButton_tags_resnet_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_tags_resnet_3.setObjectName(u"radioButton_tags_resnet_3")

        self.verticalLayout_10.addWidget(self.radioButton_tags_resnet_3)

        self.radioButton_tags_mob_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_tags_mob_3.setObjectName(u"radioButton_tags_mob_3")

        self.verticalLayout_10.addWidget(self.radioButton_tags_mob_3)

        self.pushButton_catalog_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_catalog_3.setObjectName(u"pushButton_catalog_3")

        self.verticalLayout_10.addWidget(self.pushButton_catalog_3)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)

        self.verticalLayoutWidget = QWidget(self.tab_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 891, 68))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.lineEdit_path_directory_img_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_path_directory_img_3.setObjectName(u"lineEdit_path_directory_img_3")

        self.horizontalLayout_17.addWidget(self.lineEdit_path_directory_img_3)

        self.pushButton_path_directory_img_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_path_directory_img_3.setObjectName(u"pushButton_path_directory_img_3")
        sizePolicy4.setHeightForWidth(self.pushButton_path_directory_img_3.sizePolicy().hasHeightForWidth())
        self.pushButton_path_directory_img_3.setSizePolicy(sizePolicy4)
        self.pushButton_path_directory_img_3.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_17.addWidget(self.pushButton_path_directory_img_3)

        self.pushButton_directory_img_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_directory_img_3.setObjectName(u"pushButton_directory_img_3")
        sizePolicy4.setHeightForWidth(self.pushButton_directory_img_3.sizePolicy().hasHeightForWidth())
        self.pushButton_directory_img_3.setSizePolicy(sizePolicy4)
        self.pushButton_directory_img_3.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_17.addWidget(self.pushButton_directory_img_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.tabWidget.addTab(self.tab_3, "")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 180, 361, 111))
        self.label.setStyleSheet(u"background-color: white; color: black; font-size: 20px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.hide()

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ImagesScraper", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442", None))
        self.lineEdit_search_main.setText("")
        self.lineEdit_search_main.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\n"
"\n"
"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0456 \u0441\u0438\u0441\u0442\u0435\u043c\u0438 \u0442\u0430 \n"
"\u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u0442\u043e\u0440\u0456\u043d\u043e\u043a \u0434\u043b\u044f \u043e\u0431\u0440\u043e\u0431\u043a\u0438:", None))
        self.checkBox_google_main.setText(QCoreApplication.translate("Dialog", u"Google", None))
        self.checkBox_bing_main.setText(QCoreApplication.translate("Dialog", u"Bing", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
" \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0443 \n"
"\u0437 \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u043c\u0438 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f\u043c\u0438\n"
"\u0430\u0431\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0442\u0435 \u0432\u0456\u0434\u043c\u0456\u0442\u043a\u0443", None))
        self.checkBox_savefile.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u0442\u0438 \u0443 \u0444\u0430\u0439\u043b", None))
        self.pushButton_path_directory_file_main.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
" \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u0445 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.pushButton_path_directory_img_main.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0440\u043c\u0430\u043b\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f:", None))
        self.checkBox_normalization_main.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0431\u0430\u0436\u0430\u043d\u0456 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f\n"
"\u0434\u043b\u044f \u043e\u0447\u0438\u0449\u0435\u043d\u043d\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c\n"
"(\u044f\u043a\u0449\u043e \u043d\u0435\u043c\u0430\u0454 \u043d\u0435\u043e\u0431\u0445\u0456\u0434\u043d\u043e\u0441\u0442\u0456 - \u043d\u0435 \u043e\u0431\u0438\u0440\u0430\u0442\u0438)", None))
        self.checkBox_deletedsave_main.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0435\u043d\u0456 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0437\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0443 \u043f\u0430\u043f\u043a\u0443 deleted", None))
        self.checkBox_one_color_main.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u044c\u043e\u0440\u0443", None))
        self.checkBox_small_images_main.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043c\u0430\u043b\u043e\u0433\u043e \u0440\u043e\u0437\u043c\u0456\u0440\u0443\n"
"(\u0432\u043a\u0430\u0436\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440\u0438 \u0448\u0438\u0440\u0438\u043d\u0430 * \u0432\u0438\u0441\u043e\u0442\u0430)", None))
        self.checkBox_dublicates_main.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0434\u0443\u0431\u043b\u0456\u043a\u0430\u0442\u0438", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0437\u0430 \u044f\u043a\u0438\u043c \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u043e\u043c \n"
"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0441\u0435\u0442 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c\n"
"(\u0430\u0431\u043e \u0432\u0441\u0442\u0430\u043d\u043e\u0432\u0456\u0442\u044c \u043f\u0440\u0430\u043f\u043e\u0440\u0435\u0446\u044c)", None))
        self.checkBox_catalog_needed_main.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438", None))
        self.radioButton_catalog_size_auto_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e ", None))
        self.radioButton_catalog_size_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
"((200, 200), (300, 300)), ((500, 500), (700, 700))", None))
        self.radioButton_catalog_file_sizes_auto_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e", None))
        self.radioButton_catalog_file_sizes_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
"(10B, 12KB), (11MB, 1GB)", None))
        self.radioButton_tags_resnet_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 ResNet \u043c\u043e\u0434\u0435\u043b\u0456", None))
        self.radioButton_tags_mob_main.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 MobileNetV2 \u043c\u043e\u0434\u0435\u043b\u0456", None))
        self.pushButton_start_main.setText(QCoreApplication.translate("Dialog", u"\n"
"\u041f\u043e\u0447\u0430\u0442\u0438\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u041a\u043e\u0441\u043f\u043b\u0435\u043a\u0441\u043d\u0430 \u043e\u0431\u0440\u043e\u0431\u043a\u0430", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442", None))
        self.lineEdit_search_2.setText("")
        self.lineEdit_search_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\n"
"\n"
"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0456 \u0441\u0438\u0441\u0442\u0435\u043c\u0438 \u0442\u0430 \n"
"\u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u0442\u043e\u0440\u0456\u043d\u043e\u043a \u0434\u043b\u044f \u043e\u0431\u0440\u043e\u0431\u043a\u0438:", None))
        self.checkBox_google_2.setText(QCoreApplication.translate("Dialog", u"Google", None))
        self.checkBox_bing_2.setText(QCoreApplication.translate("Dialog", u"Bing", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
" \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0443 \n"
"\u0437 \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u043c\u0438 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f\u043c\u0438", None))
        self.checkBox_savefile_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u0442\u0438 \u0443 \u0444\u0430\u0439\u043b \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f", None))
        self.pushButton_path_directory_file_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c \u0437 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u044c", None))
        self.checkBox_saveimgs_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))
        self.pushButton_path_directory_img_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.pushButton_start_parsing.setText(QCoreApplication.translate("Dialog", u"\n"
"\u0417\u0430\u043f\u0443\u0441\u043a\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0417\u0431\u0456\u0440 \u0434\u0430\u043d\u0438\u0445", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0431\u0430\u0436\u0430\u043d\u0456 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f\n"
"\u0434\u043b\u044f \u043e\u0447\u0438\u0449\u0435\u043d\u043d\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.checkBox_deletedsave_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0435\u043d\u0456 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0437\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0443 \u043f\u0430\u043f\u043a\u0443 deleted", None))
        self.checkBox_one_color_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u044c\u043e\u0440\u0443", None))
        self.checkBox_small_images_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043c\u0430\u043b\u043e\u0433\u043e \u0440\u043e\u0437\u043c\u0456\u0440\u0443\n"
"(\u0432\u043a\u0430\u0436\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440\u0438 \u0448\u0438\u0440\u0438\u043d\u0430 * \u0432\u0438\u0441\u043e\u0442\u0430)", None))
        self.checkBox_dublicates_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0434\u0443\u0431\u043b\u0456\u043a\u0430\u0442\u0438", None))
        self.pushButton_clear_set_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438 \u0441\u0435\u0442 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0440\u043c\u0430\u043b\u0456\u0437\u0430\u0446\u0456\u044f \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.pushButton_normalize_set.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0440\u043c\u0430\u043b\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0441\u0435\u0442\n"
"\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043c\u043e\u0436\u043d\u0456 \u0444\u0443\u043d\u043a\u0446\u0456\u0457:", None))
        self.pushButton_uncatalog_set.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u0437\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u0457\n"
"\u043f\u0435\u0440\u0448\u043e\u0433\u043e \u0440\u0456\u0432\u043d\u044f", None))
        self.pushButton_uncatalog_set_recursive_2.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u0437\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u0457\n"
"\u0440\u0435\u043a\u0443\u0440\u0441\u0438\u0432\u043d\u043e", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0437\u0430 \u044f\u043a\u0438\u043c \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u043e\u043c \n"
"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0441\u0435\u0442 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.radioButton_catalog_size_auto_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e ", None))
        self.radioButton_catalog_size_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
"((200, 200), (300, 300)), ((500, 500), (700, 700))", None))
        self.radioButton_catalog_file_sizes_auto_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e", None))
        self.radioButton_catalog_file_sizes_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
"(10B, 12KB), (11MB, 1GB)", None))
        self.radioButton_tags_resnet_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 ResNet \u043c\u043e\u0434\u0435\u043b\u0456", None))
        self.radioButton_tags_mob_3.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 MobileNetV2 \u043c\u043e\u0434\u0435\u043b\u0456", None))
        self.pushButton_catalog_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0441\u0435\u0442\n"
"\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c", None))
        self.pushButton_path_directory_img_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.pushButton_directory_img_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u043d\u0443\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u0420\u043e\u0431\u043e\u0442\u0430 \u0437 \u0434\u0430\u043d\u0438\u043c\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0446\u0435\u0441...", None))
    # retranslateUi

