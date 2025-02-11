# Convert seconds into hours, minutes, and seconds.
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

if __name__ == "__main__": 
    seconds = int(input("Enter number of seconds: "))
    h, m, s = seconds_to_hms(seconds)
    print(f"{seconds} seconds is equal to {h} hours, {m} minutes, and {s} seconds.")