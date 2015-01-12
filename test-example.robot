*** Settings ***
Library  Process

*** Test Cases ***
needle_visual_test_first_time
    ${result} =  Run Process  nosetests  ${CURDIR}/robot-framework-needle.py  --with-save-baseline
    log  ${result.stdout}
    log  ${result.stderr}

needle_visual_test_next_times
    ${result} =  Run Process  nosetests  ${CURDIR}/robot-framework-needle.py
    log  ${result.stdout}
    log  ${result.stderr}
    should not contain  ${result.stderr}  Unable to locate element
    should not contain  ${result.stderr}  did not match the baseline
