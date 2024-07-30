import json
import logging

logging.basicConfig(filename="prod_validation.log",
                    format="%(asctime)s %(levelname)s %(message)s",
                    level=logging.INFO)

def parse_products(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

    products = []
    for product in data:
        if "name" not in product:
            logging.error("Product missing required field: name")
            continue
        if "price" not in product:
            logging.error("Product missing required field: price")
            continue
        products.append(product)
        logging.info(f"Added product to inventory: {product['name']}")

    return products

def write_products(file_path, products):
    with open(file_path, "w") as f:
        json.dump(products, f)

if __name__ == "__main__":
    products = parse_products("prod_sample.json")
    write_products("validated_products.json", products)
    