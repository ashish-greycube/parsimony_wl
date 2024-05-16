import frappe

def after_migrate():
	fname = "parsimony_logo.svg"
	file_path = frappe.get_app_path("parsimony_wl", "public/images/{}".format(fname))
	print('file_path',file_path)
	with open(file_path, "rb") as f:
		file_content = f.read()

	logo_file = frappe.get_doc(
		{
			"doctype": "File",
			"file_name": fname,
			"content": file_content,
			"is_private": 0,
		}
	).insert()	

	frappe.db.set_value("Website Settings", "Website Settings", "app_name", "Parsimony")
	frappe.db.set_value("Website Settings", "Website Settings", "website_theme", "Parsimony")
	frappe.db.set_value("Website Settings", "Website Settings", "app_logo", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "banner_image", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "splash_image", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "favicon", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "navbar_template", "Parsimony Header")
	frappe.db.set_value("Website Settings", "Website Settings", "footer_template", "Parsimony Footer")