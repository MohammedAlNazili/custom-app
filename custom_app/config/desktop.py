from frappe import _

def get_data():
	return [
		{
			"module_name": "custom-app",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("custom-app")
		}
	]
