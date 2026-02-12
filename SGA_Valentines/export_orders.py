import json
import csv
from collections import defaultdict
import re

# Load the database export
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Dictionary to store sorted orders
sorted_orders = defaultdict(lambda: defaultdict(list))
all_orders_list = []

# Process each order
for order_id, order_data in data.get('orders', {}).items():
    # Get all gifts from this order
    gifts = order_data.get('gifts', [])
    
    for gift in gifts:
        school = gift.get('school', 'Unknown')
        recipient = gift.get('recipientName', 'Unknown')
        grade_raw = str(gift.get('grade', ''))
        gift_type = gift.get('giftType', 'Unknown')
        
        # Extract first 2 digits from grade
        grade_match = re.match(r'(\d{1,2})', grade_raw)
        if grade_match:
            grade = grade_match.group(1)
        else:
            grade = 'Unknown'
        
        # Create order info
        order_info = {
            'order_id': order_data.get('orderID', order_id),
            'buyer_name': order_data.get('buyerName', 'Unknown'),
            'buyer_email': order_data.get('buyerEmail', 'Unknown'),
            'anonymous': order_data.get('anonymous', 'NO'),
            'recipient_name': recipient,
            'school': school,
            'grade_raw': grade_raw,
            'grade': grade,
            'gift_type': gift_type,
            'payment_method': order_data.get('paymentMethod', 'Unknown'),
            'status': order_data.get('status', 'pending'),
            'total_amount': order_data.get('totalAmount', order_data.get('total', 0))
        }
        
        # Add to all orders list
        all_orders_list.append(order_info)
        
        # Sort by school, then by grade for Eton
        if school == 'Eton':
            sorted_orders[school][grade].append(order_info)
        else:
            sorted_orders[school]['all'].append(order_info)

# ===== EXPORT TO CSV =====
csv_filename = 'valentines_orders_all.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['order_id', 'school', 'grade', 'recipient_name', 'gift_type', 
                  'buyer_name', 'buyer_email', 'anonymous', 'payment_method', 'status', 'total_amount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for order in all_orders_list:
        # Only write fields that are in fieldnames
        row = {k: order[k] for k in fieldnames if k in order}
        writer.writerow(row)

print(f"✅ Exported all orders to: {csv_filename}")

# ===== EXPORT ETON BY GRADE TO SEPARATE CSVs =====
if 'Eton' in sorted_orders:
    for grade in sorted(sorted_orders['Eton'].keys(), key=lambda x: int(x) if x.isdigit() else 999):
        grade_filename = f'valentines_eton_grade_{grade}.csv'
        with open(grade_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['order_id', 'recipient_name', 'gift_type', 'buyer_name', 
                         'anonymous', 'payment_method', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for order in sorted_orders['Eton'][grade]:
                writer.writerow({
                    'order_id': order['order_id'],
                    'recipient_name': order['recipient_name'],
                    'gift_type': order['gift_type'],
                    'buyer_name': order['buyer_name'],
                    'anonymous': order['anonymous'],
                    'payment_method': order['payment_method'],
                    'status': order['status']
                })
        print(f"✅ Exported Eton Grade {grade} to: {grade_filename}")

# ===== EXPORT BY SCHOOL =====
for school in sorted_orders.keys():
    school_filename = f'valentines_{school.lower()}.csv'
    school_orders = []
    for grade_or_all in sorted_orders[school]:
        school_orders.extend(sorted_orders[school][grade_or_all])
    
    with open(school_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['order_id', 'grade', 'recipient_name', 'gift_type', 
                     'buyer_name', 'anonymous', 'payment_method', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for order in school_orders:
            writer.writerow({
                'order_id': order['order_id'],
                'grade': order['grade'],
                'recipient_name': order['recipient_name'],
                'gift_type': order['gift_type'],
                'buyer_name': order['buyer_name'],
                'anonymous': order['anonymous'],
                'payment_method': order['payment_method'],
                'status': order['status']
            })
    print(f"✅ Exported {school} orders to: {school_filename}")

# ===== EXPORT SORTED JSON =====
json_output = {
    'by_school': {},
    'summary': {
        'total_gifts': len(all_orders_list),
        'by_school': {},
        'by_gift_type': {}
    }
}

for school in sorted_orders:
    json_output['by_school'][school] = {}
    for grade_or_all in sorted(sorted_orders[school].keys(), key=lambda x: int(x) if x.isdigit() else 999):
        json_output['by_school'][school][grade_or_all] = sorted_orders[school][grade_or_all]
    
    school_total = sum(len(orders) for orders in sorted_orders[school].values())
    json_output['summary']['by_school'][school] = school_total

# Gift type summary
gift_counts = defaultdict(int)
for order in all_orders_list:
    if order['gift_type']:
        gift_counts[order['gift_type']] += 1

json_output['summary']['by_gift_type'] = dict(gift_counts)

json_filename = 'valentines_orders_sorted.json'
with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(json_output, f, indent=2, ensure_ascii=False)

print(f"✅ Exported sorted data to: {json_filename}")

# ===== PRINT SUMMARY =====
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)

for school in sorted(sorted_orders.keys()):
    school_total = sum(len(orders) for orders in sorted_orders[school].values())
    print(f"{school}: {school_total} gifts")

print(f"\nTOTAL GIFTS: {len(all_orders_list)}")

print(f"\n{'='*80}")
print("GIFT TYPE BREAKDOWN")
print(f"{'='*80}")
for gift_type in sorted(gift_counts.keys()):
    print(f"{gift_type}: {gift_counts[gift_type]}")

print("\n" + "="*80)
print(f"✅ All files exported successfully!")
print("="*80)