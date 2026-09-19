**Message Processor**

- Git --> FastAPI --> StreamLit --> Docker

**Git** is an open-source, distributed version control system designed to track changes in source code during software development. Its core purpose is to allow multiple people to work on the same project simultaneously without overwriting each other's progress.

**Streamlit** is a free, open-source Python framework that lets you turn data scripts into interactive web applications without using HTML, CSS, or JavaScrip

**FastAPI** is a modern, high-performance web framework for building APIs with Python based on standard Python type hints. It is exceptionally fast, easy to code, and production-ready.

**Docker** is an open platform used to package, ship, and run applications inside lightweight, isolated environments called containers. By bundling code with its exact dependencies, libraries, and configuration files, it solves the infamous "it works on my machine" problem by ensuring software runs identically across development, testing, and production environments.

To start the streamlit application use the below command
`streamlit run app.py`

to start the fast api use the below command
`uvicorn api:app –reload –port 8000`