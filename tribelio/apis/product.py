import requests
import frappe

url = "http://tribelio.com/api/public/product"

def get_default_header():
    api_key = frappe.get_value("Tribelio Settings", "Tribelio Settings", "api_key")
    return {
        'Authorization': 'Bearer {}'.format(api_key)
    }
  
def get_default_token():
    api_key = frappe.get_value("Tribelio Settings", "Tribelio Settings", "api_key")
    return api_key
  

@frappe.whitelist()
def get(code, page=1):
  payload={}
  headers = {}

  response = requests.request("GET", "{}/get?token={}&code={}&page={}".format(url, get_default_token(), code, page), headers=headers, data=payload)

  return response.json()


