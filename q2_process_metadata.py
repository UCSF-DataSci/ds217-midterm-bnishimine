#!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.

def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    storage = {}
    with open(filepath, 'r') as file:
        for line in file:
            splitter = line.split('=')
            storage[splitter[0]] = splitter[1]  
    return storage



def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    guidelines = {}
    for key in config:
        config[key] = int(config[key])

    if config['sample_data_rows'].type() == int:
        guidelines['sample_data_rows'] = False
    elif config['sample_data_rows'] <= 0:
        guidelines['sample_data_rows'] = False
    else:
        guidelines['sample_data_rows'] = True
    
    if config['sample_data_min'].type() == int:
        guidelines['sample_data_min'] = False
    elif config['sample_data_min'] < 1:
        guidelines['sample_data_min'] = False
    else:
        guidelines['sample_data_min'] = True

    if config['sample_data_max'].type() == int:
        guidelines['sample_data_max'] = False
    elif config['sample_data_max'] <= config['sample_data_min']:
        guidelines['sample_data_max'] = False
    else:
        guidelines['sample_data_max'] = True
    return guidelines
        



def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # TODO: Parse config values (convert strings to int)
    num_rows = int(config['sample_data_rows']) 
    min_value =int(config['sample_data_min'])
    max_value = int(config['sample_data_max'])
    # TODO: Generate random numbers and save to file
    # TODO: Use random module with config-specified range
    import random
    with open(filename, 'w') as file:
        for _ in range(num_rows):
            random_number = random.randint(min_value, max_value)
            file.write(f"{random_number}\n")



def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    dict_stats = {}
    dict_stats['mean'] = sum(data) / len(data)
    dict_stats['median'] = sorted(data)[len(data) // 2]
    dict_stats['sum'] = sum(data)
    dict_stats['count'] = len(data)
    return dict_stats



if __name__ == '__main__':
    # TODO: Test your functions with sample data
    # Example:
    config = parse_config('q2_config.txt')
    validation = validate_config(config)
    generate_sample_data('data/sample_data.csv', config)
    # 
    # TODO: Read the generated file and calculate statistics
    # TODO: Save statistics to output/statistics.txt    
    input = list()
    with open('data/sample_data.csv', 'r') as file:
        for line in file:
            input.append(int(line))
    save_data = calculate_statistics(input)    

    with open('output/statistics.txt', 'w') as file:
        for key, value in save_data.items():
            file.write(f"{key}: {value}\n")
    pass
