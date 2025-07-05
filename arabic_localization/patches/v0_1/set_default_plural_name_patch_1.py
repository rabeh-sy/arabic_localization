import frappe

def execute():
    # Map of DocType names to their plural names
    plural_name_map = {
        "Customer": "Customers",
        "Item": "Items",
        "Supplier": "Suppliers",
        "Lead": "Leads",
        "Opportunity": "Opportunities",
        # Add more mappings as needed
    }

    for name, plural_name in plural_name_map.items():
        if frappe.db.exists("DocType", name):
            frappe.db.set_value("DocType", name, "plural_name", plural_name)
