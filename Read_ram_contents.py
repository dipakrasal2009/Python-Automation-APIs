import psutil

# Get virtual memory details
virtual_memory = psutil.virtual_memory()

print(f"Total Memory: {virtual_memory.total}")
print(f"Available Memory: {virtual_memory.available}")
print(f"Used Memory: {virtual_memory.used}")
print(f"Percentage: {virtual_memory.percent}%")

