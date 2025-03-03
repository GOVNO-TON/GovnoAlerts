# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_filter_tab_add.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QTableView, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 660)
        MainWindow.setMinimumSize(QSize(845, 634))
        MainWindow.setMaximumSize(QSize(845, 660))
        font = QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"src/Components/assets/window_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setKerning(False)
        self.tabWidget.setFont(font1)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.Start_btn = QPushButton(self.tab_1)
        self.Start_btn.setObjectName(u"Start_btn")
        self.Start_btn.setGeometry(QRect(560, 510, 261, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setKerning(False)
        self.Start_btn.setFont(font2)
        self.server_connect_widget = QWidget(self.tab_1)
        self.server_connect_widget.setObjectName(u"server_connect_widget")
        self.server_connect_widget.setGeometry(QRect(580, 10, 241, 71))
        self.gridLayout_6 = QGridLayout(self.server_connect_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.server_ip_label = QLabel(self.server_connect_widget)
        self.server_ip_label.setObjectName(u"server_ip_label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(False)
        self.server_ip_label.setFont(font3)
        self.server_ip_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.server_ip_label, 2, 1, 1, 1)

        self.faq_server_link = QLabel(self.server_connect_widget)
        self.faq_server_link.setObjectName(u"faq_server_link")
        self.faq_server_link.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.faq_server_link, 1, 1, 1, 1)

        self.copy_ip_btn = QLabel(self.server_connect_widget)
        self.copy_ip_btn.setObjectName(u"copy_ip_btn")
        self.copy_ip_btn.setMaximumSize(QSize(30, 16777215))
        self.copy_ip_btn.setPixmap(QPixmap(u"src/Components/assets/copy.png"))

        self.gridLayout_6.addWidget(self.copy_ip_btn, 2, 2, 1, 1)

        self.donate_table_widget = QWidget(self.tab_1)
        self.donate_table_widget.setObjectName(u"donate_table_widget")
        self.donate_table_widget.setGeometry(QRect(10, 10, 541, 551))
        self.gridLayout_7 = QGridLayout(self.donate_table_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.donate_table = QTableView(self.donate_table_widget)
        self.donate_table.setObjectName(u"donate_table")
        self.donate_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.donate_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.donate_table.setAlternatingRowColors(False)
        self.donate_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.donate_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.donate_table.setTextElideMode(Qt.ElideMiddle)
        self.donate_table.setGridStyle(Qt.SolidLine)

        self.gridLayout_7.addWidget(self.donate_table, 1, 0, 1, 1)

        self.donate_table_label_faq = QLabel(self.donate_table_widget)
        self.donate_table_label_faq.setObjectName(u"donate_table_label_faq")
        self.donate_table_label_faq.setFont(font2)
        self.donate_table_label_faq.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.donate_table_label_faq, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.donate_table_widget.raise_()
        self.Start_btn.raise_()
        self.server_connect_widget.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setLayoutDirection(Qt.LeftToRight)
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(420, 30, 370, 221))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.test_msg_label = QLabel(self.widget)
        self.test_msg_label.setObjectName(u"test_msg_label")
        self.test_msg_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.test_msg_label)

        self.test_msg_textbox = QTextEdit(self.widget)
        self.test_msg_textbox.setObjectName(u"test_msg_textbox")
        self.test_msg_textbox.setMinimumSize(QSize(40, 100))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setKerning(False)
        self.test_msg_textbox.setFont(font4)

        self.verticalLayout_2.addWidget(self.test_msg_textbox)

        self.test_msg_textbox_button = QPushButton(self.widget)
        self.test_msg_textbox_button.setObjectName(u"test_msg_textbox_button")
        self.test_msg_textbox_button.setMinimumSize(QSize(352, 41))
        self.test_msg_textbox_button.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setKerning(False)
        self.test_msg_textbox_button.setFont(font5)
        self.test_msg_textbox_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.test_msg_textbox_button)

        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 371, 251))
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.change_lang_comboBox = QComboBox(self.widget_2)
        self.change_lang_comboBox.addItem("")
        self.change_lang_comboBox.addItem("")
        self.change_lang_comboBox.setObjectName(u"change_lang_comboBox")
        self.change_lang_comboBox.setEditable(False)

        self.gridLayout_4.addWidget(self.change_lang_comboBox, 1, 0, 1, 1)

        self.volume_slider = QSlider(self.widget_2)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximumSize(QSize(300, 22))
        self.volume_slider.setMaximum(400)
        self.volume_slider.setValue(0)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.volume_slider, 3, 0, 1, 1)

        self.speed_label = QLabel(self.widget_2)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setFont(font2)

        self.gridLayout_4.addWidget(self.speed_label, 4, 0, 1, 1)

        self.speed_slider = QSlider(self.widget_2)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setMaximumSize(QSize(300, 22))
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(200)
        self.speed_slider.setSingleStep(0)
        self.speed_slider.setPageStep(1)
        self.speed_slider.setValue(0)
        self.speed_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.speed_slider, 5, 0, 1, 1)

        self.change_lang_label = QLabel(self.widget_2)
        self.change_lang_label.setObjectName(u"change_lang_label")
        self.change_lang_label.setFont(font2)

        self.gridLayout_4.addWidget(self.change_lang_label, 0, 0, 1, 1)

        self.volume_label = QLabel(self.widget_2)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setFont(font2)

        self.gridLayout_4.addWidget(self.volume_label, 2, 0, 1, 1)

        self.voice_volume_label = QSpinBox(self.widget_2)
        self.voice_volume_label.setObjectName(u"voice_volume_label")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setKerning(False)
        self.voice_volume_label.setFont(font6)
        self.voice_volume_label.setMaximum(400)

        self.gridLayout_4.addWidget(self.voice_volume_label, 3, 1, 1, 1)

        self.voice_speed_label = QDoubleSpinBox(self.widget_2)
        self.voice_speed_label.setObjectName(u"voice_speed_label")
        self.voice_speed_label.setFont(font6)
        self.voice_speed_label.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.voice_speed_label.setMaximum(2.000000000000000)

        self.gridLayout_4.addWidget(self.voice_speed_label, 5, 1, 1, 1)

        self.widget_10 = QWidget(self.tab_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 280, 371, 131))
        self.widget_10.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.widget_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"margin: 0, 0, 4 ,-4 ")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 6)

        self.widget_17 = QWidget(self.widget_10)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout = QHBoxLayout(self.widget_17)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.len_change_spinBox = QSpinBox(self.widget_17)
        self.len_change_spinBox.setObjectName(u"len_change_spinBox")
        self.len_change_spinBox.setFont(font6)
        self.len_change_spinBox.setMaximum(99999)

        self.horizontalLayout.addWidget(self.len_change_spinBox)


        self.gridLayout_3.addWidget(self.widget_17, 1, 0, 1, 2)

        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 6)

        self.save_voice_settings_btn = QPushButton(self.tab_2)
        self.save_voice_settings_btn.setObjectName(u"save_voice_settings_btn")
        self.save_voice_settings_btn.setGeometry(QRect(20, 420, 361, 41))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_7 = QWidget(self.tab_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(20, 20, 274, 551))
        self.formLayout = QFormLayout(self.widget_7)
        self.formLayout.setObjectName(u"formLayout")
        self.shema_listbox = QListWidget(self.widget_7)
        __qlistwidgetitem = QListWidgetItem(self.shema_listbox)
        __qlistwidgetitem.setFlags(Qt.NoItemFlags);
        self.shema_listbox.setObjectName(u"shema_listbox")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setKerning(False)
        self.shema_listbox.setFont(font7)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.shema_listbox)

        self.shema_add_button = QPushButton(self.widget_7)
        self.shema_add_button.setObjectName(u"shema_add_button")
        self.shema_add_button.setMinimumSize(QSize(125, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.shema_add_button)

        self.shema_del_button = QPushButton(self.widget_7)
        self.shema_del_button.setObjectName(u"shema_del_button")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.shema_del_button)

        self.alert_settings_canvas = QWidget(self.tab_3)
        self.alert_settings_canvas.setObjectName(u"alert_settings_canvas")
        self.alert_settings_canvas.setEnabled(True)
        self.alert_settings_canvas.setGeometry(QRect(340, 20, 401, 551))
        self.widget_13 = QWidget(self.alert_settings_canvas)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setEnabled(True)
        self.widget_13.setGeometry(QRect(10, 30, 381, 71))
        self.verticalLayout_8 = QVBoxLayout(self.widget_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_20 = QLabel(self.widget_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_20)

        self.name_shema_textbox = QPlainTextEdit(self.widget_13)
        self.name_shema_textbox.setObjectName(u"name_shema_textbox")
        self.name_shema_textbox.setMaximumSize(QSize(600, 31))
        self.name_shema_textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.name_shema_textbox)

        self.widget_8 = QWidget(self.alert_settings_canvas)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 110, 401, 251))
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.text_duration_label = QLabel(self.widget_11)
        self.text_duration_label.setObjectName(u"text_duration_label")
        self.text_duration_label.setGeometry(QRect(9, 9, 341, 19))
        self.text_duration_label.setFont(font2)
        self.text_duration_slider = QSlider(self.widget_11)
        self.text_duration_slider.setObjectName(u"text_duration_slider")
        self.text_duration_slider.setGeometry(QRect(9, 34, 281, 22))
        self.text_duration_slider.setMaximum(999)
        self.text_duration_slider.setOrientation(Qt.Horizontal)
        self.text_duration_label_2 = QSpinBox(self.widget_11)
        self.text_duration_label_2.setObjectName(u"text_duration_label_2")
        self.text_duration_label_2.setGeometry(QRect(310, 30, 42, 22))
        self.text_duration_label_2.setMaximum(999)

        self.verticalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.volume_alert_label = QLabel(self.widget_12)
        self.volume_alert_label.setObjectName(u"volume_alert_label")
        self.volume_alert_label.setGeometry(QRect(9, 9, 341, 19))
        self.volume_alert_label.setFont(font2)
        self.volume_alert_slider = QSlider(self.widget_12)
        self.volume_alert_slider.setObjectName(u"volume_alert_slider")
        self.volume_alert_slider.setGeometry(QRect(9, 34, 281, 22))
        self.volume_alert_slider.setMaximum(400)
        self.volume_alert_slider.setValue(0)
        self.volume_alert_slider.setOrientation(Qt.Horizontal)
        self.volume_allert_counter_label = QSpinBox(self.widget_12)
        self.volume_allert_counter_label.setObjectName(u"volume_allert_counter_label")
        self.volume_allert_counter_label.setGeometry(QRect(310, 30, 42, 22))
        self.volume_allert_counter_label.setMaximum(400)

        self.verticalLayout_7.addWidget(self.widget_12)

        self.widget_15 = QWidget(self.widget_8)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_3 = QVBoxLayout(self.widget_15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.alert_min_trigger_price_box = QDoubleSpinBox(self.widget_15)
        self.alert_min_trigger_price_box.setObjectName(u"alert_min_trigger_price_box")
        self.alert_min_trigger_price_box.setDecimals(9)
        self.alert_min_trigger_price_box.setMaximum(1000000000000000043845843045076197354634047651840.000000000000000)
        self.alert_min_trigger_price_box.setSingleStep(0.000001000000000)

        self.verticalLayout_3.addWidget(self.alert_min_trigger_price_box)


        self.verticalLayout_7.addWidget(self.widget_15)

        self.widget_14 = QWidget(self.alert_settings_canvas)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(10, 350, 381, 71))
        self.gridLayout_2 = QGridLayout(self.widget_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.alert_gif_path = QLabel(self.widget_14)
        self.alert_gif_path.setObjectName(u"alert_gif_path")
        self.alert_gif_path.setFont(font2)

        self.gridLayout_2.addWidget(self.alert_gif_path, 0, 0, 1, 1)

        self.alert_gif_textbox = QPlainTextEdit(self.widget_14)
        self.alert_gif_textbox.setObjectName(u"alert_gif_textbox")
        self.alert_gif_textbox.setMaximumSize(QSize(600, 31))
        self.alert_gif_textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.alert_gif_textbox, 1, 0, 1, 1)

        self.search_file_gif_btn = QPushButton(self.widget_14)
        self.search_file_gif_btn.setObjectName(u"search_file_gif_btn")

        self.gridLayout_2.addWidget(self.search_file_gif_btn, 1, 1, 1, 1)

        self.widget_16 = QWidget(self.alert_settings_canvas)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(10, 420, 381, 71))
        self.gridLayout = QGridLayout(self.widget_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.allert_sound_path_label = QLabel(self.widget_16)
        self.allert_sound_path_label.setObjectName(u"allert_sound_path_label")
        self.allert_sound_path_label.setFont(font2)

        self.gridLayout.addWidget(self.allert_sound_path_label, 0, 0, 1, 1)

        self.allert_sound_path_textbox = QPlainTextEdit(self.widget_16)
        self.allert_sound_path_textbox.setObjectName(u"allert_sound_path_textbox")
        self.allert_sound_path_textbox.setMaximumSize(QSize(600, 31))
        self.allert_sound_path_textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.allert_sound_path_textbox, 1, 0, 1, 1)

        self.search_path_audio_btn = QPushButton(self.widget_16)
        self.search_path_audio_btn.setObjectName(u"search_path_audio_btn")

        self.gridLayout.addWidget(self.search_path_audio_btn, 1, 1, 1, 1)

        self.save_shema_button = QPushButton(self.alert_settings_canvas)
        self.save_shema_button.setObjectName(u"save_shema_button")
        self.save_shema_button.setGeometry(QRect(12, 510, 381, 31))
        self.checkBox = QCheckBox(self.alert_settings_canvas)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 111, 20))
        self.checkBox.setFont(font2)
        self.tabWidget.addTab(self.tab_3, "")
        self.alert_settings_canvas.raise_()
        self.widget_7.raise_()
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_3 = QWidget(self.tab_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(19, 29, 791, 481))
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(30, 20, 371, 131))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.wallet_api_key_label = QLabel(self.widget_4)
        self.wallet_api_key_label.setObjectName(u"wallet_api_key_label")
        self.wallet_api_key_label.setFont(font2)

        self.verticalLayout_4.addWidget(self.wallet_api_key_label)

        self.wallet_api_key_textbox = QTextEdit(self.widget_4)
        self.wallet_api_key_textbox.setObjectName(u"wallet_api_key_textbox")
        self.wallet_api_key_textbox.setFont(font1)
        self.wallet_api_key_textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.wallet_api_key_textbox.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.wallet_api_key_textbox.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_4.addWidget(self.wallet_api_key_textbox)

        self.wallet_api_key_button = QPushButton(self.widget_4)
        self.wallet_api_key_button.setObjectName(u"wallet_api_key_button")

        self.verticalLayout_4.addWidget(self.wallet_api_key_button)

        self.wallet_faq_label = QLabel(self.widget_4)
        self.wallet_faq_label.setObjectName(u"wallet_faq_label")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setUnderline(True)
        font8.setKerning(False)
        self.wallet_faq_label.setFont(font8)
        self.wallet_faq_label.setStyleSheet(u"color: blue")

        self.verticalLayout_4.addWidget(self.wallet_faq_label)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(30, 140, 371, 111))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.wallet_addr_label = QLabel(self.widget_5)
        self.wallet_addr_label.setObjectName(u"wallet_addr_label")
        self.wallet_addr_label.setFont(font2)

        self.verticalLayout_5.addWidget(self.wallet_addr_label)

        self.wallet_addr_textbox = QTextEdit(self.widget_5)
        self.wallet_addr_textbox.setObjectName(u"wallet_addr_textbox")
        self.wallet_addr_textbox.setFont(font1)
        self.wallet_addr_textbox.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.wallet_addr_textbox.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.wallet_addr_textbox.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.wallet_addr_textbox.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_5.addWidget(self.wallet_addr_textbox)

        self.wallet_addr_button = QPushButton(self.widget_5)
        self.wallet_addr_button.setObjectName(u"wallet_addr_button")

        self.verticalLayout_5.addWidget(self.wallet_addr_button)

        self.donate_qr = QLabel(self.widget_3)
        self.donate_qr.setObjectName(u"donate_qr")
        self.donate_qr.setGeometry(QRect(510, 200, 209, 209))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donate_qr.sizePolicy().hasHeightForWidth())
        self.donate_qr.setSizePolicy(sizePolicy)
        self.donate_qr.setPixmap(QPixmap(u"src/Components/assets/donate_qr.png"))
        self.donate_qr.setScaledContents(True)
        self.donate_desig_faq_label = QLabel(self.widget_3)
        self.donate_desig_faq_label.setObjectName(u"donate_desig_faq_label")
        self.donate_desig_faq_label.setGeometry(QRect(500, 150, 241, 31))
        self.donate_desig_faq_label.setFont(font2)
        self.donate_disig_wallet_label = QLabel(self.widget_3)
        self.donate_disig_wallet_label.setObjectName(u"donate_disig_wallet_label")
        self.donate_disig_wallet_label.setGeometry(QRect(460, 420, 321, 31))
        self.donate_disig_wallet_label.setFont(font4)
        self.donate_disig_wallet_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.widget_18 = QWidget(self.widget_3)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(520, -5, 221, 161))
        self.widget_18.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_8 = QGridLayout(self.widget_18)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, -1, -1, -1)
        self.widget_9 = QWidget(self.widget_18)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.govno_logo = QLabel(self.widget_9)
        self.govno_logo.setObjectName(u"govno_logo")
        self.govno_logo.setMaximumSize(QSize(58, 58))
        self.govno_logo.setPixmap(QPixmap(u"src/Components/assets/logo_govno.png"))
        self.govno_logo.setScaledContents(True)
        self.govno_logo.setMargin(0)

        self.horizontalLayout_2.addWidget(self.govno_logo)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        font9 = QFont()
        font9.setPointSize(28)
        font9.setBold(True)
        font9.setKerning(False)
        self.label_5.setFont(font9)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.gridLayout_8.addWidget(self.widget_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u"src/Components/assets/ton_logo_light_background.png"))
        self.label_10.setScaledContents(False)

        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.bad_words_widget = QWidget(self.tab)
        self.bad_words_widget.setObjectName(u"bad_words_widget")
        self.bad_words_widget.setGeometry(QRect(10, 10, 371, 541))
        self.verticalLayout_9 = QVBoxLayout(self.bad_words_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_19 = QWidget(self.bad_words_widget)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_9 = QGridLayout(self.widget_19)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.filter_comboBox = QComboBox(self.widget_19)
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.setObjectName(u"filter_comboBox")

        self.gridLayout_9.addWidget(self.filter_comboBox, 1, 1, 1, 1)

        self.filter_urls_checkbox_label = QLabel(self.widget_19)
        self.filter_urls_checkbox_label.setObjectName(u"filter_urls_checkbox_label")
        self.filter_urls_checkbox_label.setFont(font2)

        self.gridLayout_9.addWidget(self.filter_urls_checkbox_label, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_19)

        self.filter_settings_faq = QLabel(self.bad_words_widget)
        self.filter_settings_faq.setObjectName(u"filter_settings_faq")
        self.filter_settings_faq.setFont(font2)

        self.verticalLayout_9.addWidget(self.filter_settings_faq)

        self.filter_textEdit = QTextEdit(self.bad_words_widget)
        self.filter_textEdit.setObjectName(u"filter_textEdit")
        self.filter_textEdit.setMinimumSize(QSize(40, 100))
        self.filter_textEdit.setFont(font1)

        self.verticalLayout_9.addWidget(self.filter_textEdit)

        self.filter_save_btn = QPushButton(self.bad_words_widget)
        self.filter_save_btn.setObjectName(u"filter_save_btn")
        self.filter_save_btn.setMinimumSize(QSize(352, 40))
        self.filter_save_btn.setMaximumSize(QSize(353, 65))
        self.filter_save_btn.setFont(font5)

        self.verticalLayout_9.addWidget(self.filter_save_btn)

        self.test_filter_widget = QWidget(self.bad_words_widget)
        self.test_filter_widget.setObjectName(u"test_filter_widget")
        font10 = QFont()
        font10.setPointSize(6)
        font10.setKerning(False)
        self.test_filter_widget.setFont(font10)
        self.verticalLayout_10 = QVBoxLayout(self.test_filter_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.test_filter_user_label = QLabel(self.test_filter_widget)
        self.test_filter_user_label.setObjectName(u"test_filter_user_label")
        self.test_filter_user_label.setFont(font2)

        self.verticalLayout_10.addWidget(self.test_filter_user_label)

        self.test_filter_user_textedit = QTextEdit(self.test_filter_widget)
        self.test_filter_user_textedit.setObjectName(u"test_filter_user_textedit")
        self.test_filter_user_textedit.setMinimumSize(QSize(100, 100))
        self.test_filter_user_textedit.setFont(font1)

        self.verticalLayout_10.addWidget(self.test_filter_user_textedit)

        self.result_label = QLabel(self.test_filter_widget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setFont(font2)

        self.verticalLayout_10.addWidget(self.result_label)

        self.test_result_textEdit = QTextEdit(self.test_filter_widget)
        self.test_result_textEdit.setObjectName(u"test_result_textEdit")
        self.test_result_textEdit.setFont(font1)
        self.test_result_textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.test_result_textEdit)


        self.verticalLayout_9.addWidget(self.test_filter_widget)

        self.widget_20 = QWidget(self.tab)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(410, 10, 391, 531))
        self.verticalLayout_11 = QVBoxLayout(self.widget_20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.filter_faq = QLabel(self.widget_20)
        self.filter_faq.setObjectName(u"filter_faq")
        self.filter_faq.setFont(font2)
        self.filter_faq.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.filter_faq)

        self.filter_textBrowser = QTextEdit(self.widget_20)
        self.filter_textBrowser.setObjectName(u"filter_textBrowser")
        self.filter_textBrowser.setMinimumSize(QSize(0, 300))
        self.filter_textBrowser.setMaximumSize(QSize(373, 16777215))
        self.filter_textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)
        self.filter_textBrowser.setReadOnly(True)
        self.filter_textBrowser.setTabStopDistance(80)

        self.verticalLayout_11.addWidget(self.filter_textBrowser)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font11 = QFont()
        font11.setPointSize(9)
        font11.setBold(True)
        font11.setKerning(False)
        self.label_4.setFont(font11)

        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)

        self.telegram_link_1 = QLabel(self.frame)
        self.telegram_link_1.setObjectName(u"telegram_link_1")
        self.telegram_link_1.setFont(font11)
        self.telegram_link_1.setStyleSheet(u"color: blue")

        self.gridLayout_5.addWidget(self.telegram_link_1, 0, 2, 1, 1)

        self.telegram_link_2 = QLabel(self.frame)
        self.telegram_link_2.setObjectName(u"telegram_link_2")
        self.telegram_link_2.setFont(font11)
        self.telegram_link_2.setStyleSheet(u"color:blue;")

        self.gridLayout_5.addWidget(self.telegram_link_2, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.filter_comboBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GOVNOtion Alerts", None))
        self.Start_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.server_ip_label.setText(QCoreApplication.translate("MainWindow", u"http://127.0.0.1:5455", None))
        self.faq_server_link.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u0432\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.copy_ip_btn.setText("")
        self.donate_table_label_faq.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0414\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.test_msg_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u043e\u0437\u0432\u0443\u0447\u043a\u0438", None))
        self.test_msg_textbox_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0442\u0435\u0441\u0442\u043e\u0432\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.change_lang_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.change_lang_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))

        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.change_lang_label.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a \u043e\u0437\u0432\u0443\u0447\u043a\u0438", None))
        self.volume_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043ac. \u0434\u043b\u0438\u043d\u0430 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0431\u043e\u043b\u044c\u0448\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0443\u0442 \u043e\u0431\u0440\u0435\u0437\u0430\u043d\u044b", None))
        self.save_voice_settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041e\u0437\u0432\u0443\u0447\u043a\u0430", None))

        __sortingEnabled = self.shema_listbox.isSortingEnabled()
        self.shema_listbox.setSortingEnabled(False)
        ___qlistwidgetitem = self.shema_listbox.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.shema_listbox.setSortingEnabled(__sortingEnabled)

        self.shema_add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.shema_del_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(statustip)
        self.alert_settings_canvas.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.text_duration_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u0430(c\u0435\u043a.)", None))
        self.volume_alert_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
        self.alert_gif_path.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0433\u0438\u0444", None))
        self.search_file_gif_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.allert_sound_path_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0430\u0443\u0434\u0438\u043e", None))
        self.search_path_audio_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.save_shema_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b/\u0412\u044b\u043a\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.wallet_api_key_label.setText(QCoreApplication.translate("MainWindow", u"API KEY", None))
        self.wallet_api_key_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.wallet_faq_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0434\u0435 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0442\u043e\u043a\u0435\u043d?", None))
        self.wallet_addr_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430", None))
        self.wallet_addr_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.donate_qr.setText("")
        self.donate_desig_faq_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u0442\u044c  \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430", None))
        self.donate_disig_wallet_label.setText(QCoreApplication.translate("MainWindow", u"UQBn0pRJvGJHOio-sIIc-Txkj1AJjpOfOI7fGzvo2DmBglVd", None))
        self.govno_logo.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GOVNO", None))
        self.label_10.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430", None))
        self.filter_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u0434\u043e\u043d\u0430\u0442\u0430", None))
        self.filter_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0437\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438", None))
        self.filter_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0446\u0435\u043d\u0437\u0443\u0440\u044b", None))

        self.filter_urls_checkbox_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u0441\u0441\u044b\u043b\u043e\u043a:", None))
        self.filter_settings_faq.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0441\u043b\u043e\u0432", None))
        self.filter_save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.test_filter_user_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0442\u0435\u0441\u0442\u0430", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.filter_faq.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.filter_textBrowser.setMarkdown(QCoreApplication.translate("MainWindow", u"**\u0411\u0430\u0437\u043e\u0432\u044b\u0435 \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u044b \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438**\n"
