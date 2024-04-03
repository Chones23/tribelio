import frappe
import json

@frappe.whitelist()
def create_or_update_product(tribe_code, store_name, product_description, product_category_id, product_id, product_name, product_category, product_sku, name):

    doctype = "Tribelio Product"
    docname = name

    name = frappe.get_value(doctype, docname, "name")
    if name:
        doc = frappe.get_doc(doctype, docname)
        doc.update({
            "tribe_code": tribe_code,
            "store_name": store_name, 
            "product_description": product_description, 
            "product_category_id": product_category_id, 
            "product_id": product_id, 
            "product_name": product_name, 
            "product_category": product_category, 
            "product_sku": product_sku
        })
        doc.save(ignore_permissions=True)
    else:
        doc = frappe.new_doc(doctype)
        doc.update({
            "tribe_code": tribe_code,
            "store_name": store_name, 
            "product_description": product_description, 
            "product_category_id": product_category_id, 
            "product_id": product_id, 
            "product_name": product_name, 
            "product_category": product_category, 
            "product_sku": product_sku
        })
        doc.insert(ignore_permissions=True)
    
    return doc