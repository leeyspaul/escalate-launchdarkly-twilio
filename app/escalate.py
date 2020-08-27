import logging

from textblob import TextBlob

logging.basicConfig()
logging.root.setLevel(logging.INFO)  # demo purposes to see all info logs
logger = logging.getLogger()


class TwilioEscalate:
    """This class utilizes the global LaunchDarkly and Twilio Clients.

    For demo purposes the LaunchDarkly client is
    closed after the only function that utilizes the client.
    :func:`ping`.
    """

    def __init__(
        self,
        ld_client,
        twilio_client,
        oncall,
        from_number,
        to_number,
    ):
        """Constructs a new TwilioEscalate instance.

        :param ldclient ld_client: LaunchDarkly client.
        :param TwilioClient twilio_client: Twilio client.
        :param string oncall: name of the oncall.
        :param string from_number: number of the Twilio app.
        :param string to_number: number of the oncall to ping.
        """
        self.ld_client = ld_client
        self.twilio_client = twilio_client
        self.oncall = oncall
        self.from_number = from_number
        self.to_number = to_number

    def ping(self, escalation_needed_user, text):
        """Pings a user who has been marked as 'escalation necessary'.

        The threshold for escalation is by default set to a higher threshold.
        Flipping the feature flag will lower the escalation threshold.

        :param dict escalation_needed_user: user attributes.
        :param string text: text submitted by the user.
        """
        self.ld_client.track('escalation-needed', escalation_needed_user)

        lower_threshold_escalation_feature = self.ld_client.variation(
            'escalate', escalation_needed_user, True,
        )

        logger.info(
            'lower threshold feature is %s',
            lower_threshold_escalation_feature,
        )

        if lower_threshold_escalation_feature:
            self._lower_threshold_escalation_ping(text)

        self._higher_threshold_escalation_ping(text)

        # for demo purposes, close right away in function after use
        self.ld_client.close()

    def _calculate_escalation_score(self, text):
        blob = TextBlob(text)

        text_polarity_scores = []

        for sentence in blob.sentences:
            text_polarity_scores.append(sentence.sentiment.polarity)

        avg_polarity_score = (
            sum(text_polarity_scores) /
            len(text_polarity_scores)
        )

        logger.info('text sentiment score: %s', avg_polarity_score)

        return avg_polarity_score

    def _send_escalation_text(self, to_number):
        ESCALATION_MSG = f'Hey, {self.oncall}, something needs your attention.'

        logger.info('sending message to %s: %s', self.oncall, to_number)

        message = self.twilio_client.messages \
            .create(
                body=ESCALATION_MSG,
                from_=self.from_number,
                to=to_number,
            )

        return message.sid

    def _lower_threshold_escalation_ping(self, text):
        threshold_passed = self._calculate_escalation_score(text) < 0.4

        if threshold_passed:
            self._send_escalation_text(self.oncall, self.to_number)

    def _higher_threshold_escalation_ping(self, text):
        threshold_passed = self._calculate_escalation_score(text) < 0

        if threshold_passed:
            self._send_escalation_text(self.oncall, self.to_number)
