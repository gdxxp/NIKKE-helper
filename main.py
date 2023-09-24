import sys
import time
import pygetwindow
import threading
import auto_task

from ui import Ui_Form

from PySide6 import QtWidgets, QtCore


class TaskThread(QtCore.QThread):

    def __init__(self, task_number, parent=None):
        super().__init__(parent)
        self.task_number = task_number
        self.start_time = None

    def run(self):
        self.start_time = time.time()  # 记录任务开始时间
        if self.task_number == 1:
            while True:
                auto_task.gain_rewards()
                time.sleep(1)
        elif self.task_number == 2:
            while True:
                auto_task.recruit()
                time.sleep(1)
        elif self.task_number == 3:
            auto_task.simulation_room()
        elif self.task_number == 4:
            while True:
                auto_task.auto_consult()
                time.sleep(1)
        elif self.task_number == 5:
            while True:
                auto_task.auto_arena()
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
        self.ui.stopButton.clicked.connect(self.stop_task)
        self.ui.initButton.clicked.connect(self.correct_window)

        self.ui.horizontalSlider.valueChanged.connect(self.change_accuracy)
        self.ui.horizontalSlider_2.valueChanged.connect(self.change_interval)

        self.ui.label_2.setText("精确度：0.8")
        self.ui.label_3.setText("操作时间间隔：2.5s")

        self.current_task = None
        self.timer = None
        self.accuracy = 8
        self.interval = 25

        self.current_thread = None
        self.task1_thread = TaskThread(1)
        self.task2_thread = TaskThread(2)
        self.task3_thread = TaskThread(3)
        self.task4_thread = TaskThread(4)
        self.task5_thread = TaskThread(5)

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

    @staticmethod
    def correct_window():
        window_list = pygetwindow.getWindowsWithTitle('NIKKE')
        if window_list:
            print(window_list)
            window_list[1].resizeTo(1037, 811)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
