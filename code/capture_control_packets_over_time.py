import pyshark
import csv
import time

def capture_control_packets_over_time(scenario, capture_duration, output_file):
    # Set the capture filter based on the scenario
    if scenario == "Attack without Mitigation":
        capture_filter = "your_capture_filter_here"
    elif scenario == "Attack with Mitigation":
        capture_filter = "your_capture_filter_here"
    elif scenario == "Attack Free":
        capture_filter = "your_capture_filter_here"
    else:
        raise ValueError("Invalid scenario")
    
    # Open a live capture session
    capture = pyshark.LiveCapture()
    
    # Set the capture filter
    capture.set_debug()
    capture.sniff(timeout=capture_duration, display_filter=capture_filter)
    
    # Open the output file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(['Timestamp', 'Packet Type'])
        
        # Capture packets and write data to the CSV file
        for packet in capture:
            timestamp = packet.sniff_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            packet_type = packet.layers[0]._field_prefix
            writer.writerow([timestamp, packet_type])
            
            # Check if the capture duration has elapsed
            if time.time() > start_time + capture_duration:
                break

# Set the scenario, capture duration, and output file path
scenario = "Attack without Mitigation"  # Specify the scenario: "Attack without Mitigation", "Attack with Mitigation", or "Attack Free"
capture_duration = 6000 # Specify the duration (in seconds) to capture control packets
output_file = f"{scenario.replace(' ', '_')}_control_packets.csv"  # Specify the output file path and name

# Call the capture_control_packets_over_time function
capture_control_packets_over_time(scenario, capture_duration, output_file)
