from erpnext.accounts.doctype.purchase_invoice.purchase_invoice import PurchaseInvoice
# from erpnext.erpnext.projects.doctype.task import Task
import frappe
# from frappe import _, msgprint
from custom_app.utils.qrcode import gen_qrcode

class CustomPurchaseInvoice(PurchaseInvoice):
    def onload(self):
        super().onload()
        # if self.docstatus!=1:
        #     self.update_costing()


    def validate(self):
        super().validate()
        # self.validate_advance_amount()

    def submit(self):
        super().submit()
        print("***********************************")
        print("***********************************")
        print("***********************************")
        # self.validate_advance_amount()
        self.generate_qr_code()
    
    def generate_qr_code(self):
        self.qr_code_image = "<img src='{{ gen_qrcode(self.name) }}' width='100' />"
        # gen_qrcode
        pass
        # img=qrcode.make('Hello World')
        # print("Hello")
        # print(str(img))
        # img.save('/home/malnozili/Desktop/hello.png')
        # _file = frappe.get_doc({
        #     "doctype": "File",
        #     "file_name": "hello.png",
        #     "attached_to_name": self.name,
        #     "attached_to_doctype": "Purchase Invoice",
        #     # "folder": self.get_folder("Test Folder 1", "Home").name,
        #     "file_url": '/home/malnozili/Desktop/hello.png'
        #     })
        # _file.save()

        # self.qrcode_text = str(img)
