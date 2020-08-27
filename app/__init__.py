import json

import ldclient
from twilio.rest import Client


# Helpers


def _get_json_credentials(creds_path):
    creds_dict = None

    with open(creds_path) as creds_file:
        creds_dict = json.load(creds_file)

    return creds_dict


def _get_sdk_credentials(ld_creds_path):
    creds = _get_json_credentials(ld_creds_path)

    return creds['SDK_KEY']


def _set_sdk_key_credentials(sdk_creds):

    ldclient.set_sdk_key(sdk_creds)


def _get_twilio_credentials(creds_path):
    creds = _get_json_credentials(creds_path)

    return (creds['ACCOUNT_SID'], creds['AUTH_TOKEN'])


def get_ld_twilio_clients(ld_creds_path, twilio_creds_path):
    # setup ld creds
    ld_sdk_key = _get_sdk_credentials(ld_creds_path)
    _set_sdk_key_credentials(ld_sdk_key)

    # setup twilio creds
    ACCOUNT_SID, AUTH_TOKEN = _get_twilio_credentials(twilio_creds_path)

    # get ld and twilio clients
    return ldclient.get(), Client(ACCOUNT_SID, AUTH_TOKEN)
