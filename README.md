# FizzBuzz in Python  

## Description  
This project contains a simple implementation of the classic **FizzBuzz** problem in Python.  
It also includes unit tests to validate the correctness of the function.  

## Files  
- `main.py` – Implements the `fizz_buzz` function.  
- `test.py` – Contains unit tests for `fizz_buzz` using Python's `unittest` module.  

## Usage  

### Running FizzBuzz  
To run the FizzBuzz function for numbers 1 to 100, modify `main.py` like this:  

```python
if __name__ == "__main__":
    for i in range(1, 101):
        print(fizz_buzz(i))
```

Then, execute:  
```bash
python main.py
```

### Running Unit Tests  
To test the function, run:  
```bash
python -m unittest test.py
```

## Requirements  
- Python 3.x  

