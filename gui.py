# -*- coding: utf-8 -*-
from myraflib import myEnv
from myraflib import myFit

from PyQt4 import QtGui
from PyQt4 import QtCore

from matplotlib.patches import Circle


class Gui():

    def __init__(self, verb=True):
        self.verb = verb
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)
        self.mfetc = myFit.etc(verb=self.verb)

    def show_are_you_sure(self, him, message):
        ret = False
        reply = QtGui.QMessageBox.question(him, 'Message',
            message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            ret = True
        else:
            ret = False

        return ret

    def show_dialog(self, him, message_type, head, text):
        ret = False
        if message_type == "critic":
            try:
                QtGui.QMessageBox.critical(him, (head), (text))
                ret = True
            except Exception as e:
                self.meetc.print_if(e)
        elif message_type == "info":
            try:
                QtGui.QMessageBox.information(him, (head), (text))
                ret = True
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def is_checked(self, check_dev):
        return check_dev.checkState() == QtCore.Qt.Checked

    def set_enabled(self, dev, stat):
        ret = False
        try:
            dev.setEnabled(stat)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def set_current_index_to_list(self, devlist, index):
        ret = False
        try:
            devlist.setCurrentRow(index)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_current_index_from_list(self, devlist):
        ret = [False, None]
        try:
            row = devlist.currentRow()
            ret = [True, row]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_file_list(self, him, file_type, check_fits=True):
        ret = [False, None]
        file_names = []
        try:
            fn = QtGui.QFileDialog.getOpenFileNames(him,
                "Select Data", "~", (file_type))
            for i in fn:
                if check_fits:
                    if self.mfetc.is_fits(str(i)):
                        file_names.append(str(i))
                else:
                    file_names.append(str(i))
            ret = [True, file_names]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_folder(self, him):
        ret = [False, None]
        try:
            hm = self.mefo.get_home_dir()
            if hm[0]:
                o_dir = hm[1]
            else:
                o_dir = "."
            out_dir = QtGui.QFileDialog.getExistingDirectory(him,
                'Select a directory to save.', o_dir)
            if not out_dir == "":
                ret = [True, out_dir]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_file(self, him, file_to_save, file_filter):
        ret = [False, None]
        try:
            hm = self.mefo.get_home_dir()
            if hm[0]:
                o_dir = hm[1]
            else:
                o_dir = "."
            out_file = QtGui.QFileDialog.getSaveFileName(him,
                'Save file', "%s/%s" % (o_dir, file_to_save),
                '%s (*.%s)' % (file_filter, file_filter))
            ret = [True, out_file]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_count_of_list(self, list_dev):
        ret = [False, None]
        try:
            cou = list_dev.count()
            ret = [True, cou]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_all_items_from_list(self, list_dev):
        ret = [False, None]
        try:
            itemsTextList = [str(list_dev.item(i).text())
            for i in range(list_dev.count())]
            ret = [True, itemsTextList]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_all_items_from_combo(self, combo_dev):

        ret = [False, None]
        try:
            itemsTextList = [combo_dev.itemText(i)
                for i in range(combo_dev.count())]
            ret = [True, itemsTextList]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def set_values_to_list(self, him, list_dev, items):
        ret = False
        all_items = self.get_all_items_from_list(list_dev)
        if all_items[0]:
            try:
                it = list_dev.count() - 1
                for i in items:
                    if not i in all_items[1]:
                        it = it + 1
                        item = QtGui.QListWidgetItem()
                        list_dev.addItem(item)
                        item = list_dev.item(it)
                        item.setText(QtGui.QApplication.translate("Form",
                        str(i), None, QtGui.QApplication.UnicodeUTF8))
                    else:
                        self.meetc.print_if("%s already exist. Skipping." % (i))
                ret = True
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def set_values_to_combo(self, him, combo_dev, items):
        ret = False
        all_items = self.get_all_items_from_combo(combo_dev)
        if all_items[0]:
            try:
                for i in items:
                    if not i in all_items[1]:
                        combo_dev.addItem(i)
                    else:
                        self.meetc.print_if("%s already exist. Skipping." % (i))
                ret = True
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def remove_values_from_list(self, list_dev):
        ret = False
        try:
            for i in list_dev.selectedItems():
                list_dev.takeItem(list_dev.row(i))
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_list_index_of_selected_items_from_list(self, list_dev):
        ret = [False, None]
        lst_of_indexes = []
        try:
            for i in list_dev.selectedItems():
                lst_of_indexes.append(list_dev.row(i))
            ret = [True, lst_of_indexes]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def unselect_all_list(self, list_dev):
        ret = False
        try:
            for i in range(list_dev.count()):
                list_dev.item(i).setSelected(False)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def select_given_range_in_list(self, list_dev, rang):
        ret = False
        try:
            if self.unselect_all_list(list_dev):
                for i in rang:
                    list_dev.item(i).setSelected(True)
                ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def remove_all_values_from_list(self, list_dev):
        ret = False
        try:
            for i in range(list_dev.count()):
                list_dev.takeItem(0)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def remove_all_values_from_combo(self, bombo_dev):
        ret = False
        try:
            for i in range(bombo_dev.count()):
                bombo_dev.removeItem(0)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_current_item_from_list(self, list_dev):
        ret = [False, None]
        try:
            item = list_dev.currentItem()
            if not item is None:
                item = item.text()
                ret = [True, str(item)]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_selected_items_from_list(self, list_dev):
        ret = [False, None]
        coors = []
        try:
            items = list_dev.selectedItems()
            if len(items) > 0:
                for i in items:
                    coors.append(i.text())
                ret = [True, coors]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_current_item_from_combo(self, combo_dev):
        ret = [False, None]
        try:
            item = combo_dev.currentText()
            ret = [True, str(item)]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def reload_list_with_new_items(self, him, list_dev, items):
        ret = False
        if self.remove_all_values_from_list(list_dev):
            self.set_values_to_list(him, list_dev, items)
            ret = True

        return ret

    def reload_combo_with_new_items(self, him, combo_dev, items):
        ret = False
        if self.remove_all_values_from_combo(combo_dev):
            self.set_values_to_combo(him, combo_dev, items)
            ret = True

        return ret

    def update_status_bar(self, him, text):
        ret = False
        try:
            him.ui.statusbar.showMessage(text)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def timestamp_checked(self, him, state):
        if state:
            him.ui.label_98.setText("Time Stamp")
            him.ui.label_100.setText("Seperator")
        else:
            him.ui.label_98.setText("Time OBS")
            him.ui.label_100.setText("Date OBS")

    def epoch_calculator(self, him, state):
        if state:
            him.ui.lineEdit_41.setEnabled(False)
            self.set_state(him.ui.checkBox_5, True)
        else:
            him.ui.lineEdit_41.setEnabled(True)
            self.set_state(him.ui.checkBox_5, False)

    def set_state(self, check_dev, state):
        check_dev.setChecked(state)

    def set_combo_current_text(self, com_dev, text):
        ret = False
        try:
            index = com_dev.findText(text, QtCore.Qt.MatchFixedString)
            if index >= 0:
                com_dev.setCurrentIndex(index)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def calc_percentage(self, current, whole):
        proc = int(100 * float(current) / float(whole))
        return proc

    def get_item_from_list(self, list_dev):
        ret = [False, None]
        try:
            item = list_dev.currentItem().text()
            ret = [True, str(item)]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_item_from_combo(self, combo_dev):
        ret = [False, None]
        try:
            item = combo_dev.currentText()
            ret = [True, str(item)]
        except Exception as e:
            self.meetc.print_if(e)
        return ret

    def display(self, file_name, disp_dev):
        ret = False
        try:
            if self.mfetc.is_fits(file_name):
                disp_dev.load(str(file_name))
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def draw_a_circle(self, disp_dev, x, y, radi, colour, label=""):
        circAnnulus = Circle((radi, radi), radi, edgecolor=colour,
            facecolor="none")
        disp_dev.canvas.fig.gca().add_artist(circAnnulus)
        circAnnulus.center = x, y
        disp_dev.canvas.fig.gca().annotate(str(label), xy=(x, y),
            xytext=(radi / 8, radi / 8), textcoords='offset points',
            color = "red", fontsize = radi / 4)
        disp_dev.canvas.draw()
