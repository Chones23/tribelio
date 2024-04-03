// Copyright (c) 2022, Tribelio and contributors
// For license information, please see license.txt

var page = 0
var idx = 0
var per_page = 10
var total_page = 0
var total_data = 0
var items = []
frappe.ui.form.on('Tribelio Settings', {
	refresh: function(frm) {
		frm.add_custom_button(__("Sync"), function(){
			if (frm.doc.tribe_code != null && frm.doc.tribe_code != undefined && frm.doc.tribe_code != ""
			 	&& frm.doc.api_key != null && frm.doc.api_key != undefined && frm.doc.api_key != "") {
				// Make recursive
				page = 1
				idx = 0
				frm.events.start_sync_recursive_product(frm)
			} else {
				frappe.throw("Tribe code dan API Key perlu di isi")
			}
			
		});
		  
		if (frm.doc.webhook_url != "" && frm.doc.webhook_url != null && frm.doc.webhook_url != undefined && frm.doc.webhook_status != 'active') {
			frm.events.post_webhook_url_set(frm)
		}
		frm.events.fetch_webhook_status(frm)

		frm.set_df_property("webhook_url","read_only", frm.doc.webhook_status == "active")
	},
	unset: function(frm) {
		//POST unset webhook url
		frappe.call({
			method: 'tribelio.apis.webhook.unset_url',
			args: {},
			callback: function(r) {
				if (!r.exc) {
					if (r.message.data.status != null && r.message.data.status != undefined) {
						if (r.message.data.status != frm.doc.webhook_status) {
							frm.set_value("webhook_status", r.message.data.status)
							frm.set_value("webhook_url", "")
							frm.save()
						}
					} else {
						frappe.msgprint("Maaf, webhook sudah di set silahkan klik tombol unset untuk mengubah")
					}
				}
			}
		});
	},
	start_sync_recursive_product: function(frm) {
		if (page == 1) {
			frappe.show_progress('Sync Product..', 0, 100, 'Please wait');
			frm.save()
		}
		
		//Products
		frappe.call({
			method: 'tribelio.apis.product.get',
			args: {
				"code": frm.doc.tribe_code,
				"page": page
			},
			callback: function(r) {
				if (!r.exc) {
					console.log("atas", r.message)
					if (r.message.data) {
						total_data = r.message.data.total
						total_page = r.message.data.lastPage
						per_page = r.message.data.perPage
						items = r.message.data.items
						frappe.show_progress('Sync Product..', (idx + ((page-1) * per_page)) / (total_data) * 100, 100, 'Please wait');

						// Make recursive
						if (idx < per_page) {
							frm.events.sync_product(frm, items[idx])
						} else {
							if (page < total_page) {
								page += 1
								idx = 0
								frm.events.start_sync_recursive_product(frm)
							}
						}
					}
					
				}
			}
		});
	},
	sync_product: function(frm, data) {
		if (data != null && data != undefined) {
			frappe.call({
				method: 'tribelio.apis.sync.create_or_update_product',
				args: {
					"tribe_code": frm.doc.tribe_code,
					"store_name": data.storeName,
					"product_description": data.description,
					"product_category_id": data.category.productCategoryId,
					"product_id": data.productId,
					"product_name": data.name,
					"product_category": data.category.name,
					"product_sku": data.sku,
					"name": data.productId
				},
				callback: function(r) {
					if (!r.exc) {
						if (!r.message.name) {
							frappe.msgprint("Ada gagal sync product: "+ data.name)
						}
						idx += 1
						frappe.show_progress('Sync Product..', (idx + ((page-1) * per_page)) / (total_data) * 100, 100, 'Please wait');
						// Make recursive
						if (idx < per_page) {
							frm.events.sync_product(frm, items[idx])
						} else {
							if (page < total_page) {
								page += 1
								idx = 0
								frm.events.start_sync_recursive_product(frm)
							}
						}
					}
				}
			});
		} else {
			page = 0
			idx = 0
			per_page = 10
			total_page = 0
			total_data = 0
			items = []
			frappe.msgprint("All Product Sync Succeed")
		}
	},
	post_webhook_url_set: function(frm) {
		//POST set webhook url
		frappe.call({
			method: 'tribelio.apis.webhook.set_url',
			args: {},
			callback: function(r) {
				if (!r.exc) {
					if (r.message.data.status != null && r.message.data.status != undefined) {
						if (r.message.data.status != frm.doc.webhook_status) {
							frm.set_value("webhook_status", r.message.data.status)
							frm.save()
						}
					} else {
						frappe.msgprint("Maaf, webhook sudah di set silahkan klik tombol unset untuk mengubah")
					}
				}
			}
		});
	},
	fetch_webhook_status: function(frm) {
		//Update webhook status
		frappe.call({
			method: 'tribelio.apis.webhook.info',
			args: {},
			callback: function(r) {
				if (!r.exc) {
					if (r.message.data.status != null && r.message.data.status != undefined) {
						if (r.message.data.status != frm.doc.webhook_status) {
							frm.set_value("webhook_status", r.message.data.status)
							frm.save()
						}
						
					}
				}
			}
		});
	}
});
