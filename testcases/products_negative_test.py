from tools import req

rq = req.REQ()


def test_ng_tc1_product_empty_payload():
    """
    Negative test case for 'products' endpoint. Try to create a product with empty payload and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    print("Running Test Case 1: Testing 'products' endpoint, with payload being empty json.")

    input_data = {}
    info = rq.post('products', input_data)
    print info

    response_code = info[0]
    assert response_code == 201, 'Test Case 1: empty payload, Expected: 201, Actual: {act}'.format(act=response_code)

    response_body = info[1]
    assert 'errors' in response_body.keys(), "Test Case 1: empty payload, the response body " \
                                             "does not have 'errors' as key"

    exp_error_msg = "No product data specified to create product"
    act_error_msg = response_body['errors'][0]['message']

    assert exp_error_msg == act_error_msg, 'Test Case 1: empty payload, The error message is not as expected.'

    exp_error_code = "woocommerce_api_missing_product_data"
    act_error_code = response_body['errors'][0]['code']

    assert exp_error_code == act_error_code, 'Test Case 1: empty payload, The error code is not as expected.'

    print "Test Case 1: empty payload, PASS"


def test_ng_tc2_product_missing_title_key_in_payload():
    """
    Negative test case for 'products' endpoint. Try to create a product with missing parameter 'title'. Title is a
    required parameter. Making the call with no 'title' and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    print('Running Test Case 2: create product with missing parameter title')
    input_data = {}
    product = {"regular_price": '19.99', "type": 'simple'}

    input_data["product"] = product
    info = rq.post('products', input_data)

    response_code = info[0]
    assert response_code == 400, ('Test Case 2: missing parameter title, '
                                  'Expected: 400, Actual: {act}'.format(act=response_code))

    response_body = info[1]
    assert 'errors' in response_body.keys(), "Test Case 2, missing 'title' in payload, " \
                                             "The response body does not have the key 'errors'"

    exp_error_msg = "Missing parameter title"
    act_error_msg = response_body['errors'][0]['message']
    assert act_error_msg == exp_error_msg, "Test Case 2:  missing 'title' in payload, " \
                                           "The error message is not as expected."

    exp_error_code = 'woocommerce_api_missing_product_title'
    act_error_code = response_body['errors'][0]['code']
    assert act_error_code == exp_error_code, 'Test Case 1: empty payload, The error code is not as expected.'

    print "Test Case 2: empty payload, PASS"


def test_ng_tc3_product_empty_sting_for_title_in_payload():
    """
    Negative test case for 'products' endpoint. Try to create a product with empty sting for parameter 'title' in the
    payload. Title is a required parameter. Making the call with no 'title' and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    print('Running Test Case 3: create product with missing value for title')

    input_data = {}
    product = {"regular_price": '19.99', "type": 'simple', "title": ''}

    input_data["product"] = product
    info = rq.post('products', input_data)

    tc = 'ng, products, empty string for title'
    expected_message = "Content, title, and excerpt are empty."
    expected_error_code = "woocommerce_api_cannot_create_product"

    verify_ng_test_response(info, tc, expected_message, expected_error_code)


def verify_ng_test_response(response_list, test_case, exp_err_msg, exp_err_code):
    """
    Function to verify the response of the negative test cases.

    Args:
        response_list - the response of the call as a list. the has elements status code, response body and url
        test_case - the name of the test case (string)
        exp_err_msg - the expected error message
        exp_err_code - the expected error code
    """

    # verify response code
    response_code = response_list[0]
    assert response_code == 400, ('Response code is not correct for {tc} Expected: 400,'
                                  ' Actual: {act}'.format(tc=test_case, act=response_code))

    # verify there is key 'errors' in the response
    response_body = response_list[1]
    assert 'errors' in response_body.keys(), "For test case '{tc}', " \
                                             "The response body does not have the key 'errors'".format(tc=test_case)

    # verify the content of the error message
    act_error_msg = response_body['errors'][0]['message']
    assert act_error_msg == exp_err_msg, "Test Case '{tc] failed, The error message is not as expected. " \
                                         "Expected msg: {exp}, Actual msg: {act}".format(tc=test_case, exp=exp_err_msg,
                                                                                         act=act_error_msg)

    # verify the error code in the response
    act_error_code = response_body['errors'][0]['code']
    assert act_error_code == exp_err_code, "Test Case: {tc}. The error code is not as expected" \
                                           "Expected: {exp}, Actual: {act}.".format(tc=test_case,
                                                                                    exp=exp_err_code,
                                                                                    act=act_error_code)

    print "Test '{tc}' PASS".format(tc=test_case)


test_ng_tc1_product_empty_payload()
test_ng_tc2_product_missing_title_key_in_payload()
test_ng_tc3_product_empty_sting_for_title_in_payload()
