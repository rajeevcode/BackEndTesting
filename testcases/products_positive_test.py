from tools import req
from tools import dbconnect
import json

# creating our object to be used to make API call and db connections
rq = req.REQ()
qry = dbconnect.DBConnect()


def test_create_a_product():
    """
    Function to make 'products' API call to create a product.
    Some value for payload are hardcoded, the call made and then the data in the response verified.
    """

    # print "Running 'create product' endpoint test ...."

    # set global variables to be used in different functions
    # global rs_id

    # create payload for the call
    # print 'Building the payload for the call'
    global product_id
    global title
    global price
    title = 'TEST1 TEST'
    price = '9.99'

    input_data = {
                        'product': {
                            'title': title,
                            'type': 'simple',
                            'regular_price': price}}

    # print "Making the 'product' API call"
    info = rq.post('product', input_data)
    # print info
    response_code = info[0]
    response_body = info[1]

    # print info[0]
    # print json.dumps(info[1], indent=4)

    response_code = info[0]
    response_body = info[1]

    print "Verifying the response status code"
    assert response_code == 404, "The status code returned creating product is not as " \
                                 "expected. Expected: 400, Actual: {act}".format(act=response_code)

    rs_title = response_body["product"]["title"]
    rs_price = response_body["product"]["regular_price"]
    product_id = response_body["product"]["id"]
    # title ='abc'

    print 'id is: {}'.format(product_id)

    print "verifying the title in the response"
    assert rs_title == title, "The title in response is not same as in request." \
                              "The response title is: {}".format(rs_title)

    print "verifying the price in the response"
    assert rs_price == price, "The price in response did not match." \
                              "Expected: {}, Actual, {}".format(price, rs_price)

    print 'The create_product test PASS'


def test_verify_product_created_in_db():
    """
    Function to query the data base and verify product is created with the correct information.

    Note:
        This function depends on the first function 'test_create_a_product()' being called first. The variables
        set in that function are used in this function.
    """

    print "Querying the database to get product information"
    sql ='''SELECT p.post_title, p.post_type, pm.meta_value FROM ak_posts p JOIN ak_postmeta pm
            ON p.id=pm.post_id WHERE p.id={} AND pm.meta_key='_regular_price' '''.format(product_id)
    qrs = qry.select('wp975', sql)
    print qrs

    # extracting the data
    db_title = qrs[0][1]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]

    print "Verifying the product title"
    assert db_title == title, "The tile in db is not as expected. DB title: {}, " \
                              "Expected: {}".format(db_title, title)

    print "Verifying the post_type"
    assert db_type == 'product', "The post_type in DB is not 'product'.Expected: 'product', " \
                                 "Actual: {}".format(db_type)

    print "Verifying the product regular price"
    assert db_regular_price == price, "The regular price in db is not as expected. Expected: {}, " \
                                      "Actual: {}".format(price, db_regular_price)

    print "'products positive tc, verify product created in db, PASS"


test_create_a_product()
test_verify_product_created_in_db()