"\n"
"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 \"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0444\u0438\u043b\u044c\u0442\u0440\u0430\" \u0443\u043a\u0430\u0436\u0435\u043c \u0441\u043b\u043e\u0432\u043e \u0438\u0434\u0438\u043e\u0442. \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0437\u0430\u043c\u0435\u043d\u0438\u0442 \u0435\u0433\u043e\n"
"\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: \u0438\u0434\u0438\u043e\u0442\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0432\u0435\u0434\u0435\u0448\u044c \u0441\u0435\u0431\u044f \u043a\u0430\u043a \u0438\u0434\u0438"
                        "\u043e\u0442\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b \u0432\u0435\u0434\u0435\u0448\u044c \u0441\u0435\u0431\u044f \u043a\u0430\u043a *****\n"
"\n"
"**\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0448\u0430\u0431\u043b\u043e\u043d\u0430\u043c\u0438**\n"
"\n"
"\u0412 \u043f\u043e\u043b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u043c\u043e\u0436\u043d\u043e \u0437\u0430\u0434\u0430\u0432\u0430\u0442\u044c \u043f\u0440\u0430\u0432\u0438\u043b\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432.\n"
"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0438\u0442 \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u044f \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443 \u0438 \u0437\u0430\u043c\u0435\u043d\u0438\u0442"
                        " \u0438\u0445.\n"
