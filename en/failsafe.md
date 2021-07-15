# Failsafe configuration

Main article is available at https://docs.px4.io/master/en/config/safety.html.

The *Safety* panel allows you to configure actions that should be performed when a failsafe is triggered. You should at the very least configure the RC Loss failsafe, which is triggered when the RC transmitter link is lost:

1. Open the *Safety* panel.
2. Select one of the following actions in the *RC Loss Failsafe Trigger* option:
    * *Land mode* – transition to automatic land mode;
    * *Terminate* – set all outputs to their failsafe values.
3. Set the timeout value before RC Loss triggers in the *RC Loss Timeout* field. We recommend setting it to 0.5 s.

<img src="../assets/qgc-failsafe.png" alt="QGroundControl failsafe" class="zoom">
