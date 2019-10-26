# Starting with the tiny alpine-based image of python
FROM python:3.6.9-alpine

# We install pipenv
RUN python -m pip install pipenv

# Create and change into a directory
WORKDIR /usr/app

# Create a layer of only the dependencies
# These change less often than our python code
# And this layer will be cached and not rebuild
# as we continue developing our python code
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install

# Copy in the application code
COPY . .

# Default command
# This won't run on build, and we will uses a docker compose file
# to instruct what python command should run in the container
CMD ["python", "--version"]
