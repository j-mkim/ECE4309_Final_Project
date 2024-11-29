import psutil
import time
import logging
from datetime import datetime

# Set up logging with date and time in filename
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"C:/Users/jaemi/scripts/system_usage_{current_time}.log"

logging.basicConfig(filename=log_filename,
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_system_usage():
    t_end = time.time() + 60 * 5
    while time.time() < t_end:
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Get Memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        # Get Disk usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent

        # Get Network usage
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Log the system usage
        logging.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}% | Bytes Sent: {bytes_sent} | Bytes Received: {bytes_recv}")

        # Sleep for a specified interval before logging again
        time.sleep(1)  # Log every 1 seconds

if __name__ == "__main__":
    log_system_usage()
