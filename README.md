# pytest
Testing funtions and APIs via pytest module

## To run
```
python -m pytest -v module/tests/test_1.py
```

To solve the problem of relative import, path for main folder needs to be added via the command ``` sys.path.append() ```

To pass the configuration file (which contains environment values) during runtime install the ```pytest-env``` module and run the test cases like ``` python -m pytest -v module/tests/test_1.py -c pytest.ini -s ```

## For mock usage

https://codefellows.github.io/sea-python-401d7/lectures/mock.html
