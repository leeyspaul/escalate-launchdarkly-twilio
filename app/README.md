# escalate

escalate is a demo feature built to send a text through Twilio SMS Python based on a text sentiment score given some piece of text (e.g. email, Slack).

When the feature flag `escalate` is toggled to True the Twilio SMS feature will have a higher sensitivity to text articles. If toggled to False, the Twilio SMS feature will have a lower sensitivity.

## Instructions

The instructions here assume you have a LaunchDarkly and Twilio account to get the respective `SDK_KEY` and `ACCOUNT_SID` as well as `AUTH_TOKEN`.

1. Set your credentials in the `config.py` file. You can optionally pass them in directly by modifying the code in `__init__.py`

2. Run the code in `run.py` with `python run.py`
