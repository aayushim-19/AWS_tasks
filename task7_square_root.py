import math

def lambda_handler(event, context):

    numbers = event.get("numbers", [])

    result = []

    for num in numbers:
        result.append(math.sqrt(num))

    return {
        "square_roots": result
    }

