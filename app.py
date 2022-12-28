from PyQt5.QtWidgets import *
import sys
from orm.Product import Product
import psycopg2

################# blok obiavlenia #############

class Window(QMainWindow):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("E-SHOP GUI App")
        self.resize(600,600)
        
        widget=QWidget()
        self.setCentralWidget(widget)
        
        layout=QGridLayout()
        widget.setLayout(layout)
        
        toolBar = QToolBar("Main")
        self.addToolBar(toolBar)
        
        catalogMenu= QAction("Catalog", self)
        catalogMenu.triggered.connect(self.onCatalog)
        
        toolBar.addAction(catalogMenu)
        
        bagMenu= QAction("Bag", self)
        bagMenu.triggered.connect(self.onBag)

        toolBar.addAction(bagMenu)

    def onCatalog(self):
        products = Product.findAll()
        rows = len(products)
        table = QTableWidget(rows,2)
        
        for ri in range(rows):
            table.setItem(ri, 0, QTableWidgetItem(products[ri].name))
            
        self.layout.addWidget(table, 0, 0)
        
        table.resizeColumnsToContents()
        table.resizeToContents()
        
        
        print(products)
        
    def onBag(self):
        print("Bag")
        
        
        
#################### blok upravlenia #########
app= QApplication(sys.argv)

w = Window()
w.show()

sys.exit(app.exec())
