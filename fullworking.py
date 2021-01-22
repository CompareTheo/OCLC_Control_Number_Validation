from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from mainui import Ui_MainWindow
from idvarify import ID_MainWindow
from pymarc import MARCReader
import csv
import pymarc
import refreshtoken
import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox)
from selenium import webdriver
import time
import re
import requests

class CloneThread(QThread):
	countChanged = pyqtSignal(int)

	def __init__(self):
		QThread.__init__(self)

	def run(self):
		i = 0
		csv_out = csv.writer(open('deprecated.csv', 'w', newline=''), delimiter=',', quotechar='"',
							 quoting=csv.QUOTE_ALL)
		csv_out.writerow(['current_oclc', 'new_oclc', 'status'])

		with open('finished.mrc', 'wb') as f:
			with open(MARC, 'rb') as fh:
				reader = MARCReader(fh)
				self.completed = 0
				for record in reader:
					oclc_number = record['001']
					oclc_sierra = re.sub("ebk", "", str(oclc_number))
					strip_oclc = re.sub("=001", "", str(oclc_sierra))
					clean_oclc = re.sub("(\D)", "", str(strip_oclc))
					record_number = record['907']
					strip_rn = re.search("\.b........", str(record_number))
					if i%800 == 0:
						refreshtoken.refreshing_token()
						a_token_file = open('access.log')
						a_token = a_token_file.readlines()
						a_token_file.close()
						for line in a_token:
							access_token = line.strip()
							print(access_token)
							authorization_header = "Bearer {} principleID=5dc41f8e-25d9-43d7-9924-20090d05d895, principleDNS=urn:oclc:platform:319".format(
								access_token)
							request_url = 'https://worldcat.org/bib/checkcontrolnumbers?oclcNumbers='
							headers = {'Authorization': authorization_header, 'Accept': 'application/atom+xml'}
							try:
								response = requests.get(request_url + clean_oclc, headers=headers)
								content = response.content
								soup = BeautifulSoup(content, 'xml')
								current_oclc = soup.find_all('currentOclcNumber')[0].get_text()
								if current_oclc != clean_oclc:
									csv_out.writerow([clean_oclc, current_oclc, 'New', strip_rn.group()])
									additional019 = pymarc.Field(
										tag='019',
										indicators=[' ', ' '],
										subfields=['aebk', current_oclc]
									)
									record.add_ordered_field(additional019)
									f.write(record.as_marc21())
									i = i + 1
									self.countChanged.emit(i)
									print(i)
								elif current_oclc == clean_oclc:
									csv_out.writerow([clean_oclc, current_oclc, 'No Change', strip_rn.group()])
									f.write(record.as_marc21())
									i = i + 1
									self.countChanged.emit(i)
									print(i)
							except AttributeError:
								csv_out.writerow([clean_oclc, 'Attribute Error', 'Error', strip_rn.group()])
								self.ExampleApp.textEdit.setText(
									"An attribute error has been raised. The error and bib number have been recorded in the deprecated spreadsheet.")
							except UnicodeError:
								csv_out.writerow([clean_oclc, 'Unicode Encoding Error', 'Error', strip_rn.group()])
								self.ExampleApp.textEdit.setText(
									"A unicode error has been raised. The error and bib number have been recorded in the deprecated spreadsheet.")
					else:
						a_token_file = open('access.log')
						a_token = a_token_file.readlines()
						a_token_file.close()
						for line in a_token:
							access_token = line.strip()
							print(access_token)
							authorization_header = "Bearer {} principleID=5dc41f8e-25d9-43d7-9924-20090d05d895, principleDNS=urn:oclc:platform:319".format(
								access_token)
							request_url = 'https://worldcat.org/bib/checkcontrolnumbers?oclcNumbers='
							headers = {'Authorization': authorization_header, 'Accept': 'application/atom+xml'}
							try:
								response = requests.get(request_url + clean_oclc, headers=headers)
								content = response.content
								soup = BeautifulSoup(content, 'xml')
								current_oclc = soup.find_all('currentOclcNumber')[0].get_text()
								if current_oclc != clean_oclc:
									csv_out.writerow([clean_oclc, current_oclc, 'New', strip_rn.group()])
									additional019 = pymarc.Field(
										tag='019',
										indicators=[' ', ' '],
										subfields=['aebk', current_oclc]
									)
									record.add_ordered_field(additional019)
									f.write(record.as_marc21())
									i = i + 1
									self.countChanged.emit(i)
									print(i)
								elif current_oclc == clean_oclc:
									csv_out.writerow([clean_oclc, current_oclc, 'No Change', strip_rn.group()])
									f.write(record.as_marc21())
									i = i + 1
									self.countChanged.emit(i)
									print(i)
							except AttributeError:
								csv_out.writerow([clean_oclc, 'Attribute Error', 'Error', strip_rn.group()])
								self.ExampleApp.textEdit.setText(
									"An attribute error has been raised. The error and bib number have been recorded in the deprecated spreadsheet.")
							except UnicodeError:
								csv_out.writerow([clean_oclc, 'Unicode Encoding Error', 'Error', strip_rn.group()])
								self.ExampleApp.textEdit.setText(
									"A unicode error has been raised. The error and bib number have been recorded in the deprecated spreadsheet.")

