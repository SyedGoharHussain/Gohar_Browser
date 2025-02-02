import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QStatusBar, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("✨ Gohar's Browser ✨")
        self.setGeometry(100, 100, 1200, 800)

        self.dark_mode = False  # Start in light mode

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.add_tab(QUrl("https://www.google.com"), "🌍 New Tab")

        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setMovable(False)
        self.addToolBar(nav_toolbar)

        back_btn = QAction("⬅️ Back", self)
        back_btn.triggered.connect(self.navigate_back)
        nav_toolbar.addAction(back_btn)

        forward_btn = QAction("➡️ Forward", self)
        forward_btn.triggered.connect(self.navigate_forward)
        nav_toolbar.addAction(forward_btn)

        reload_btn = QAction("🔄 Reload", self)
        reload_btn.triggered.connect(self.navigate_reload)
        nav_toolbar.addAction(reload_btn)

        home_btn = QAction("🏠 Home", self)
        home_btn.triggered.connect(self.navigate_home)
        nav_toolbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        new_tab_btn = QAction("➕ New Tab", self)
        new_tab_btn.triggered.connect(lambda: self.add_tab(QUrl("https://www.google.com"), "🌍 New Tab"))
        nav_toolbar.addAction(new_tab_btn)

        self.dark_mode_btn = QAction("🌙 Dark Mode", self)
        self.dark_mode_btn.triggered.connect(self.toggle_dark_mode)
        nav_toolbar.addAction(self.dark_mode_btn)

        portfolio_btn = QAction("👨‍💻 Creator's Portfolio", self)
        portfolio_btn.triggered.connect(self.open_portfolio)
        nav_toolbar.addAction(portfolio_btn)

        self.apply_styles()  # Apply initial styles

        self.status = QStatusBar()
        self.setStatusBar(self.status)


    def add_tab(self, url, label="🌍 New Tab"):
        browser = QWebEngineView()
        browser.setUrl(url)
        browser.urlChanged.connect(self.update_url_bar)

        self.tabs.addTab(browser, label)
        self.tabs.setCurrentWidget(browser)

        if self.dark_mode:
            self.apply_website_dark_mode(browser)


    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)


    def navigate_back(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.back()


    def navigate_forward(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.forward()


    def navigate_reload(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.reload()


    def navigate_home(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.setUrl(QUrl("https://www.google.com"))


    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.setUrl(QUrl(url))


    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)


    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.dark_mode_btn.setText("🌙 Dark Mode" if not self.dark_mode else "☀️ Light Mode")
        self.apply_styles()

        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i)
            if self.dark_mode:
                self.apply_website_dark_mode(browser)
            else:
                self.remove_website_dark_mode(browser)


    def apply_styles(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QMainWindow { background-color: #0d1117; }
                QToolBar {
                    background-color: #161b22;
                    padding: 5px;
                    border-bottom: 1px solid #30363d;
                }
                QAction {
                    font-size: 14px;
                    padding: 5px 10px;
                    color: #f0f6fc;
                }
                QAction:hover { background-color: #21262d; }
                QLineEdit {
                    font-size: 14px;
                    padding: 5px;
                    border: 1px solid #30363d;
                    border-radius: 5px;
                    min-width: 400px;
                    background-color: #0d1117;
                    color: #f0f6fc;
                }
                QTabBar::tab {
                    background: #161b22;
                    padding: 10px;
                    border: 1px solid #30363d;
                    color: #f0f6fc;
                }
                QTabBar::tab:selected {
                    background: #0d1117;
                    border-bottom: 2px solid #58a6ff;
                }
                QTabBar::tab:hover { background: #21262d; }
                QStatusBar {
                    background-color: #161b22;
                    color: #f0f6fc;
                }
                QToolButton { color: #f0f6fc; }
                QTabWidget::pane {
                    background: #0d1117;
                    border: 1px solid #30363d;
                }
            """)
        else:
            self.setStyleSheet("""  # Light Mode Styles
                QMainWindow { background-color: #f0f0f0; }  # Example
                QToolBar {
                    background-color: #f0f0f0;
                    padding: 5px;
                    border-bottom: 1px solid #ccc;
                }
                QAction {
                    font-size: 14px;
                    padding: 5px 10px;
                    color: #000;  # Black text
                }
                QAction:hover { background-color: #ddd; }
                QLineEdit {
                    font-size: 14px;
                    padding: 5px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    min-width: 400px;
                    background-color: #fff;  # White background
                    color: #000;
                }
                QTabBar::tab {
                    background: #f0f0f0;
                    padding: 10px;
                    border: 1px solid #ccc;
                    color: #000;
                }
                QTabBar::tab:selected {
                    background: #fff;
                    border-bottom: 2px solid #0078d7;  # Blue selection
                }
                QTabBar::tab:hover { background: #ddd; }
                QStatusBar {
                    background-color: #f0f0f0;
                    color: #000;
                }
                QToolButton { color: #000; }
                QTabWidget::pane {
                    background: #fff;
                    border: 1px solid #ccc;
                }
            """)


    def apply_website_dark_mode(self, browser):
        css = """
            body {
                background-color: #0d1117 !important;
                color: #f0f6fc !important;
            }
            a {
                color: #58a6ff !important;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #f0f6fc !important;
            }
            code, pre {
                background-color: #161b22 !important;
                color: #f0f6fc !important;
            }
            table, th, td {
                border: 1px solid #30363d !important;
            }
            input, textarea, select {  /* Form elements */
                background-color: #161b22 !important;
                color: #f0f6fc !important;
                border: 1px solid #30363d !important;
            }
            /* Style for buttons if needed */
            button {
                background-color: #21262d !important;  /* Darker button background */
                color: #f0f6fc !important;
                border: 1px solid #30363d !important;
            }
        """
        browser.page().runJavaScript(f"""
            var style = document.createElement('style');
            style.type = 'text/css';
            style.innerHTML = `{css}`;
            document.head.appendChild(style);
        """)

        # Scrollbar styling (WebKit)
        browser.page().runJavaScript("""
            var style = document.createElement('style');
            style.type = 'text/css';
            style.innerHTML = `
                ::-webkit-scrollbar { width: 8px; }
                ::-webkit-scrollbar-track { background: #161b22; }
                ::-webkit-scrollbar-thumb {
                    background: #30363d;
                    border-radius: 4px;
                }
                ::-webkit-scrollbar-thumb:hover { background: #58a6ff; }
            `;
            document.head.appendChild(style);
        """)


    def remove_website_dark_mode(self, browser):
        browser.page().runJavaScript("""
            var styles = document.querySelectorAll('style');
            styles.forEach(style => style.remove());
        """)


    def open_portfolio(self):
        self.add_tab(QUrl("https://syedgoharhussain.github.io/Portfolio/"), "👨‍💻 Portfolio")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Important for consistent styling

    window = Browser()
    window.show()
    sys.exit(app.exec_())