def divide_numbers(numerator, denominator):
    try:
        numerator, denominator = int(numerator), int(denominator)
        return numerator / denominator
    except ValueError:
        raise ValueError("Only integers please!")
    except:
        return 0
        
    pass

divide_numbers()
