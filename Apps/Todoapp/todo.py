import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 300, 400)
        
        self.tasks = [] 
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit(self)
        self.add_button = QPushButton("Add Task", self)
        self.task_list = QListWidget
        
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.task_list = QListWidget(self)
        
        self.add_button.clicked.connect(self.add_task)
        
        self.setLayout(self.layout)
        
    def add_task(self):
        task_text = self.input_field.text()
        if task_text:
            self.tasks.append(task_text)
            self.task_list.addItem(task_text)
            self.input_field.clear()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
    