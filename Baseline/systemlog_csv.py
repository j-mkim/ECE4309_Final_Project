import csv
import re
from datetime import datetime

# Specify the log file to read
log_filename = "system_usage_20241129_012233.log"  # Replace with actual filename
csv_filename = log_filename + ".csv"

# Regular expression to extract data from log lines
log_pattern = re.compile(r"^(?P<timestamp>.+?) - INFO - CPU Usage: (?P<cpu_usage>\d+\.?\d*)% \| Memory Usage: (?P<memory_usage>\d+\.?\d*)% \| Disk Usage: (?P<disk_usage>\d+\.?\d*)% \| Bytes Sent: (?P<bytes_sent>\d+) \| Bytes Received: (?P<bytes_recv>\d+)")

def convert_log_to_csv(log_filename, csv_filename):
    with open(log_filename, 'r') as log_file, open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write CSV header
        csv_writer.writerow(["Timestamp", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)", "Bytes Sent", "Bytes Received"])
        
        # Read log file line by line and parse the data
        for line in log_file:
            match = log_pattern.match(line)
            if match:
                timestamp = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S,%f")
                cpu_usage = match.group("cpu_usage")
                memory_usage = match.group("memory_usage")
                disk_usage = match.group("disk_usage")
                bytes_sent = match.group("bytes_sent")
                bytes_recv = match.group("bytes_recv")
                
                # Write the parsed data to the CSV file
                csv_writer.writerow([timestamp, cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_recv])

if __name__ == "__main__":
    convert_log_to_csv(log_filename, csv_filename)