"\n"
"\u0420\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u2014 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442 \u0434\u043b\u044f \u0433\u0438\u0431\u043a\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430 \u0438 \u0437\u0430\u043c\u0435\u043d\u044b \u0442\u0435\u043a\u0441\u0442\u0430. \u041e\u043d\u0438\n"
"\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441, \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0439\u0441\u044f \u0441 re:\n"
"\n"
"**\u041f\u0440\u0438\u043c\u0435\u0440 1**: \u0417\u0430\u043c\u0435\u043d\u0430 \u043b\u044e\u0431\u043e\u0433\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u0430\n"
"\n"
"\u0421\u0438\u043c\u0432\u043e\u043b . \u0437\u0430\u043c\u0435\u043d\u044f\u0435\u0442 \u043b\u044e\u0431\u043e\u0439 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0439"
                        " \u0441\u0438\u043c\u0432\u043e\u043b. \u041d\u0430\u0439\u0434\u0435\u043c \u0441\u043b\u043e\u0432\u0430 \u0438\u0437 5 \u0431\u0443\u043a\u0432, \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0435\u0441\u044f\n"
"\u043d\u0430 \u0413 \u0438 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430 \u041a:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0433...\u043a\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0433\u043e\u0432\u043e\u0440\u0438\u0448\u044c \u0435\u0440\u0443\u043d\u0434\u0443, \u0433\u0440\u044f\u0437\u043a\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b \u0433\u043e\u0432\u043e\u0440\u0438\u0448\u044c \u0435\u0440\u0443\u043d\u0434\u0443, *****\n"
"\n"
"**\u041f\u0440\u0438\u043c\u0435\u0440 2**: \u0417"
                        "\u0430\u043c\u0435\u043d\u0430 \u0441\u043f\u0435\u0446. \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 ()[]-^|?!:*+$<>.\n"
