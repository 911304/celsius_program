import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    c = float(sys.argv[1])
    print(celsius_to_fahrenheit(c))
