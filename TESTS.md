# Generate Test Case with Github Copilot

```
I am working on a Flask application using Blueprints. The file I'm currently in contains REST API routes registered using Flask's Blueprint. The application also sets the `template_folder` path for rendering UI templates.

Please analyze this file and help generate **unit test cases using pytest** for the Flask routes defined here.

The tests should cover:

1. Functional test cases for successful responses (HTTP 200 or 201) 
2. Negative test cases (e.g., missing params, invalid input, unauthorized access) 
3. Security test case for XSS or HTML/script injection in input fields 

Make sure to:
- Use `pytest` style functions (not classes)
- Use Flask's test client (`app.test_client()`) to make requests
- Include proper `setup_module()` if needed to register the Blueprint
- Mock any database or third-party service if it's used in the route logic
- Use descriptive function names and inline comments to explain each test

Generate the test cases in a new file called `test_<router_filename>.py`
And save it under the /tests folder
```


## Observation

### 1. Save the new file
Save the new file under `__App_folder__/sample_app/tests/`

### 2. Run `pytest`

```bash
pytest

#Output
sample_app\tests\test_profile.py:96: AssertionError
=============================== short test summary info ===============================
FAILED sample_app/tests/test_profile.py::test_profile_list_file_not_found - FileNotFoundError
FAILED sample_app/tests/test_profile.py::test_profile_list_unauthorized_access - assert 200 in [401, 403]
============================ 2 failed, 10 passed in 0.68s ============================= 
```

Based on the error we need to update the templates folder, but Copilot couldnt help in solving it as the context was not set to the complete folder.

```bash

We need to include the Roor app path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


```

After this we can run the pytest again and it should run without any errors.