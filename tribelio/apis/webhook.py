import requests
import frappe

url = "https://tribelio.com/api/public/webhook/"

def get_default_header():
    api_key = frappe.get_value("Tribelio Settings", "Tribelio Settings", "api_key")
    return {
        'Authorization': 'Bearer {}'.format(api_key)
    }

@frappe.whitelist()
def info():
    payload={}
    response = requests.request("GET", "{}/info".format(url), headers=get_default_header(), data=payload)
    return response.json()


@frappe.whitelist()
def set_url():
    webhook_url = frappe.get_value("Tribelio Settings", "Tribelio Settings", "webhook_url")
    payload={
        "url": webhook_url
    }
    response = requests.request("POST", "{}/set".format(url), headers=get_default_header(), data=payload)
    return response.json()


@frappe.whitelist()
def unset_url():
    webhook_url = frappe.get_value("Tribelio Settings", "Tribelio Settings", "webhook_url")
    payload={
        "url": webhook_url
    }
    response = requests.request("POST", "{}/unset".format(url), headers=get_default_header(), data=payload)
    return response.json()
