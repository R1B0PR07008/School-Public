import json
from collections import defaultdict
import re

# Load the database export
with open('./data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Dictionary to store sorted orders
sorted_orders = defaultdict(lambda: defaultdict(list))

# Process each order
for order_id, order_data in data.get('orders', {}).items():
    # Get all gifts from this order
    gifts = order_data.get('gifts', [])
    
    for gift in gifts:
        school = gift.get('school', 'Unknown')
        recipient = gift.get('recipientName', 'Unknown')
        grade_raw = str(gift.get('grade', ''))
        gift_type = gift.get('giftType', 'Unknown')
        
        # Extract grade number and normalize
        # 9, 90, 903 → "9"
        # 10, 1002 → "10"
        grade_match = re.match(r'(\d{1,2})', grade_raw)
        if grade_match:
            grade_num = grade_match.group(1)
            # If it's a single digit (7, 8, 9), keep it
            # If it starts with 1 (10, 11, 12, 13), keep both digits
            if len(grade_num) == 1 or grade_num.startswith('1'):
                grade = grade_num
            else:
                # For 90, 80, 70 etc., take just first digit
                grade = grade_num[0]
        else:
            grade = 'Unknown'
        
        # Create order info
        order_info = {
            'order_id': order_data.get('orderID', order_id),
            'buyer_name': order_data.get('buyerName', 'Unknown'),
            'buyer_email': order_data.get('buyerEmail', 'Unknown'),
            'anonymous': order_data.get('anonymous', 'NO'),
            'recipient_name': recipient,
            'grade_raw': grade_raw,
            'grade': grade,
            'gift_type': gift_type,
            'payment_method': order_data.get('paymentMethod', 'Unknown'),
            'status': order_data.get('status', 'pending'),
            'total_amount': order_data.get('totalAmount', order_data.get('total', 0))
        }
        
        # Sort by school, then by grade for Eton
        if school == 'Eton':
            sorted_orders[school][grade].append(order_info)
        else:
            sorted_orders[school]['all'].append(order_info)

# Print results
print("="*80)
print("VALENTINE'S DAY ORDERS - SORTED BY SCHOOL & GRADE")
print("="*80)

for school in sorted(sorted_orders.keys()):
    print(f"\n{'='*80}")
    print(f"SCHOOL: {school}")
    print(f"{'='*80}")
    
    if school == 'Eton':
        # Sort Eton by grade
        for grade in sorted(sorted_orders[school].keys(), key=lambda x: int(x) if x.isdigit() else 999):
            orders = sorted_orders[school][grade]
            print(f"\n  --- GRADE {grade} ({len(orders)} gifts) ---")
            
            for order in orders:
                print(f"\n    Recipient: {order['recipient_name']}")
                print(f"    Gift: {order['gift_type']}")
                print(f"    From: {order['buyer_name']} {'(ANONYMOUS)' if order['anonymous'] == 'YES' else ''}")
                print(f"    Order ID: {order['order_id']}")
                print(f"    Payment: {order['payment_method']} - {order['status']}")
    else:
        # For non-Eton schools, just list all
        orders = sorted_orders[school]['all']
        print(f"\n  Total gifts: {len(orders)}")
        
        for order in orders:
            print(f"\n    Recipient: {order['recipient_name']} (Grade: {order['grade']})")
            print(f"    Gift: {order['gift_type']}")
            print(f"    From: {order['buyer_name']} {'(ANONYMOUS)' if order['anonymous'] == 'YES' else ''}")
            print(f"    Order ID: {order['order_id']}")
            print(f"    Payment: {order['payment_method']} - {order['status']}")

# Generate summary statistics
print(f"\n\n{'='*80}")
print("SUMMARY STATISTICS")
print(f"{'='*80}")

total_gifts = 0
for school in sorted_orders:
    school_total = sum(len(orders) for orders in sorted_orders[school].values())
    total_gifts += school_total
    print(f"{school}: {school_total} gifts")

print(f"\nTOTAL GIFTS: {total_gifts}")

# Gift type breakdown
print(f"\n{'='*80}")
print("GIFT TYPE BREAKDOWN")
print(f"{'='*80}")

gift_counts = defaultdict(int)
for school in sorted_orders:
    for grade_or_all in sorted_orders[school]:
        for order in sorted_orders[school][grade_or_all]:
            if order['gift_type']:
                gift_counts[order['gift_type']] += 1

for gift_type in sorted(gift_counts.keys()):
    print(f"{gift_type}: {gift_counts[gift_type]}")

print("\n" + "="*80)