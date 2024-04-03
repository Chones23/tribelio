import frappe

def execute(doc, method):
    if doc.transaction_status == "COMPLETED":
        user = frappe.get_value("User", doc.contact_email, "name")
        if user is None:
            user_doc = frappe.new_doc("User")
            user_doc.update({
                "email": doc.contact_email,
                "first_name": doc.contact_name,
                "mobile_no": doc.contact_phone,
                "send_welcome_email": 1
            })
            user_doc.insert(ignore_permissions=True)