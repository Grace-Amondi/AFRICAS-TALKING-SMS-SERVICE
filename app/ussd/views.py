
from flask import request
from . import ussd


@ussd.route('/ussd/callback', methods=['POST'])
def ussd_callback():
    """
    Handles post call back from AT

    :return:
    """

    # GET values from the AT's POST request
    session_id = request.values.get("sessionId", None)


    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    text_array = text.split("*")
    user_response = text_array[len(text_array) - 1]

    # create your rresponses here!
    menu_text = "END Hello Africa!"
    response = make_response(menu_text, 200)
    response.headers['Content-Type'] = "text/plain"
    return response


   