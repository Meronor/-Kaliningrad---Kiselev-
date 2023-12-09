import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QTableWidget" name="tableWidget"/>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Add</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
temp_dia = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>487</width>
    <height>203</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="add">
   <property name="geometry">
    <rect>
     <x>300</x>
     <y>160</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Add</string>
   </property>
  </widget>
  <widget class="QPushButton" name="back">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>160</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Back</string>
   </property>
  </widget>
  <widget class="QLabel" name="Name">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>30</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Name</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Name_ed">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>50</y>
     <width>81</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLineEdit" name="Sort_ed">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>50</y>
     <width>81</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Sort">
   <property name="geometry">
    <rect>
     <x>160</x>
     <y>30</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Sort</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Roasting_ed">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>50</y>
     <width>81</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Roasting">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>30</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Roasting</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Grains_ed">
   <property name="geometry">
    <rect>
     <x>350</x>
     <y>50</y>
     <width>111</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Grains">
   <property name="geometry">
    <rect>
     <x>390</x>
     <y>30</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Grains</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Description_ed">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>110</y>
     <width>281</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Description">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>90</y>
     <width>61</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Description</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Cost_ed">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>110</y>
     <width>61</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Cost">
   <property name="geometry">
    <rect>
     <x>360</x>
     <y>90</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Сost</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="Volume_ed">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>110</y>
     <width>61</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="Volume">
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>90</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Volume</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        que = "SELECT * FROM data"
        result = cur.execute(que).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.pushButton.clicked.connect(self.addevent_wind)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['Name', 'Sort', 'Roasting', 'Grains', 'Description', 'Сost', 'Volume'])

    def addevent_wind(self):
        dlg = AddeventWind(self)
        dlg.exec()


class AddeventWind(QDialog):
    def __init__(self, main):
        super().__init__()
        self.main = main
        f = io.StringIO(temp_dia)
        uic.loadUi(f, self)
        self.add.clicked.connect(self.add_coffee)
        self.back.clicked.connect(self.backk)

    def backk(self):
        self.close()

    def add_coffee(self):
        if self.Name_ed.text() in get_names():
            with sqlite3.connect("coffee.sqlite") as con:
                cur = con.cursor()
                cur.execute(
                    f'UPDATE data SET sort = "{self.Sort_ed.text()}", medium = "{self.Roasting_ed.text()}"'
                    f', zern = "{self.Grains_ed.text()}", describtion = "{self.Description_ed.text()}", cost = '
                    f'"{self.Cost_ed.text()}", V = "{self.Volume_ed.text()}" WHERE name = "{self.Name_ed.text()}"')
                self.close()
        else:
            with sqlite3.connect("coffee.sqlite") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO data (name, sort, medium, zern, describtion, cost, V) VALUES"
                            f" ('{self.Name_ed.text()}', '{self.Sort_ed.text()}', '{self.Roasting_ed.text()}', "
                            f"'{self.Grains_ed.text()}', "
                            f"'{self.Description_ed.text()}', '{self.Cost_ed.text()}', '{self.Volume_ed.text()}')")
                self.close()
        self.main.con = sqlite3.connect("coffee.sqlite")
        cur = self.main.con.cursor()
        que = "SELECT * FROM data"
        result = cur.execute(que).fetchall()
        self.main.tableWidget.setRowCount(len(result))
        self.main.tableWidget.setColumnCount(len(result[0]))
        self.main.pushButton.clicked.connect(self.main.addevent_wind)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.main.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.main.tableWidget.setHorizontalHeaderLabels(
            ['Name', 'Sort', 'Roasting', 'Grains', 'Description', 'Сost', 'Volume'])


def get_names():
    try:
        with sqlite3.connect("coffee.sqlite") as con:
            cur = con.cursor()
            return list(map(lambda x: x[0], cur.execute(f"SELECT name FROM data").fetchall()))
    except Exception as s:
        print('email')
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