"\n"
"\u0427\u0442\u043e\u0431\u044b \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043f\u0435\u0446 \u0441\u0438\u043c\u0432\u043e\u043b, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u044d\u043a\u0440\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \\: \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0437\u0430\u043c\u0435\u043d\u0438\u043c\n"
"\u0441\u0438\u043c\u0432\u043e\u043b \".\":\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\.\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u042d\u0442\u043e \u0442\u0435\u0441\u0442.\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u042d\u0442\u043e \u0442\u0435\u0441\u0442*****\n"
"\n"
"\u042d"
                        "\u043a\u0440\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0443\u0436\u043d\u043e \u043a\u0430\u0436\u0434\u044b\u0439 \u0441\u0438\u043c\u0432\u043e\u043b.\n"
"\n"
"**\u041f\u0440\u0438\u043c\u0435\u0440 3: **\u0417\u0430\u043c\u0435\u043d\u0430 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432\n"
"\n"
"\u0414\u043b\u044f \u0437\u0430\u043c\u0435\u043d\u044b \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 re:\\s\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\s\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0423\u0431\u0435\u0440\u0438 \u043f\u0440\u043e\u0431\u0435\u043b\u044b\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0423\u0431\u0435\u0440\u0438****\u043f\u0440\u043e\u0431\u0435\u043b\u044b\n"
"\n"
"**\u041f\u0440"
                        "\u0438\u043c\u0435\u0440 4**: \u041f\u0440\u043e\u0431\u0435\u043b\u044b \u0432 \u0441\u043b\u043e\u0432\u0430\u0445\n"
