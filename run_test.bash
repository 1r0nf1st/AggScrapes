#!/usr/bin/env bash

# Declaring pytest arguments
export PYTEST_ARGUMENTS=${@:-tests/test_script.py}

# Set tag names to folders
export AUTOMATION_IMAGE=blazemeter/selenium-framework
export PROJECT_IMAGE=blazemeter/blazedemo-app-selenium

export ALLURE_RESULTS_DIR=allure-results
export PROJECT_DIR=blazedemo_app

# Create tags for selenium-base-image and the project folder
docker build selenium-base-image -t ${AUTOMATION_IMAGE}
docker build ${PROJECT_DIR} -t ${PROJECT_IMAGE}


# Run Selenium py.test with script arguments
# Map allure output xml to image folder
# Map root folder to image folder
# Set the working directory as the root folder in the image
# Set the PYTHONPATH to the root folder in the image
# Run the project image as declared above
docker run --rm \
    -v $(pwd)/$PROJECT_DIR/$ALLURE_RESULTS_DIR:/code/$ALLURE_RESULTS_DIR \
    -v $(pwd)/blazedemo_app/:/code/ \
    -w=/code \
    -e PYTHONPATH=/code/ \
    ${PROJECT_IMAGE} \
    "$PYTEST_ARGUMENTS"