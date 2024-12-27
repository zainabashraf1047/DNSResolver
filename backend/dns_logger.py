import logging
from datetime import datetime
import json
import csv

# Set up the DNS logger
dns_logger = logging.getLogger("dns_logger")
dns_logger.setLevel(logging.INFO)
handler = logging.FileHandler("dns_queries.log", mode="w")  # Overwrite each time
formatter = logging.Formatter("%(asctime)s | %(message)s")
handler.setFormatter(formatter)
dns_logger.addHandler(handler)


def log_query(domain, result):
    dns_logger.info(f"Query: {domain}, Result: {result}")


def export_log_to_json(log_file="dns_queries.log"):
    queries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                if "Query:" in line:  # Filter out unrelated logs
                    parts = line.strip().split(" | ")
                    if len(parts) == 2:
                        timestamp, message = parts
                        query, result = message.replace("Query: ", "").split(", Result: ")
                        queries.append({"timestamp": timestamp, "query": query, "result": result})
        with open("dns_queries.json", "w") as json_file:
            json.dump(queries, json_file, indent=4)
    except Exception as e:
        print(f"Error exporting to JSON: {e}")


def export_log_to_csv(log_file="dns_queries.log"):
    queries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                if "Query:" in line:  # Filter out unrelated logs
                    parts = line.strip().split(" | ")
                    if len(parts) == 2:
                        timestamp, message = parts
                        query, result = message.replace("Query: ", "").split(", Result: ")
                        queries.append([timestamp, query, result])
        with open("dns_queries.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Timestamp", "Query", "Result"])
            writer.writerows(queries)
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