"\n"
"\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0441\u043b\u043e\u0432 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u0430\u043c\u0438 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u0435 \\s*:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438\\s*\u0434\\s*\u0438\\s*\u043e\\s*\u0442\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0438 \u0434 \u0438 \u043e \u0442\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b *****\n"
"\n"
"**\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u044b**\n"
"\n"
"\u041a\u0432\u0430\u0434"
                        "\u0440\u0430\u0442\u043d\u044b\u0435 \u0441\u043a\u043e\u0431\u043a\u0438 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438[\u0434\u043f]\u0438\u043e\u0442\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 \u0438\u043f\u0438\u043e\u0442 \u2014 \u043e\u0431\u0430 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: ***** \u0438\u043b\u0438 ***** \u2014 \u043e\u0431\u0430 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430\n"
"\n"
"**\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b \u0431\u0443\u043a\u0432**\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432"
                        "\u0430: re:[\u0430-\u044f]\u0438\u043e\u0442\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0411\u0438\u043e\u0442 \u0438\u043b\u0438 \u0444\u0438\u043e\u0442\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: ***** \u0438\u043b\u0438 *****\n"
"\n"
"**\u0418\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432**\n"
"\n"
"\u0421\u0438\u043c\u0432\u043e\u043b ^ \u0438\u0441\u043a\u043b\u044e\u0447\u0430\u0435\u0442 \u0431\u0443\u043a\u0432\u044b \u0438\u0437 \u043f\u043e\u0438\u0441\u043a\u0430:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438[^\u0434]\u0438\u043e\u0442\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 \u0438\u0441\u0438"
                        "\u043e\u0442\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 *****\n"
