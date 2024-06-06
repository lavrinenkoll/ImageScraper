import os
import threading

from PySide6 import QtWidgets

from cataloging_img.imgs_cataloger import ImagesCataloger
from ui.main_ui import Ui_Dialog
from parsers.main_parser import MainParser
from process_img.img_normalizer import ImagesNormalizer
from process_img.imgs_cleaner import ImagesCleaner
from scrapers_img.main_scraper import MainScraper
from selenium import webdriver


class LogicUI(Ui_Dialog):
    def __init__(self, dialog):
        super().__init__()
        self.setupUi(dialog)
        self.pushButton_start_main.clicked.connect(self.on_start_main)
        self.pushButton_path_directory_file_main.clicked.connect(lambda: self.file_dialog(self.lineEdit_path_to_file))
        self.pushButton_path_directory_img_main.clicked.connect(lambda: self.file_dialog(self.lineEdit_path_directory_img_main))

        self.pushButton_start_parsing.clicked.connect(self.on_search_2)
        self.pushButton_path_directory_img_2.clicked.connect(lambda: self.file_dialog(self.lineEdit_path_directory_img_2))
        self.pushButton_path_directory_file_2.clicked.connect(lambda: self.file_dialog(self.lineEdit_path_to_file_2))

        self.pushButton_clear_set_3.clicked.connect(self.on_clean_3)
        self.pushButton_path_directory_img_3.clicked.connect(lambda: self.file_dialog(self.lineEdit_path_directory_img_3))
        self.pushButton_directory_img_3.clicked.connect(lambda: self.open_explorer(self.lineEdit_path_directory_img_3.text()))

        self.pushButton_normalize_set.clicked.connect(self.on_normalize_3)
        self.pushButton_catalog_3.clicked.connect(self.on_catalog_3)
        self.pushButton_uncatalog_set.clicked.connect(self.on_uncatalog_3)
        self.pushButton_uncatalog_set_recursive_2.clicked.connect(self.on_uncatalog_recursive_3)

        self.parser = MainParser(None, None, None, None, None)
        self.imgs_scraper = MainScraper()
        self.imgs_cleaner = ImagesCleaner(None, None)
        self.imgs_normalizer = ImagesNormalizer()
        self.imgs_cataloger = ImagesCataloger(None)

    def on_start_main(self):
        query = self.lineEdit_search_main.text()
        google_needed = self.checkBox_google_main.isChecked()
        n_pages_google = int(self.spinBox_google_main.text())
        bing_needed = self.checkBox_bing_main.isChecked()
        n_pages_bing = int(self.spinBox_bing_main.text())
        if not query:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Введіть запит')
            error_dialog.exec()
            return
        if not google_needed and not bing_needed or n_pages_google == 0 and n_pages_bing == 0:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть хоча б один пошуковик та вкажіть кількість сторінок для пошуку')
            error_dialog.exec()
            return
        n_pages_google = 0 if not google_needed else n_pages_google
        n_pages_bing = 0 if not bing_needed else n_pages_bing

        save_links = self.checkBox_savefile.isChecked()
        directory_path = None
        if not save_links:
            directory_path = self.lineEdit_path_to_file.text()
            directory_path_valid = os.path.isdir(directory_path)
            if not directory_path or not directory_path_valid or not os.access(directory_path, os.W_OK):
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Вкажіть шлях для збереження файлу з посиланнями')
                error_dialog.exec()
                return

        path_to_save = self.lineEdit_path_directory_img_main.text()
        path_to_save_valid = os.path.isdir(path_to_save)
        if not path_to_save or not path_to_save_valid or not os.access(path_to_save, os.W_OK):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях для збереження зображень')
            error_dialog.exec()
            return

        flag_normalize = self.checkBox_normalization_main.isChecked()

        flag_delete = self.checkBox_deletedsave_main.isChecked()
        flag_one_color = self.checkBox_one_color_main.isChecked()
        flag_small = self.checkBox_small_images_main.isChecked()
        width = int(self.spinBox_small_width_main.text())
        height = int(self.spinBox_small_heigth_main.text())
        flag_duplicates = self.checkBox_dublicates_main.isChecked()
        os.makedirs(f'{path_to_save}/{query}', exist_ok=True)


        flag_catalog = self.checkBox_catalog_needed_main.isChecked()
        flag_catalog_size_auto = self.radioButton_catalog_size_auto_main.isChecked()
        flag_catalog_size_manual = self.radioButton_catalog_size_main.isChecked()
        sizes_manual = self.lineEdit_sizes_main.text()
        if flag_catalog_size_manual:
            try:
                sizes_manual = self.imgs_cataloger.str_to_resolutions(sizes_manual)
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка, введіть розміри в правильному форматі: {e}')
                error_dialog.exec()
                return
        flag_catalog_size_file_auto = self.radioButton_catalog_file_sizes_auto_main.isChecked()
        flag_catalog_size_file_manual = self.radioButton_catalog_file_sizes_main.isChecked()
        sizes_file_manual = self.lineEdit_sizes_files_main.text()
        if flag_catalog_size_file_manual:
            try:
                sizes_file_manual = self.imgs_cataloger.str_to_file_sizes(sizes_file_manual)
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка, введіть розміри в правильному форматі: {e}')
                error_dialog.exec()
                return
        flag_catalog_tags_resnet = self.radioButton_tags_resnet_main.isChecked()
        flag_catalog_tags_mobilenet = self.radioButton_tags_mob_main.isChecked()
        if not flag_catalog and not flag_catalog_size_auto and not flag_catalog_size_manual and not flag_catalog_size_file_auto and not flag_catalog_size_file_manual\
                and not flag_catalog_tags_resnet and not flag_catalog_tags_mobilenet:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть спосіб каталогізації')
            error_dialog.exec()
            return


        self.tabWidget.setEnabled(False)
        label = self.label
        label.show()

        label.setText('Підготовка...')
        try:
            driver_google_options = webdriver.ChromeOptions()
            driver_google_options.add_argument('--ignore-certificate-errors')
            driver_google_options.add_argument('--incognito')
            driver_google_options.add_argument('--headless')
            driver_google = webdriver.Chrome(options=driver_google_options)
            driver_bing = webdriver.Chrome(options=driver_google_options)
            self.parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
            self.imgs_scraper = MainScraper()
            self.imgs_cleaner = ImagesCleaner(f'{path_to_save}/{query}', flag_delete)
            self.imgs_cataloger = ImagesCataloger(f'{path_to_save}/{query}')
        except Exception as e:
            label.hide()
            self.tabWidget.setEnabled(True)
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(f'Помилка: {e}')
            error_dialog.exec()
            return

        def start():
            try:
                self.label.setText('Парсинг...')
                links = self.parser.parse(path_to_save=directory_path)
                if directory_path:
                    self.open_explorer(directory_path)
                label.setText('Скачування зображень...')
                self.imgs_scraper.run(links, query, path_to_save)
                self.open_explorer(path_to_save)
                if flag_normalize:
                    label.setText('Нормалізація зображень...')
                    self.imgs_normalizer.normalize_images(f'{path_to_save}/{query}')
                label.setText('Очищення зображень...')
                self.imgs_cleaner.run(flag_one_color,
                                      flag_small, width, height,
                                      flag_duplicates,
                                      flag_duplicates, flag_duplicates, flag_duplicates)
                if not flag_catalog:
                    label.setText('Каталогізація зображень...')
                    self.imgs_cataloger.start(flag_catalog_size_manual, sizes_manual, flag_catalog_size_auto,
                                                flag_catalog_size_file_manual, sizes_file_manual, flag_catalog_size_file_auto,
                                                flag_catalog_tags_resnet, flag_catalog_tags_mobilenet)
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    @staticmethod
    def file_dialog(label):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        label.setText(directory)

    @staticmethod
    def open_explorer(directory):
        if directory:
            directory = directory[0] if isinstance(directory, list) else directory
            os.startfile(directory)

    def on_search_2(self):
        query = self.lineEdit_search_2.text()
        google_needed = self.checkBox_google_2.isChecked()
        n_pages_google = int(self.spinBox_google_2.text())
        bing_needed = self.checkBox_bing_2.isChecked()
        n_pages_bing = int(self.spinBox_bing_2.text())
        if not query:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Введіть запит')
            error_dialog.exec()
            return
        if not google_needed and not bing_needed or n_pages_google == 0 and n_pages_bing == 0:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть хоча б один пошуковик та вкажіть кількість сторінок для пошуку')
            error_dialog.exec()
            return
        n_pages_google = 0 if not google_needed else n_pages_google
        n_pages_bing = 0 if not bing_needed else n_pages_bing

        save_links = self.checkBox_savefile_2.isChecked()
        directory_path = None
        if not save_links:
            directory_path = self.lineEdit_path_to_file_2.text()
            directory_path_valid = os.path.isdir(directory_path)
            if not directory_path or not directory_path_valid or not os.access(directory_path, os.W_OK):
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Вкажіть шлях для збереження файлу з посиланнями')
                error_dialog.exec()
                return

        save_img = self.checkBox_saveimgs_2.isChecked()
        if save_links and save_img:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть хоча б один спосіб збереження інформації')
            error_dialog.exec()
            return

        path_to_save = None
        if not save_img:
            path_to_save = self.lineEdit_path_directory_img_2.text()
            path_to_save_valid = os.path.isdir(path_to_save)
            if not path_to_save or not path_to_save_valid or not os.access(path_to_save, os.W_OK):
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Вкажіть шлях для збереження зображень')
                error_dialog.exec()
                return

        label = self.label
        self.tabWidget.setEnabled(False)
        label.show()
        label.setText('Підготовка...')
        driver_google_options = webdriver.ChromeOptions()
        driver_google_options.add_argument('--ignore-certificate-errors')
        driver_google_options.add_argument('--incognito')
        driver_google_options.add_argument('--headless')
        driver_google = webdriver.Chrome(options=driver_google_options)
        driver_bing = webdriver.Chrome(options=driver_google_options)

        self.parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)
        self.imgs_scraper = MainScraper()

        def start():
            try:
                label.setText('Парсинг...')
                links = self.parser.parse(path_to_save=directory_path)
                if directory_path:
                    self.open_explorer(directory_path)
                if not save_img:
                    label.setText('Скачування зображень...')
                    self.imgs_scraper.run(links, query, path_to_save)
                    self.open_explorer(path_to_save)
                label.setText('Готово')
                self.tabWidget.setEnabled(True)
                label.hide()
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    def on_clean_3(self):
        dir = self.lineEdit_path_directory_img_3.text()
        if not dir or not os.path.exists(dir):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях до папки')
            error_dialog.exec()
            return

        flag_one_color = self.checkBox_one_color_3.isChecked()
        flag_small = self.checkBox_small_images_3.isChecked()
        width = int(self.spinBox_small_width_3.text())
        height = int(self.spinBox_small_heigth_3.text())
        flag_duplicates = self.checkBox_dublicates_3.isChecked()
        flag_delete = self.checkBox_deletedsave_3.isChecked()


        label = self.label
        label.show()
        self.tabWidget.setEnabled(False)
        label.setText('Підготовка...')
        self.imgs_cleaner = ImagesCleaner(dir, flag_delete)

        def start():
            try:
                label.setText('Очищення зображень...')
                self.imgs_cleaner.run(flag_one_color, flag_small, width, height, flag_duplicates, flag_duplicates,
                                      flag_duplicates, flag_duplicates)
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    def on_normalize_3(self):
        dir = self.lineEdit_path_directory_img_3.text()
        if not dir or not os.path.exists(dir):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях до папки')
            error_dialog.exec()
            return

        label = self.label
        label.show()
        self.tabWidget.setEnabled(False)
        label.setText('Підготовка...')
        self.imgs_normalizer = ImagesNormalizer()

        def start():
            try:
                label.setText('Нормалізація зображень...')
                self.imgs_normalizer.normalize_images(dir)
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    def on_catalog_3(self):
        dir = self.lineEdit_path_directory_img_3.text()
        if not dir or not os.path.exists(dir):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях до папки')
            error_dialog.exec()
            return

        flag_catalog_size_auto = self.radioButton_catalog_size_auto_3.isChecked()
        flag_catalog_size_manual = self.radioButton_catalog_size_3.isChecked()
        sizes_manual = self.lineEdit_sizes_3.text()
        if flag_catalog_size_manual:
            try:
                sizes_manual = self.imgs_cataloger.str_to_resolutions(sizes_manual)
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка, введіть розміри в правильному форматі: {e}')
                error_dialog.exec()
                return
        flag_catalog_size_file_auto = self.radioButton_catalog_file_sizes_auto_3.isChecked()
        flag_catalog_size_file_manual = self.radioButton_catalog_file_sizes_3.isChecked()
        sizes_file_manual = self.lineEdit_sizes_files_3.text()
        if flag_catalog_size_file_manual:
            try:
                sizes_file_manual = self.imgs_cataloger.str_to_file_sizes(sizes_file_manual)
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка, введіть розміри в правильному форматі: {e}')
                error_dialog.exec()
                return
        flag_catalog_tags_resnet = self.radioButton_tags_resnet_3.isChecked()
        flag_catalog_tags_mobilenet = self.radioButton_tags_mob_3.isChecked()
        if not flag_catalog_size_auto and not flag_catalog_size_manual and not flag_catalog_size_file_auto and not flag_catalog_size_file_manual\
                and not flag_catalog_tags_resnet and not flag_catalog_tags_mobilenet:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть спосіб каталогізації')
            error_dialog.exec()
            return

        label = self.label
        label.show()
        self.tabWidget.setEnabled(False)
        label.setText('Підготовка...')
        self.imgs_cataloger = ImagesCataloger(dir)

        def start():
            try:
                label.setText('Каталогізація зображень...')
                self.imgs_cataloger.start(flag_catalog_size_manual, sizes_manual, flag_catalog_size_auto,
                                          flag_catalog_size_file_manual, sizes_file_manual, flag_catalog_size_file_auto,
                                          flag_catalog_tags_resnet, flag_catalog_tags_mobilenet)
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    def on_uncatalog_3(self):
        dir = self.lineEdit_path_directory_img_3.text()
        if not dir or not os.path.exists(dir):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях до папки')
            error_dialog.exec()
            return

        label = self.label
        label.show()
        self.tabWidget.setEnabled(False)
        label.setText('Підготовка...')
        self.imgs_cataloger = ImagesCataloger(dir)

        def start():
            try:
                label.setText('Видалення каталогів...')
                self.imgs_cataloger.extract_images_from_folders()
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()

    def on_uncatalog_recursive_3(self):
        dir = self.lineEdit_path_directory_img_3.text()
        if not dir or not os.path.exists(dir):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях до папки')
            error_dialog.exec()
            return

        label = self.label
        label.show()
        self.tabWidget.setEnabled(False)
        label.setText('Підготовка...')
        self.imgs_cataloger = ImagesCataloger(dir)

        def start():
            try:
                label.setText('Видалення каталогів...')
                self.imgs_cataloger.extract_images_from_folders_recursive()
                label.setText('Готово')
                label.hide()
                self.tabWidget.setEnabled(True)
            except Exception as e:
                label.hide()
                self.tabWidget.setEnabled(True)
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()
