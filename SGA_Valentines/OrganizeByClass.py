import pandas as pd

# =============================
# FILE PATH
# =============================
file_path = "students_and_orders.xlsx"

# =============================
# CLASS LIST SHEET
# =============================
class_sheet = "lista alumnos todo MS & HS"

df_classes = pd.read_excel(file_path, sheet_name=class_sheet)

# Build full name
df_classes["FullName"] = (
    df_classes["FirstName"].str.strip() + " " +
    df_classes["LastName"].str.strip()
)

# Keep only needed columns
df_classes = df_classes[["FullName", "Class"]]

# =============================
# LOAD ALL SHEETS
# =============================
all_sheets = pd.read_excel(file_path, sheet_name=None)

# Sheets to skip (do not modify)
skip_sheets = [class_sheet]

# =============================
# PROCESS EACH ORDERS SHEET
# =============================
updated_sheets = {}

for sheet_name, df_orders in all_sheets.items():

    # Skip the class list sheet
    if sheet_name in skip_sheets:
        updated_sheets[sheet_name] = df_orders
        continue

    # Skip empty sheets
    if df_orders.empty:
        updated_sheets[sheet_name] = df_orders
        continue

    # Make sure RecipientName exists
    if "RecipientName" not in df_orders.columns:
        updated_sheets[sheet_name] = df_orders
        continue

    # Clean recipient names
    df_orders["RecipientName"] = df_orders["RecipientName"].str.strip()

    # Merge with class list
    df_final = df_orders.merge(
        df_classes,
        left_on="RecipientName",
        right_on="FullName",
        how="left"
    )

    # Drop helper column
    df_final.drop(columns=["FullName"], inplace=True)

    # Sort by recipient name
    df_final = df_final.sort_values(by="RecipientName")

    # Store updated sheet
    updated_sheets[sheet_name] = df_final


# =============================
# SAVE EVERYTHING BACK
# =============================
with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
    for sheet_name, df in updated_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Done! Classes added to every grade orders sheet.")