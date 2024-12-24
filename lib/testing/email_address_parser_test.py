# lib/testing/email_address_parser_test.py
import pytest
from email_address_parser import EmailAddressParser

def test_parse_comma_separated():
    parser = EmailAddressParser("john@doe.com, person@somewhere.org")
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_space_separated():
    parser = EmailAddressParser("john@doe.com person@somewhere.org")
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_mixed_separators():
    parser = EmailAddressParser("john@doe.com, person@somewhere.org john@doe.com")
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_removes_duplicates():
    parser = EmailAddressParser("person@somewhere.org, person@somewhere.org")
    assert parser.parse() == ["person@somewhere.org"]
