"""
Utility functions for cleaning titles, extracting prices, and categorizing products.
Functions:
    clean_title(title: str) -> str:
        Cleans the given title by removing specific keywords and special characters.
    extract_price(price_text: str) -> str:
        Extracts the price from the given text. Returns the price as a string without commas,
        or 'N/A' if no price is found.
    categorize_product(name: str) -> str:
        Categorizes the product based on its name. Returns the category as a string.
"""

import re
import os
import csv
from typing import List, Tuple

class UtilityFunctions:

    def __init__(self):
        pass

    @staticmethod
    def save_to_csv(data: List[Tuple[str, str, str, str, str, str, str, str]], folder: str = "scraped_data", filename: str = "products.csv") -> None:
        """Saves scraped data to a CSV file inside a specified folder."""
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, filename)

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Category", "Vendor", "Condition", "Website", "Product URL", "Image URL"])
            writer.writerows(data)

        print(f"Data saved to {file_path}")

    @staticmethod
    def clean_title(title: str) -> str:
        title = re.sub(r'\b(New|Used)\b', '', title, flags=re.IGNORECASE)
        title = re.sub(r'[\W_]+', ' ', title)  # Remove special characters
        title = re.sub(r'\b(buy|in|pakistan|techmatched)\b', '', title, flags=re.IGNORECASE)
        return title

    @staticmethod
    def extract_price(price_text: str) -> str:
        match = re.search(r'Original price was:.*?(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)', price_text)
        if match:
            return match.group(1).replace(',', '')
        else:
            numbers = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?', price_text)
            return numbers[0].replace(',', '') if numbers else 'N/A'

    @staticmethod
    def categorize_product(name: str) -> str:
        categories = [
            ("GPU", ["gpu", "graphics card", "graphic card", "zotac", "nvidia", "intel arc", "quadro", "radeon", "firepro", "tesla", "gtx", "rtx", "rx", "asrock", "b570"]),
            ("CPU", ["processor", "chip", "ryzen", "intel i", "threadripper", "xeon", "epyc", "intel core"]),
            ("RAM", ["ram", "memory", "ddr4", "ddr5", "corsair", "g.skill", "kingston", "crucial"]),
            ("SSD", ["ssd", "solid state drive", "samsung", "crucial", "kingston", "adata", "wd", "corsair"]),
            ("HDD", ["hard drive", "hdd", "seagate", "western digital", "wd", "toshiba"]),
            ("PSU", ["psu", "power supply", "corsair", "evga", "seasonic", "cooler master", "antec"]),
            ("Motherboard", ["motherboard", "mobo", "asus", "msi", "gigabyte", "b450", "b550", "x570", "z490", "nvme slot", "m2 slot"]),
            ("Case", ["case", "chassis", "nzxt", "cooler master", "corsair", "lian li"]),
            ("Cooler", ["fan", "cooler", "heat sink", "fan kit", "noctua", "arctic", "rgb fan"]),
            ("Laptop", ["laptop", "notebook", "macbook", "ultrabook", "thinkpad", "xps", "spectre", "rog", "omen", "predator"]),
            ("Laptop Screen Protector", ["screen protector", "laptop screen guard", "privacy screen", "anti-glare", "blue light filter"]),
            ("Monitor", ["monitor", "display", "lcd", "led", "curved monitor", "gaming monitor", "4k monitor"]),
            ("Networking", ["router", "modem", "network adapter", "wireless adapter", "wifi card", "ethernet switch", "range extender"]),
            ("PC Accessories", ["keyboard", "mouse", "gamepad","controller","gaming mouse", "mechanical keyboard", "mousepad", "webcam", "headset", "usb hub"]),
            ("Consoles",["microsoft","sony","nintendo","xbox","playstation"]),
            ("Other", ["cable", "wire", "remote"])
        ]

        name_lower = name.lower()

        if "monitor arm" in name_lower:
            return "Monitor Arm"
        if "headsets" in name_lower or "headphones" in name_lower or "earbuds" in name_lower:
            return "PC Accessories"
        if "processor" in name_lower:
            return "CPU"
        if "monitor" in name_lower:
            return "Monitor"
        if "case" in name_lower:
            return "Case"
        if "fan" in name_lower and "rgb" in name_lower:
            return "Cooler"
        if "heat sink" in name_lower:
            return "Cooler"
        if "laptop" in name_lower:
            return "Laptop"
        if "cable" in name_lower or "wire" in name_lower:
            return "Other"

        for category, keywords in categories:
            if category == "GPU" and any(keyword in name_lower for keyword in ["amd", "ryzen", "intel"]):
                continue
            if any(keyword in name_lower for keyword in keywords):
                return category

        return "Other"
