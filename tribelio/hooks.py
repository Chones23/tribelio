# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tribelio"
app_title = "Tribelio"
app_publisher = "Tribelio"
app_description = "Tribelio"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tribelio"
app_license = "TBL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tribelio/css/tribelio.css"
# app_include_js = "/assets/tribelio/js/tribelio.js"

# include js, css files in header of web template
# web_include_css = "/assets/tribelio/css/tribelio.css"
# web_include_js = "/assets/tribelio/js/tribelio.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tribelio.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tribelio.install.before_install"
# after_install = "tribelio.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tribelio.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Tribelio Transaction": {
		"validate": [
            "tribelio.doc_events.tribelio_transaction.create_user_if_not_exist.execute",
            "tribelio.doc_events.tribelio_transaction.create_or_update_role_profile.execute"
        ]
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tribelio.tasks.all"
# 	],
# 	"daily": [
# 		"tribelio.tasks.daily"
# 	],
# 	"hourly": [
# 		"tribelio.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tribelio.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tribelio.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tribelio.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tribelio.event.get_events"
# }

