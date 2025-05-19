from pywfp import Filter

# Create a filter to block TCP traffic to port 80
filter = Filter(action="block", protocol="tcp", dst_port=80)
filter.add()

# Note: This is a placeholder; actual PyWFP syntax may differ
print("Windows filter applied")