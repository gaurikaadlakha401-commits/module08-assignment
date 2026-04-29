# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Services dictionary
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "Technical Support": 90
}

# TODO 2: Customer dictionaries
customer1 = {"company_name": "Alpha Corp", "contact_person": "John Smith", "email": "john@alphacorp.com", "phone": "813-555-1111"}
customer2 = {"company_name": "Beta Industries", "contact_person": "Sarah Lee", "email": "sarah@beta.com", "phone": "813-555-2222"}
customer3 = {"company_name": "Gamma Solutions", "contact_person": "David Kim", "email": "david@gamma.com", "phone": "813-555-3333"}
customer4 = {"company_name": "Delta Tech", "contact_person": "Emily Clark", "email": "emily@delta.com", "phone": "813-555-4444"}

# TODO 3: Master customers dictionary
customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"Customer ID: {cid}")
    for k,v in info.items():
        print(f"  {k}: {v}")
    print()

# TODO 5: Customer lookups
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "813-999-0000"
customers["C002"]["industry"] = "Manufacturing"

print("\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Project dictionaries
projects = {
    "C001": [
        {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 40, "budget": 8800}
    ],
    "C002": [
        {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 60, "budget": 10500}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 80, "budget": 16000}
    ],
    "C004": [
        {"name": "System Maintenance", "service": "Technical Support", "hours": 30, "budget": 2700}
    ]
}

print("\nProject Information:")
print("-" * 60)
for cid, plist in projects.items():
    for p in plist:
        print(f"{cid} - {p}")

# TODO 8: Project cost calculations
print("\nProject Cost Calculations:")
print("-" * 60)
for cid, plist in projects.items():
    for p in plist:
        cost = p["hours"] * services[p["service"]]
        print(f"{p['name']} (Customer {cid}) Cost: ${cost}")

# TODO 9: Customer statistics
print("\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [c["company_name"] for c in customers.values()])
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {s: 0 for s in services}
for plist in projects.values():
    for p in plist:
        service_counts[p["service"]] += 1

print("\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
all_budgets = [p["budget"] for plist in projects.values() for p in plist]
all_hours = [p["hours"] for plist in projects.values() for p in plist]

total_budget = sum(all_budgets)
total_hours = sum(all_hours)
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print("\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Highest Project Budget:", max_budget)
print("Lowest Project Budget:", min_budget)

# TODO 12: Customer summary report
print("\nCustomer Summary Report:")
print("-" * 60)
for cid, info in customers.items():
    plist = projects.get(cid, [])
    total_h = sum(p["hours"] for p in plist)
    total_b = sum(p["budget"] for p in plist)
    print(f"{info['company_name']} ({cid})")
    print("Projects:", len(plist))
    print("Total Hours:", total_h)
    print("Total Budget:", total_b)
    print()

# TODO 13: Adjust service rates using dictionary comprehension
adjusted_rates = {s: r*1.1 for s,r in services.items()}
print("\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Active customers dictionary comprehension
active_customers = {cid: cust for cid, cust in customers.items() if cid in projects and len(projects[cid])>0}
print("\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Customer budget totals dictionary comprehension
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print("\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers
service_tiers = {s: "Premium" if r>=200 else "Standard" if r>=100 else "Basic" for s,r in services.items()}
print("\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(cust):
    required = ["company_name","contact_person","email","phone"]
    return all(field in cust for field in required)

print("\nCustomer Validation:")
print("-" * 60)
for cid, cust in customers.items():
    print(f"{cid} Valid:", validate_customer(cust))

# TODO 18: Project status tracking
status_list = ["active","completed","pending"]
status_counts = {s: 0 for s in status_list}
i = 0
for plist in projects.values():
    for p in plist:
        p["status"] = status_list[i%3]
        status_counts[status_list[i%3]] += 1
        i += 1

print("\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function
def analyze_customer_budgets(projects_dict):
    result = {}
    for cid, plist in projects_dict.items():
        budgets = [p["budget"] for p in plist]
        total = sum(budgets)
        count = len(budgets)
        avg = total/count if count>0 else 0
        result[cid] = {"total": total, "average": avg, "count": count}
    return result

print("\nDetailed Budget Analysis:")
print("-" * 60)
budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
def recommend_services(cid, customers, projects, services):
    used_services = {p["service"] for p in projects.get(cid,[])}
    return [s for s in services if s not in used_services]

print("\nService Recommendations:")
print("-" * 60)
for cid in customers:
    print(f"{cid} Recommended:", recommend_services(cid, customers, projects, services))