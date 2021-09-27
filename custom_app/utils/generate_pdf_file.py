
import frappe
import requests
from urllib.parse import urljoin
from frappe.utils.print_format import download_pdf
from pathlib import Path


# custom_app.utils.generate_pdf_file.get_pdf_file
@frappe.whitelist(True)
# def get_pdf_file(doctype, name, format=None, doc=None, no_letterhead=0):
def get_pdf_file():
    print("get_pdf_file")
    generated_secret = frappe.utils.password.get_decrypted_password(
    "User", "Administrator",'api_secret'
    )
    print("generated_secret", generated_secret)
    api_key = frappe.db.get_value("User", "Administrator", "api_key")
    print("api_key", api_key)
    header = {"Authorization": "token {}:{}".format(api_key, generated_secret)}
    # header = {}
    # def login():
    #     return session.get(urljoin("http://0.0.0.0:8005", '/api/method/login'), params={
    #         'usr': "Administrator",
    #         'pwd': "123"
    #     })
    # session = requests.Session()
    # login()
    url = "http://0.0.0.0:8005/api/method/frappe.utils.print_format.download_pdf?doctype=User&name=Administrator&format=Standard&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=ar"
    res = requests.get(url, headers=header, verify=False, stream=True)
    # download_pdf(doctype, name, format, doc, no_letterhead)
    print("response")
    print(res.status_code)
    file = None
    # filename = Path('metadata.pdf')
    # filename.write_bytes(res.content)
    # print("filename**")
    # print(filename)

    with open('ACC-SINV-2021-00001.pdf', 'wb') as f:
        f.write(res.content)
    
    

    # return f

    # user_key = frappe.db.get_value('User', self.user, 'api_key')
	# 	user_secret = get_decrypted_password('User', self.user, 'api_secret')


    frappe.whitelist(True)
def get_qr_file():
    frappe.local.response.filename = "Full CV ar_1.pdf"
    frappe.local.response.filecontent = read_file_content('/private/files/Full CV ar_1.pdf') # custom function
    frappe.local.response.type = "download"