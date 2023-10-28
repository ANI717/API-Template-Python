import sys
import json
import pytest
import logging
from dotenv import load_dotenv
from fastapi import HTTPException


sys.path.append("src")
load_dotenv()


with open("tests/resources/inputs.json", "r") as fp:
    inputs = json.load(fp)
with open("tests/resources/outputs.json", "r") as fp:
    outputs = json.load(fp)


@pytest.mark.utils
def test_object_to_dict():
    
    from api.utils.object_to_dict import object_to_dict
    from api.schemas.input_schema import InputKeys
    
    inputs_object = InputKeys(**inputs)
    
    assert object_to_dict(inputs_object, logging) == inputs
    
    with pytest.raises(HTTPException):
        assert object_to_dict("not_dictionary", logging)


@pytest.mark.utils
def test_generate_output():
    
    from api.utils.generate_output import generate_output
    
    assert generate_output(inputs, logging) == outputs
    
    with pytest.raises(HTTPException):
        assert generate_output(None, logging)
