import argparse
import json
from decimal import Decimal, InvalidOperation

# Check if a value can be parsed to Decimal. Returns (is_valid, Decimal or None)
def try_parse_decimal(value):
    try:
        return True, Decimal(value)
    except (InvalidOperation, TypeError):
        return False, None

# Validate that a value matches the sum of its children
# Includes checks for invalid decimal strings
def validate_level(name, value, children, path):
    errors = []

    # Validate that the parent value is a valid decimal
    parent_valid, parent_decimal = try_parse_decimal(value)
    if not parent_valid:
        errors.append({
            "path": path,
            "name": name,
            "error": "Invalid decimal format",
            "field": "value",
            "raw_value": value
        })
        return False, errors

    # If there are no children (either None or empty list), skip child sum validation (it's a leaf)
    if not children:
        return True, []  # Leaf node, no errors, just return True

    # Validate all child values are decimals and sum them
    child_total = Decimal("0")
    for child in children or []:  # In case children is None, we convert it to an empty list
        child_value = child.get("value")
        child_name = child.get("name")
        child_path = f"{path} > {child_name}"
        is_valid, child_decimal = try_parse_decimal(child_value)

        if not is_valid:
            errors.append({
                "path": child_path,
                "name": child_name,
                "error": "Invalid decimal format",
                "field": "value",
                "raw_value": child_value
            })
        else:
            child_total += child_decimal

        # Recursively validate children of each child object (if it has children)
        child_items = child.get("items", [])
        valid, child_errors = validate_level(
            name=child_name,
            value=child_value,
            children=child_items,
            path=child_path
        )
        if not valid:
            errors.extend(child_errors)

    # If any decimal parsing errors, skip comparison
    if errors:
        return False, errors

    # Compare parent to sum of children
    if parent_decimal != child_total:
        errors.append({
            "path": path,
            "name": name,
            "error": "Value mismatch",
            "expected": str(parent_decimal),
            "actual": str(child_total)
        })
        return False, errors

    return True, []

# Validates the entire JSON structure recursively
def validate_json(data):
    is_validated = True
    validation_errors = []

    # Iterate over the entire JSON data
    for section_key, section in data.items():
        # Start recursive validation from the root section
        valid, errors = validate_level(
            name=section.get("name"),
            value=section.get("value"),
            children=section.get("items"),
            path=section_key
        )
        if not valid:
            validation_errors.extend(errors)
            is_validated = False

    return {
        "is_validated": is_validated,
        "validation_errors": validation_errors
    }


def main(): 
    parser = argparse.ArgumentParser(description="Validate a financial JSON file.")
    parser.add_argument("--file", "-f", required=True, help="Path to the financial JSON file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        data = json.load(f)

    result = validate_json(data)
    print(json.dumps(result, indent=2))

    if not result["is_validated"]:
        exit(1)

if __name__ == "__main__":
    main()