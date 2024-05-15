import os
import sys
import threading

from PySide6 import QtWidgets

from cataloging_img.imgs_cataloger import ImagesCataloger
from main_ui import Ui_Dialog
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

        self.parser = MainParser(None, None, None, None, None)
        self.imgs_scraper = MainScraper()
        self.imgs_cleaner = ImagesCleaner(None, None)
        self.imgs_normalizer = ImagesNormalizer(None, None, None, None)
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
            if not directory_path:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Вкажіть шлях для збереження файлу з посиланнями')
                error_dialog.exec()
                return

        driver_google_options = webdriver.ChromeOptions()
        driver_google_options.add_argument('--ignore-certificate-errors')
        driver_google_options.add_argument('--incognito')
        driver_google_options.add_argument('--headless')
        driver_google = webdriver.Chrome(options=driver_google_options)
        driver_bing = webdriver.Chrome(options=driver_google_options)
        self.parser = MainParser(query, driver_google, driver_bing, n_pages_google, n_pages_bing)

        path_to_save = self.lineEdit_path_directory_img_main.text()
        if not path_to_save:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Вкажіть шлях для збереження зображень')
            error_dialog.exec()
            return
        self.imgs_scraper = MainScraper()

        flag_delete = self.checkBox_deletedsave_main.isChecked()
        flag_one_color = self.checkBox_one_color_main.isChecked()
        flag_small = self.checkBox_small_images_main.isChecked()
        width = int(self.spinBox_small_width_main.text())
        height = int(self.spinBox_small_heigth_main.text())
        flag_duplicates = self.checkBox_dublicates_main.isChecked()
        os.makedirs(f'{path_to_save}/{query}', exist_ok=True)
        self.imgs_cleaner = ImagesCleaner(f'{path_to_save}/{query}', flag_delete)

        flag_catalog = self.checkBox_catalog_needed_main.isChecked()
        flag_catalog_size_auto = self.radioButton_catalog_size_auto_main.isChecked()
        flag_catalog_size_manual = self.radioButton_catalog_size_main.isChecked()
        sizes_manual = self.lineEdit_sizes_main.text()
        flag_catalog_size_file_auto = self.radioButton_catalog_file_sizes_auto_main.isChecked()
        flag_catalog_size_file_manual = self.radioButton_catalog_file_sizes_main.isChecked()
        sizes_file_manual = self.lineEdit_sizes_files_main.text()
        flag_catalog_tags_resnet = self.radioButton_tags_resnet_main.isChecked()
        flag_catalog_tags_mobilenet = self.radioButton_tags_mob_main.isChecked()
        if not flag_catalog and not flag_catalog_size_auto and not flag_catalog_size_manual and not flag_catalog_size_file_auto and not flag_catalog_size_file_manual:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Оберіть спосіб каталогізації')
            error_dialog.exec()
            return
        self.imgs_cataloger = ImagesCataloger(f'{path_to_save}/{query}')

        def start():
            try:
                self.tabWidget.setEnabled(False)
                self.pushButton_start_main.setText('Парсинг...')
                links = self.parser.parse(path_to_save=directory_path)
                self.pushButton_start_main.setText('Скачування зображень...')
                self.imgs_scraper.run(links, query, path_to_save)
                self.pushButton_start_main.setText('Очищення зображень...')
                self.imgs_cleaner.run(flag_one_color,
                                      flag_small, width, height,
                                      flag_duplicates,
                                      flag_duplicates, flag_duplicates, flag_duplicates)
                if not flag_catalog:
                    self.pushButton_start_main.setText('Каталогізація зображень...')
                    self.imgs_cataloger.start(flag_catalog_size_auto, flag_catalog_size_manual, sizes_manual,
                                              flag_catalog_size_file_auto, flag_catalog_size_file_manual, sizes_file_manual,
                                              flag_catalog_tags_resnet, flag_catalog_tags_mobilenet)
                self.pushButton_start_main.setText('Готово')
                self.tabWidget.setEnabled(True)
                self.pushButton_start_main.setText('Почати')
            except Exception as e:
                self.tabWidget.setEnabled(True)
                self.pushButton_start_main.setText('Почати')
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Помилка: {e}')
                error_dialog.exec()

        threading.Thread(target=start).start()


class Main:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QDialog()
        self.logic_ui = LogicUI(self.dialog)
        self.dialog.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    Main()


# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(window)
# window.show()
# sys.exit(app.exec_())