import logging
import json
import csv
from datetime import datetime

# Configure logging
logging.basicConfig(filename="dns_queries.log", level=logging.INFO, format="%(asctime)s | %(message)s")

def log_query(domain, result):
    """Logs DNS query results to a file."""
    logging.info(f"Query: {domain}, Result: {result}")


def export_log_to_json(log_file="dns_queries.log"):
    """Exports logs to a JSON file."""
    queries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    query_part, result_part = parts
                    if query_part.startswith("Query:") and result_part.startswith("Result:"):
                        domain = query_part.split("Query:")[1].strip()
                        result = result_part.split("Result:")[1].strip()
                        queries.append({"timestamp": parts[0], "query": domain, "result": result})
        with open("dns_queries.json", "w") as json_file:
            json.dump(queries, json_file, indent=4)
        print("Exported to dns_queries.json successfully.")
    except Exception as e:
        print(f"Error exporting to JSON: {e}")


def export_log_to_csv(log_file="dns_queries.log"):
    """Exports logs to a CSV file."""
    queries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    query_part, result_part = parts
                    if query_part.startswith("Query:") and result_part.startswith("Result:"):
                        domain = query_part.split("Query:")[1].strip()
                        result = result_part.split("Result:")[1].strip()
                        queries.append([parts[0], domain, result])
        with open("dns_queries.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Timestamp", "Query", "Result"])
            writer.writerows(queries)
        print("Exported to dns_queries.csv successfully.")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")


# Example usage:
# log_query("www.google.com", "172.217.16.196")
# export_log_to_json()
# export_log_to_csv()
