from app import get_ld_twilio_clients
from app.config import FROM_NUMBER
from app.config import LD_CREDS_PATH
from app.config import ONCALL
from app.config import TO_NUMBER
from app.config import TWILIO_CREDS_PATH
from app.escalate import TwilioEscalate


if __name__ == '__main__':
    user = {
        'key': '12345',
        'firstName': 'Raven',
        'lastName': 'Niners',
        'custom': {
            'group': 'top-10-customers',
        },
    }

    # get clients
    ld_client, twilio_client = get_ld_twilio_clients(
        LD_CREDS_PATH, TWILIO_CREDS_PATH,
    )

    # run the feature!
    twilio_escalate = TwilioEscalate(
        ld_client, twilio_client, ONCALL, FROM_NUMBER, TO_NUMBER,
    )
    twilio_escalate.ping(user, 'hey this feature is amazing!')
