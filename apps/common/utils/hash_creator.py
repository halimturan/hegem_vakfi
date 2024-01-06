import hashlib
import base64
import requests
from hegem_vakfi.settings import PAYMENT_OK_URL, PAYMENT_FAIL_URL, PAYMENT_CLIENT_ID


def hash_creator(oid, amount, store_key):
    plain_text = f"{PAYMENT_CLIENT_ID}{oid}{amount}{PAYMENT_OK_URL}{PAYMENT_FAIL_URL}Auth2asdf{store_key}"
    hash_object = hashlib.sha1(plain_text.encode('utf-8'))
    print(hash_object.digest())
    print(hash_object.hexdigest())
    encoded = base64.b64encode(hash_object.digest())
    print(encoded)

    r = requests.post('https://sanalpos.isbank.com.tr/fim/est3Dgate/', data={
        "clientid": "700679591149",
        "storetype": "3d_pay",
        "hash": "j0mHm/eg2RdKwu3LnMr1s7c8okU=",
        "islemtipi": "Auth",
        "amount": "10",
        "currency": "949",
        "oid": "112233",
        "okUrl": "http://127.0.0.1:8080/payment/success",
        "failurl": "http://127.0.0.1:8080/payment/fail",
        "lang": "tr",
        "rnd": "asdf",
        "pan": "4242424242424242",
        "Ecom_Payment_Card_ExpDate_Year": "28",
        "Ecom_Payment_Card_ExpDate_Month": "11"})
    print(r.status_code)
    print(r.text)


hash_creator(1, 10, 123456)

