# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled6.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        Dialog.resize(903, 453)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 901, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_7 = QWidget(self.tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 891, 425))
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

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

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

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

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
        self.pushButton_start_main = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_start_main.setObjectName(u"pushButton_start_main")

        self.horizontalLayout_14.addWidget(self.pushButton_start_main)

        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget_5 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 0, 891, 331))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(self.horizontalLayoutWidget_5)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.spinBox = QSpinBox(self.horizontalLayoutWidget_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.spinBox_2 = QSpinBox(self.horizontalLayoutWidget_5)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setMinimumSize(QSize(444, 136))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_6.addWidget(self.lineEdit_3)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(75, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy7)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.button_stop = QPushButton(Dialog)
        self.button_stop.setGeometry(QRect(0, 0, Dialog.width(), Dialog.height() // 2))
        self.button_stop.setText('Зупинити')
        self.button_stop.hide()

        self.label = QLabel(Dialog)
        self.label.setGeometry(0, 0, Dialog.width(), Dialog.height())
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("background-color: white; color: black; font-size: 20px;")
        self.label.hide()

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ImagesScraper", None))
        self.label_4.setText(QCoreApplication.translate("Dialog",
                                                        u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442",
                                                        None))
        self.lineEdit_search_main.setText("")
        self.lineEdit_search_main.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                                u"\u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442",
                                                                                None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\n"
                                                                  "\n"
                                                                  "\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0456 \u0441\u0438\u0441\u0442\u0435\u043c\u0438 \u0442\u0430 \n"
                                                                  "\u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u0442\u043e\u0440\u0456\u043d\u043e\u043a \u0434\u043b\u044f \u043e\u0431\u0440\u043e\u0431\u043a\u0438:",
                                                        None))
        self.checkBox_google_main.setText(QCoreApplication.translate("Dialog", u"Google", None))
        self.checkBox_bing_main.setText(QCoreApplication.translate("Dialog", u"Bing", None))
        self.label_7.setText(QCoreApplication.translate("Dialog",
                                                        u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
                                                        " \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0443 \n"
                                                        "\u0437 \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u043c\u0438 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f\u043c\u0438\n"
                                                        "\u0430\u0431\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0442\u0435 \u0432\u0456\u0434\u043c\u0456\u0442\u043a\u0443",
                                                        None))
        self.checkBox_savefile.setText(QCoreApplication.translate("Dialog",
                                                                  u"\u041d\u0435 \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u0442\u0438 \u0443 \u0444\u0430\u0439\u043b",
                                                                  None))
        self.pushButton_path_directory_file_main.setText(
            QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.label_8.setText(QCoreApplication.translate("Dialog",
                                                        u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
                                                        " \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u0445 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c",
                                                        None))
        self.pushButton_path_directory_img_main.setText(
            QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.label_6.setText(QCoreApplication.translate("Dialog",
                                                        u"\u041d\u043e\u0440\u043c\u0430\u043b\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f:",
                                                        None))
        self.checkBox_normalization_main.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog",
                                                        u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0431\u0430\u0436\u0430\u043d\u0456 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f\n"
                                                        "\u0434\u043b\u044f \u043e\u0447\u0438\u0449\u0435\u043d\u043d\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c\n"
                                                        "(\u044f\u043a\u0449\u043e \u043d\u0435\u043c\u0430\u0454 \u043d\u0435\u043e\u0431\u0445\u0456\u0434\u043d\u043e\u0441\u0442\u0456 - \u043d\u0435 \u043e\u0431\u0438\u0440\u0430\u0442\u0438)",
                                                        None))
        self.checkBox_deletedsave_main.setText(QCoreApplication.translate("Dialog",
                                                                          u"\u0412\u0438\u0434\u0430\u043b\u0435\u043d\u0456 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0437\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0443 \u043f\u0430\u043f\u043a\u0443 deleted",
                                                                          None))
        self.checkBox_one_color_main.setText(QCoreApplication.translate("Dialog",
                                                                        u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u044c\u043e\u0440\u0443",
                                                                        None))
        self.checkBox_small_images_main.setText(QCoreApplication.translate("Dialog",
                                                                           u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u043c\u0430\u043b\u043e\u0433\u043e \u0440\u043e\u0437\u043c\u0456\u0440\u0443\n"
                                                                           "(\u0432\u043a\u0430\u0436\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440\u0438 \u0448\u0438\u0440\u0438\u043d\u0430 * \u0432\u0438\u0441\u043e\u0442\u0430)",
                                                                           None))
        self.checkBox_dublicates_main.setText(QCoreApplication.translate("Dialog",
                                                                         u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0434\u0443\u0431\u043b\u0456\u043a\u0430\u0442\u0438",
                                                                         None))
        self.label_10.setText(QCoreApplication.translate("Dialog",
                                                         u"\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u0437\u0430 \u044f\u043a\u0438\u043c \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u043e\u043c \n"
                                                         "\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0441\u0435\u0442 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c\n"
                                                         "(\u0430\u0431\u043e \u0432\u0441\u0442\u0430\u043d\u043e\u0432\u0456\u0442\u044c \u043f\u0440\u0430\u043f\u043e\u0440\u0435\u0446\u044c)",
                                                         None))
        self.checkBox_catalog_needed_main.setText(QCoreApplication.translate("Dialog",
                                                                             u"\u041d\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0443\u0432\u0430\u0442\u0438",
                                                                             None))
        self.radioButton_catalog_size_auto_main.setText(QCoreApplication.translate("Dialog",
                                                                                   u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e ",
                                                                                   None))
        self.radioButton_catalog_size_main.setText(QCoreApplication.translate("Dialog",
                                                                              u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f",
                                                                              None))
        self.label_11.setText(QCoreApplication.translate("Dialog",
                                                         u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
                                                         "((200, 200), (300, 300)), ((500, 500), (700, 700))", None))
        self.radioButton_catalog_file_sizes_auto_main.setText(QCoreApplication.translate("Dialog",
                                                                                         u"\u0417\u0430 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e",
                                                                                         None))
        self.radioButton_catalog_file_sizes_main.setText(QCoreApplication.translate("Dialog",
                                                                                    u"\u0417\u0430 \u0432\u043a\u0430\u0437\u0430\u043d\u0438\u043c\u0438 \u0440\u043e\u0437\u043c\u0456\u0440\u0430\u043c\u0438 \u0444\u0430\u0439\u043b\u0443",
                                                                                    None))
        self.label_12.setText(QCoreApplication.translate("Dialog",
                                                         u"\u041f\u0440\u0438\u043a\u043b\u0430\u0434 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044f: \n"
                                                         "(10B, 12KB), (11MB, 1GB)", None))
        self.radioButton_tags_resnet_main.setText(QCoreApplication.translate("Dialog",
                                                                             u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 ResNet \u043c\u043e\u0434\u0435\u043b\u0456",
                                                                             None))
        self.radioButton_tags_mob_main.setText(QCoreApplication.translate("Dialog",
                                                                          u"\u0417\u0430 \u0442\u0435\u0433\u0430\u043c\u0438 MobileNetV2 \u043c\u043e\u0434\u0435\u043b\u0456",
                                                                          None))
        self.pushButton_start_main.setText(
            QCoreApplication.translate("Dialog", u"\u041f\u043e\u0447\u0430\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog",
                                                                                               u"\u041a\u043e\u0441\u043f\u043b\u0435\u043a\u0441\u043d\u0430 \u043e\u0431\u0440\u043e\u0431\u043a\u0430",
                                                                                               None))
        self.label.setText(QCoreApplication.translate("Dialog",
                                                      u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442",
                                                      None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                    u"\u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0438\u0439 \u0437\u0430\u043f\u0438\u0442",
                                                                    None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\n"
                                                                  "\n"
                                                                  "\u041e\u0431\u0435\u0440\u0456\u0442\u044c \u043f\u043e\u0448\u0443\u043a\u043e\u0432\u0456 \u0441\u0438\u0441\u0442\u0435\u043c\u0438 \u0442\u0430 \n"
                                                                  "\u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0441\u0442\u043e\u0440\u0456\u043d\u043e\u043a \u0434\u043b\u044f \u043e\u0431\u0440\u043e\u0431\u043a\u0438:",
                                                        None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Google", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Bing", None))
        self.label_3.setText(QCoreApplication.translate("Dialog",
                                                        u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e \u0434\u043b\u044f \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u043d\u043d\u044f\n"
                                                        " \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0443 \n"
                                                        "\u0437 \u043e\u0442\u0440\u0438\u043c\u0430\u043d\u0438\u043c\u0438 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u043d\u044f\u043c\u0438",
                                                        None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u043b\u044f\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog",
                                                                                                 u"\u0417\u0431\u0456\u0440 \u043f\u043e\u0441\u0438\u043b\u0430\u043d\u044c",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog",
                                                                                                 u"\u0417\u0431\u0456\u0440 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog",
                                                                                                 u"\u041e\u0447\u0438\u0449\u0435\u043d\u043d\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog",
                                                                                                 u"\u041d\u043e\u0440\u043c\u0430\u043b\u0456\u0437\u0430\u0446\u0456\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c",
                                                                                                 None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Dialog",
                                                                                                 u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0456\u0437\u0430\u0446\u0456\u044f \u0441\u0435\u0442\u0443 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044c",
                                                                                                 None))
    # retranslateUi