"\n"
"**\u041f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432**\n"
"\n"
"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 | \u0434\u043b\u044f \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0441\u043b\u043e\u0432:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438\u0434\u0438\u043e\u0442|\u0434\u0443\u0440\u0430\u043a\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0438\u0434\u0438\u043e\u0442 \u0438 \u0434\u0443\u0440\u0430\u043a\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c"
                        "\u0435: \u0422\u044b ***** \u0438 *****\n"
"\n"
"**\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b**\n"
"\n"
"\u0417\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430 \u0434\u043b\u044f \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u043b\u044e\u0431\u043e\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:[a-z]* (\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0441\u043b\u043e\u0432\u0430)\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u042f \u043a\u0443\u043f\u0438\u043b 10 apples\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u042f \u043a\u0443\u043f\u0438\u043b 10 *****\n"
"\n"
"**\u041f\u043e\u0438\u0441\u043a"
                        " \u0447\u0438\u0441\u0435\u043b**\n"
"\n"
"\\d \u0434\u043b\u044f \u043e\u0434\u043d\u043e\u0439 \u0446\u0438\u0444\u0440\u044b, \\d+ \u0434\u043b\u044f \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0438 \\d{\u0447\u0438\u0441\u043b\u043e} \u0434\u043b\u044f \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0442\u043e\u0447\u043d\u043e\u0433\u043e\n"
"\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u0447\u0438\u0441\u043b\u0435:\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\d{2} (\u0434\u0432\u0443\u0437\u043d\u0430\u0447\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430)\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043b 5 \u0438 99 \u043e\u0447\u043a\u043e\u0432\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d"
                        "\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043b 5 \u0438 **** \u043e\u0447\u043a\u043e\u0432\n"
