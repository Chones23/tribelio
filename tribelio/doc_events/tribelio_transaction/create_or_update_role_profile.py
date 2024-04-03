import frappe

def execute(doc, method):
    if doc.transaction_status == "COMPLETED":
        user_assign_role_profile = frappe.get_value("User Assign Role Profile", {"tribelio_product": doc.details[0].product_id}, "role_profile")
        if user_assign_role_profile is not None:
            user = frappe.get_value("User", doc.contact_email, "name")
            if user is not None:
                user_doc = frappe.get_doc("User", user)
                user_doc.role_profile_name = user_assign_role_profile
                user_doc.save(ignore_permissions=True)