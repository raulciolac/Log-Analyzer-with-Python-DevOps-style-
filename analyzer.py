def analyze_log(file_path):
    errors = 0
    warnings = 0
    info = 0

    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1
            elif "INFO" in line:
                info += 1

    print("Log Analysis Report")
    print("-------------------")
    print(f"INFO: {info}")
    print(f"WARNING: {warnings}")
    print(f"ERROR: {errors}")


if __name__ == "__main__":
    analyze_log("sample.log")
