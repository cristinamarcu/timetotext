![example workflow](https://github.com/cristinamarcu/timetotext/actions/workflows/python-app.yml/badge.svg)


# Convert HH:MM time to human friendly text.

* 1:00 One o'clock
* 2:00 Two o'clock
* 13:00 One o'clock
* 13:05 Five past one
* 13:10 Ten past one
* 13:25 Twenty five past one
* 13:30 Half past one
* 13:35 Twenty five to two
* 13:55 Five to two

## Running the main script.
### Output the current time.
For example, if we execute this program at 16:30, it should output "Half past four":
```commandline
> main.py 
Half past four
```

### Generic conversion.
Allow the command to take an arbitrary Numeric Time parameter as input and return the "Human Friendly Text" equivalent.
```commandline
> main.py 11:00
Eleven o'clock
```

## Unit tests.
Unit tests for the conversion logic are available in the unittest folder.
```commandline
python -m unittest ./unittest/testConvert.py
Ran 7 tests in 0.002s

OK
```
Unit tests are run by **Github CI** [Actions](https://docs.github.com/en/actions). 
See the status on the Actions tab of the repo and in each pull request. 

## As an Azure HTTP Function.
Start the local Azure function and access it. 
Quick start guide is available [here](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python).
* For current time: `http://localhost:7071/api/HttpExample`
* With user supplied query: `http://localhost:7071/api/HttpExample?time=14:00`

Returns a JSON in the format: `{"time_text": "Two o'clock"}`

More about Azure functions and serverless computing [here](https://azure.microsoft.com/en-gb/products/functions).