class LoginForm(QWidget, ID_MainWindow):
	def __init__(self):
		loginsuccess = pyqtSignal()
		self.access_token = None
		self.refresh_token = None
		super(LoginForm, self).__init__()
		self.iduisetup(self)
		self.setWindowTitle('OCLC Authenication - Login')
		self.setWindowIcon(QtGui.QIcon('loginicon.JPG'))
		self.resize(426, 267)
		self.pButton.setText("Login")
		self.pButton.clicked.connect(self.check_password)


	def check_password(self):
		msg = QMessageBox()
		authorize_url = " https://oauth.oclc.org/auth/319"
		token_url = "https://oauth.oclc.org/token"
		callback_uri = "https://library.lmu.edu"

		client_id = 'c8xdg03m0ENtsvOtUqtijdxmxbtvYPv7uuWxJOzpXs6nMnILMh6UHfPGqbN5ryS4h6i17NW74tb9voVe'
		client_secret = 'twUZCIQdXvRgHYz0mLVwCwLZ0h87VUPr'

		authorization_redirect_url = authorize_url + '?client_id=' + client_id + '&redirect_uri=' + callback_uri + '&response_type=code&scope=WorldCatMetadataAPI%20refresh_token'

		fireFoxOptions = webdriver.FirefoxOptions()
		fireFoxOptions.headless = False
		browser = webdriver.Firefox(options=fireFoxOptions)

		browser.get(authorization_redirect_url)
		time.sleep(5)
		username = browser.find_element_by_id("username")
		password = browser.find_element_by_id("password")
		submit = browser.find_element_by_id("submitSignin")
		username.send_keys(self.lineEdit.text())
		password.send_keys(self.lineEdit_2.text())

		submit.click()
		time.sleep(10)
		approve = browser.find_element_by_id("approveButton")
		approve.click()
		auth_url = browser.current_url
		browser.quit()

		regex = r"(?<=\=)(.*?)(?=\&)"
		auth = re.search(regex, auth_url)
		auth_token = auth.group(1)
		print(auth_token)

		authorization_code = auth_token

		data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
		print("requesting access token")
		access_token_response = requests.post(token_url, data=data, allow_redirects=False,
											  auth=(client_id, client_secret))

		access_response = access_token_response.text
		regex = r"(tk_.{36})"
		access = re.search(regex, access_response)
		self.access_token = access.group(1)
		with open('access.log', 'w') as a:
			a.write(self.access_token)
		print(self.access_token)

		access_response = access_token_response.text
		regex = r"(rt_.{36})"
		access = re.search(regex, access_response)
		self.refresh_token = access.group(1)
		with open('refresh.log', 'w') as r:
			r.write(self.refresh_token)
		print(self.refresh_token)

		if self.access_token is not None:
			msg.setText('Authentication Successful')
			msg.exec_()

		else:
			msg.setText('Authentication Error - Please Try Again')
			msg.exec_()


#GUI & Instruction Class
class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):
		Signal = QtCore.pyqtSignal
		super(ExampleApp, self).__init__(parent)
		self.running_thread = CloneThread()
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('icon.JPG'))
		self.pushButton.setText("Select File")
		self.pushButton.clicked.connect(self.get_file)
		self.startButton.setText("Run Script")
		self.startButton.clicked.connect(self.run_script)
		self.running_thread.countChanged.connect(self.updateProgressBar)
		self.actionLogin.triggered.connect(self.login_popup)

	def get_file(self):
		global MARC
		global record_count
		MARC, _ =QFileDialog.getOpenFileName(None, 'Open File', r"", '')
		with open(MARC, 'rb') as cr:
			count_reader = MARCReader(cr)
			record_count = sum(1 for record in count_reader)
			self.progressBar.setMaximum(record_count)
			cr.close()

	def run_script(self):
		self.pushButton.setEnabled(False)  # Disables the pushButton
		self.startButton.setEnabled(False)
		self.textEdit.setText("The OCLC validation operation has started.")  # Updates the UI
		self.running_thread.start()  # Finally starts the thread

	def updateProgressBar(self, value):
		self.progressBar.setValue(value)

	def login_popup(self):
		self.loginapp = QtWidgets.QApplication(sys.argv)
		self.exPopup = LoginForm()
		self.exPopup.show()
		self.loginapp.exec()


def main():
	app = QtWidgets.QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()