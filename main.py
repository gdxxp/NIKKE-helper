import sys
import time
import pygetwindow
import threading
import auto_task

from ui import Ui_Form
from dialog import Ui_Dialog

from PySide6 import QtWidgets, QtCore

auto_task_list = [True, True, True, True, False, False, False]


class TaskThread(QtCore.QThread):

    def __init__(self, task_number, parent=None):
        super().__init__(parent)
        self.task_number = task_number
        self.start_time = None

    def run(self):
        if self.task_number == 8:
            auto_task.continuous_click()
        else:
            self.start_time = time.time()  # 记录任务开始时间
            if self.task_number == 1:
                auto_task.gain_rewards()
            elif self.task_number == 2:
                while True:
                    auto_task.recruit()
                    time.sleep(1)
            elif self.task_number == 3:
                auto_task.simulation_room()
            elif self.task_number == 4:
                auto_task.auto_consult()
            elif self.task_number == 5:
                auto_task.auto_arena()
            elif self.task_number == 6:
                auto_task.union_battle()
            elif self.task_number == 7:
                while True:
                    auto_task.auto_all(auto_task_list)
                    time.sleep(1)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton1.clicked.connect(lambda: self.run_task(1, "收米"))
        self.ui.pushButton2.clicked.connect(lambda: self.run_task(2, "连续单抽"))
        self.ui.pushButton3.clicked.connect(lambda: self.run_task(3, "模拟室"))
        self.ui.pushButton4.clicked.connect(lambda: self.run_task(4, "自动咨询"))
        self.ui.pushButton5.clicked.connect(lambda: self.run_task(5, "竞技场"))
        self.ui.pushButton6.clicked.connect(lambda: self.run_task(6, "联盟战"))
        self.ui.pushButton7.clicked.connect(lambda: self.run_task(7, "一键摆烂"))
        self.ui.stopButton.clicked.connect(self.stop_task)
        self.ui.initButton.clicked.connect(self.correct_window)
        self.ui.toolButton.clicked.connect(self.auto_all_settings)
        self.ui.checkBox.stateChanged.connect(lambda state=self.ui.checkBox.isChecked(): self.continuous_click(state))

        self.ui.horizontalSlider.valueChanged.connect(self.change_accuracy)
        self.ui.horizontalSlider_2.valueChanged.connect(self.change_interval)

        self.ui.label_2.setText("精确度：0.8")
        self.ui.label_3.setText("操作时间间隔：2.5s")

        self.current_task = None
        self.timer = None
        self.accuracy = 8
        self.interval = 25

        self.click_thread = TaskThread(8)
        self.current_thread = None
        self.task1_thread = TaskThread(1)
        self.task2_thread = TaskThread(2)
        self.task3_thread = TaskThread(3)
        self.task4_thread = TaskThread(4)
        self.task5_thread = TaskThread(5)
        self.task6_thread = TaskThread(6)
        self.task7_thread = TaskThread(7)

    def run_task(self, task_number, task_name):
        if self.current_thread:
            self.stop_task()
        self.current_task = task_name
        self.current_thread = getattr(self, f"task{task_number}_thread")
        self.current_thread.start()
        self.start_timer()

    def stop_task(self):
        if self.current_thread:
            self.current_thread.terminate()
        self.stop_timer()

    def start_timer(self):
        self.timer = threading.Timer(1, self.update_time)
        self.timer.start()

    def stop_timer(self):
        if self.timer is not None:
            self.timer.cancel()

    def update_time(self):
        if self.current_thread and self.current_thread.start_time is not None:
            elapsed_time = time.time() - self.current_thread.start_time
            elapsed_time_str = QtCore.QTime(0, 0, 0).addSecs(int(elapsed_time)).toString("hh:mm:ss")
            self.ui.label.setText(f"{self.current_task}: {elapsed_time_str}")
        self.start_timer()

    def change_accuracy(self):
        self.accuracy = self.ui.horizontalSlider.value()
        self.ui.label_2.setText(f"精确度：{self.accuracy / 10}")
        auto_task.change_accuracy(self.accuracy / 10)

    def change_interval(self):
        self.interval = self.ui.horizontalSlider_2.value()
        self.ui.label_3.setText(f"操作时间间隔：{self.interval / 10}s")
        auto_task.change_interval(self.interval / 10)

    def continuous_click(self, state: bool):
        if state:
            self.click_thread.start()
        else:
            if self.click_thread:
                self.click_thread.terminate()

    @staticmethod
    def correct_window():
        window_list = pygetwindow.getWindowsWithTitle('NIKKE')
        if window_list:
            print(window_list)
            window_list[1].resizeTo(1037, 811)

    @staticmethod
    def auto_all_settings():
        dialog = Dialog()
        dialog.exec()


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBox_0.setChecked(auto_task_list[0])
        self.ui.checkBox_1.setChecked(auto_task_list[1])
        self.ui.checkBox_2.setChecked(auto_task_list[2])
        self.ui.checkBox_3.setChecked(auto_task_list[3])
        self.ui.checkBox_4.setChecked(auto_task_list[4])
        self.ui.checkBox_5.setChecked(auto_task_list[5])
        self.ui.checkBox_6.setChecked(auto_task_list[6])

        self.ui.checkBox_0.stateChanged.connect(lambda state, index=0: self.auto_task_change(index))
        self.ui.checkBox_1.stateChanged.connect(lambda state, index=1: self.auto_task_change(index))
        self.ui.checkBox_2.stateChanged.connect(lambda state, index=2: self.auto_task_change(index))
        self.ui.checkBox_3.stateChanged.connect(lambda state, index=3: self.auto_task_change(index))
        self.ui.checkBox_4.stateChanged.connect(lambda state, index=4: self.auto_task_change(index))
        self.ui.checkBox_5.stateChanged.connect(lambda state, index=5: self.auto_task_change(index))
        self.ui.checkBox_6.stateChanged.connect(lambda state, index=6: self.auto_task_change(index))

    def auto_task_change(self, index):
        auto_task_list[index] = not auto_task_list[index]
        check_change = getattr(self.ui, f"checkBox_{index}")
        check_change.setChecked(auto_task_list[index])
        print(auto_task_list)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
