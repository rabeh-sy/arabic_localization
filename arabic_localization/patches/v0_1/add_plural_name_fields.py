import frappe

def execute():
    # Add plural_name field to DocType if it doesn't exist
    frappe.db.sql_ddl("""
        ALTER TABLE `tabDocType`
        ADD COLUMN IF NOT EXISTS `plural_name` VARCHAR(255)
    """)
