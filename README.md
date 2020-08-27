# escalate

escalate is a demo feature built to send a text through Twilio SMS Python based on a text sentiment score given some piece of text (e.g. email, Slack).

When the feature flag `escalate` is toggled to True the Twilio SMS feature will have a higher sensitivity to text articles. If toggled to False, the Twilio SMS feature will have a lower sensitivity.

## Feature overview

The [ping](https://github.com/leeyspaul/escalate-launchdarkly-twilio/blob/master/app/escalate.py#L40) functionality depends on the feature flag to be toggled `True` or `False`. 

When `True` the text sensitivty will be raised higher (the range is between -1.0 and 1.0). With the higher sensitivity, it will trigger a Twilio SMS based on text that are not outright "angry" or "sad". 

Feature: [_lower_threshold_escalation_ping](https://github.com/leeyspaul/escalate-launchdarkly-twilio/blob/master/app/escalate.py#L100)


When `False` the text sensitivity will be lowered and the Twilio SMS trigger will on send on text that are directly "angry" or "sad". 

Feature: [_higher_threshold_escalation_ping](https://github.com/leeyspaul/escalate-launchdarkly-twilio/blob/master/app/escalate.py#L106)

## Instructions

The instructions here assume you have a LaunchDarkly and Twilio account to get the respective `SDK_KEY` and `ACCOUNT_SID` as well as `AUTH_TOKEN`.

1. Set your credentials in the `config.py` file. You can optionally pass them in directly by modifying the code in `__init__.py`

2. Run the code in `run.py` with `python run.py`