"\n"
"**\u0424\u0438\u0433\u0443\u0440\u043d\u044b\u0435 \u0441\u043a\u043e\u0431\u043a\u0438 \u0434\u043b\u044f \u043f\u043e\u0432\u0442\u043e\u0440\u043e\u0432**\n"
"\n"
"    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\d{2,4} (\u0447\u0438\u0441\u043b\u0430 \u043e\u0442 2 \u0434\u043e 4 \u0446\u0438\u0444\u0440)\n"
"\n"
"    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u041a\u043e\u0434\u044b: 12, 345, 6789\n"
"\n"
"    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u041a\u043e\u0434\u044b: ****, ****, ****\n"
"\n"
"", None))
        self.filter_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0411\u0430\u0437\u043e\u0432\u044b\u0435 \u043f\u0440\u0438\u043d\u0446\u0438\u043f\u044b \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u043f\u0440\u0438"
                        "\u043c\u0435\u0440, \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 &quot;\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0444\u0438\u043b\u044c\u0442\u0440\u0430&quot; \u0443\u043a\u0430\u0436\u0435\u043c \u0441\u043b\u043e\u0432\u043e \u0438\u0434\u0438\u043e\u0442. \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0437\u0430\u043c\u0435\u043d\u0438\u0442 \u0435\u0433\u043e \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: \u0438\u0434\u0438\u043e\u0442</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0432\u0435\u0434\u0435\u0448\u044c \u0441\u0435\u0431\u044f \u043a\u0430\u043a \u0438\u0434\u0438\u043e\u0442</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b \u0432\u0435\u0434\u0435\u0448\u044c \u0441\u0435\u0431\u044f \u043a\u0430\u043a *****</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:12pt; font-weight:600;\">\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0448\u0430\u0431\u043b\u043e\u043d\u0430\u043c\u0438</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412 \u043f\u043e\u043b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u043c\u043e\u0436\u043d\u043e \u0437\u0430\u0434\u0430\u0432\u0430\u0442\u044c \u043f\u0440\u0430\u0432\u0438\u043b\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432. \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0438\u0442 \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u044f"
                        " \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443 \u0438 \u0437\u0430\u043c\u0435\u043d\u0438\u0442 \u0438\u0445.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u2014 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442 \u0434\u043b\u044f \u0433\u0438\u0431\u043a\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430 \u0438 \u0437\u0430\u043c\u0435\u043d\u044b \u0442\u0435\u043a\u0441\u0442\u0430. \u041e\u043d\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441, \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0439\u0441\u044f \u0441 re:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u041f\u0440\u0438\u043c\u0435\u0440 1</span>: \u0417\u0430\u043c\u0435\u043d\u0430 \u043b\u044e\u0431\u043e\u0433\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0438\u043c\u0432\u043e\u043b . \u0437\u0430\u043c\u0435\u043d\u044f\u0435\u0442 \u043b\u044e\u0431\u043e\u0439 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0439 \u0441\u0438\u043c\u0432\u043e\u043b. \u041d\u0430\u0439\u0434\u0435\u043c \u0441\u043b\u043e\u0432\u0430 \u0438\u0437 5 \u0431\u0443\u043a\u0432, \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430 \u0413 \u0438 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430"
                        " \u041a:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0433...\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0433\u043e\u0432\u043e\u0440\u0438\u0448\u044c \u0435\u0440\u0443\u043d\u0434\u0443, \u0433\u0440\u044f\u0437\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435"
                        ": \u0422\u044b \u0433\u043e\u0432\u043e\u0440\u0438\u0448\u044c \u0435\u0440\u0443\u043d\u0434\u0443, *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u041f\u0440\u0438\u043c\u0435\u0440 2</span>: \u0417\u0430\u043c\u0435\u043d\u0430 \u0441\u043f\u0435\u0446. \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 ()[]-^|?!:*+$&lt;&gt;.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0427\u0442\u043e\u0431\u044b \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043f\u0435\u0446 \u0441\u0438\u043c\u0432\u043e\u043b, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u044d\u043a\u0440\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438"
                        "\u0435 \\: \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u0437\u0430\u043c\u0435\u043d\u0438\u043c \u0441\u0438\u043c\u0432\u043e\u043b &quot;.&quot;:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u042d\u0442\u043e \u0442\u0435\u0441\u0442.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442"
                        " \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u042d\u0442\u043e \u0442\u0435\u0441\u0442*****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042d\u043a\u0440\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0443\u0436\u043d\u043e \u043a\u0430\u0436\u0434\u044b\u0439 \u0441\u0438\u043c\u0432\u043e\u043b.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u041f\u0440\u0438\u043c\u0435\u0440 3: </span>\u0417\u0430\u043c\u0435\u043d\u0430 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432"
                        "</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0437\u0430\u043c\u0435\u043d\u044b \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 re:\\s</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0423\u0431\u0435\u0440\u0438 \u043f\u0440\u043e\u0431\u0435\u043b\u044b</p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0423\u0431\u0435\u0440\u0438****\u043f\u0440\u043e\u0431\u0435\u043b\u044b</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u041f\u0440\u0438\u043c\u0435\u0440 4</span>: \u041f\u0440\u043e\u0431\u0435\u043b\u044b \u0432 \u0441\u043b\u043e\u0432\u0430\u0445</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0441\u043b\u043e\u0432 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u0430"
                        "\u043c\u0438 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u0435 \\s*:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438\\s*\u0434\\s*\u0438\\s*\u043e\\s*\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0438 \u0434 \u0438 \u043e \u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437"
                        "\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u044b</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u0441\u043a\u043e\u0431\u043a\u0438 \u0434\u043b\u044f \u0432\u044b\u0431\u043e"
                        "\u0440\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438[\u0434\u043f]\u0438\u043e\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 \u0438\u043f\u0438\u043e\u0442 \u2014 \u043e\u0431\u0430 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420"
                        "\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: ***** \u0438\u043b\u0438 ***** \u2014 \u043e\u0431\u0430 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b \u0431\u0443\u043a\u0432</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435"
                        " \u0441\u043b\u043e\u0432\u0430: re:[\u0430-\u044f]\u0438\u043e\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0411\u0438\u043e\u0442 \u0438\u043b\u0438 \u0444\u0438\u043e\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: ***** \u0438\u043b\u0438 *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0418\u0441\u043a\u043b"
                        "\u044e\u0447\u0435\u043d\u0438\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0438\u043c\u0432\u043e\u043b ^ \u0438\u0441\u043a\u043b\u044e\u0447\u0430\u0435\u0442 \u0431\u0443\u043a\u0432\u044b \u0438\u0437 \u043f\u043e\u0438\u0441\u043a\u0430:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438[^\u0434]\u0438\u043e\u0442</p>"
                        "\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 \u0438\u0441\u0438\u043e\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0418\u0434\u0438\u043e\u0442 \u0438\u043b\u0438 *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u041f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d"
                        "\u0438\u0435 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 | \u0434\u043b\u044f \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0441\u043b\u043e\u0432:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\u0438\u0434\u0438\u043e\u0442|\u0434"
                        "\u0443\u0440\u0430\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0422\u044b \u0438\u0434\u0438\u043e\u0442 \u0438 \u0434\u0443\u0440\u0430\u043a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0422\u044b ***** \u0438 *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d"
                        "\u044b\u0435 \u0441\u0438\u043c\u0432\u043e\u043b\u044b</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430 \u0434\u043b\u044f \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u043b\u044e\u0431\u043e\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b"
                        "\u043e\u0432\u0430: re:[a-z]* (\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0441\u043b\u043e\u0432\u0430)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u042f \u043a\u0443\u043f\u0438\u043b 10 apples</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u042f \u043a\u0443\u043f\u0438\u043b 10 *****</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt"
                        "; font-weight:600;\">\u041f\u043e\u0438\u0441\u043a \u0447\u0438\u0441\u0435\u043b</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\\d \u0434\u043b\u044f \u043e\u0434\u043d\u043e\u0439 \u0446\u0438\u0444\u0440\u044b, \\d+ \u0434\u043b\u044f \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0438 \\d{\u0447\u0438\u0441\u043b\u043e} \u0434\u043b\u044f \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0442\u043e\u0447\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u0447\u0438\u0441\u043b\u0435:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\d{2} (\u0434\u0432\u0443\u0437\u043d\u0430\u0447\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043b 5 \u0438 99 \u043e\u0447\u043a\u043e\u0432</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u0417\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043b 5 \u0438 **** \u043e\u0447\u043a\u043e"
                        "\u0432</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u0424\u0438\u0433\u0443\u0440\u043d\u044b\u0435 \u0441\u043a\u043e\u0431\u043a\u0438 \u0434\u043b\u044f \u043f\u043e\u0432\u0442\u043e\u0440\u043e\u0432</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0424\u0438\u043b\u044c\u0442\u0440\u0443\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430: re:\\d{2,4} (\u0447\u0438\u0441\u043b\u0430 \u043e\u0442 2 \u0434\u043e 4 \u0446\u0438\u0444\u0440)</p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435: \u041a\u043e\u0434\u044b: 12, 345, 6789</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0430 \u0441\u0442\u0440\u0438\u043c\u0435: \u041a\u043e\u0434\u044b: ****, ****, ****</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u043e \u0441\u0438\u043b\u0430\u043c\u0438 ", None))
        self.telegram_link_1.setText(QCoreApplication.translate("MainWindow", u"@LanArch1", None))
        self.telegram_link_2.setText(QCoreApplication.translate("MainWindow", u"@cathome", None))
    # retranslateUi

