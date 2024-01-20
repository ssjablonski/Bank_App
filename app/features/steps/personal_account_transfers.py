from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual
import sys
sys.path.append("..")

assert_equal = AssertEqual()
URL = "http://localhost:5000"

@given('I create personal account with name: "{name}", surname: "{surname}", pesel: "{pesel}"')
def create_account(context, name, surname, pesel):
    json_body = {"imie": f"{name}",
                 "nazwisko": f"{surname}",
                 "pesel": f"{pesel}"
    }
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    assert_equal(create_resp.status_code, 201) 

@step('I receive incoming transfer for amount: "{amount}" for account with pesel: "{pesel}"')
def receive_normal_transfer(context, amount, pesel):
    json_body = {"amount": int(amount),
                 "type": "incoming"
    }
    resp = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    assert_equal(resp.status_code, 200)

@step('I send outgoing transfer for amount: "{amount}" with account with pesel: "{pesel}"')
def send_normal_transfer(context, amount, pesel):
    json_body = {"amount": int(amount),
                 "type": "outgoing"
    }
    resp = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    assert_equal(resp.status_code, 200)

@step('Account saldo with pesel: "{pesel}" equals: "{expected_balance}"')
def check_account_balance(context, expected_balance, pesel):
    resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(resp.json()["Saldo"], int(expected_balance))

@step('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    resp = requests.delete(URL + f"/api/accounts/delete/{pesel}")
    assert_equal(resp.status_code, 200)
    assert_equal(resp.json()["message"], "Konto zostało usunięte")