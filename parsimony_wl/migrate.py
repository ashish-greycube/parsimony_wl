import frappe

def after_migrate():
	set_logo_in_file()
	set_values_in_web_settings()

def set_logo_in_file():
	fname = "parsimony_logo.svg"
	file_path = frappe.get_app_path("parsimony_wl", "public/images/{}".format(fname))
	with open(file_path, "rb") as f:
		file_content = f.read()

	logo_file = frappe.db.get_list("File", fields=["file_name"], filters={"file_name":fname})

	if(len(logo_file) < 1):
		frappe.get_doc(
		{
			"doctype": "File",
			"file_name": fname,
			"content": file_content,
			"is_private": 0,
		}
	).insert()	

def set_values_in_web_settings():
	frappe.db.set_value("Website Settings", "Website Settings", "app_name", "Parsimony HRMS")
	frappe.db.set_value("Website Settings", "Website Settings", "website_theme", "Parsimony")
	frappe.db.set_value("Website Settings", "Website Settings", "app_logo", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "show_footer_on_login", 1)
	frappe.db.set_value("Website Settings", "Website Settings", "banner_image", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "splash_image", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "favicon", "/files/parsimony_logo.svg")
	frappe.db.set_value("Website Settings", "Website Settings", "navbar_template", "Parsimony Header")
	frappe.db.set_value("Website Settings", "Website Settings", "footer_template", "Parsimony Footer")
	frappe.db.set_value("Navbar Settings", "Navbar Settings", "app_logo", "/files/parsimony_logo.svg")