import frappe
import json

@frappe.whitelist(allow_guest=True)
def log():
    data = frappe.request.data
    doc = frappe.new_doc("Tribelio Webhook Log")
    doc.response = data
    doc.insert(ignore_permissions=True)

    return "success"


@frappe.whitelist(allow_guest=True)
def log_transaction():
    log()
    frappe.db.commit()
    data = frappe.request.data
    data = json.loads(data)
    
    try:
        data_to_save = {
            "code": data['code'],
            "transaction_status": data['transactionStatus'],
            "tribe_code": data['tribe']['code'],
            "contact_name": data['contact']['name'],
            "contact_email": data['contact']['email'],
            "contact_phone": data['contact']['phone'],
            "details": [
                {
                    "product_id": data['invoices'][0]['details'][0]['productId'],
                    "product_name": data['invoices'][0]['details'][0]['productName'],
                    "product_sku": data['invoices'][0]['details'][0]['productSku'],
                    "qty": data['invoices'][0]['details'][0]['qty'],
                }
            ]
        }
    except:
        data = data['data']
        data_to_save = {
            "code": data['code'],
            "transaction_status": data['transactionStatus'],
            "tribe_code": data['tribe']['code'],
            "contact_name": data['contact']['name'],
            "contact_email": data['contact']['email'],
            "contact_phone": data['contact']['phone'],
            "details": [
                {
                    "product_id": data['invoices'][0]['details'][0]['productId'],
                    "product_name": data['invoices'][0]['details'][0]['productName'],
                    "product_sku": data['invoices'][0]['details'][0]['productSku'],
                    "qty": data['invoices'][0]['details'][0]['qty'],
                }
            ]
        }
    transaction = frappe.get_value("Tribelio Transaction", data_to_save['code'], "name")
    if transaction:
        doc = frappe.get_doc("Tribelio Transaction", transaction)
        doc.update(data_to_save)
        doc.save(ignore_permissions=True)
    else:
        doc = frappe.new_doc("Tribelio Transaction")
        doc.update(data_to_save)
        doc.insert(ignore_permissions=True)

    return "success"