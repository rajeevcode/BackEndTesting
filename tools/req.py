
from woocommerce import API


class REQ():
    """
    This class is used to make the api calls. It will create the object using the hardcoded
    consumer_key and consumer_secret.
    """

    def __init__(self):

        # store the key and secret in variable to make it easy to change
        admin_consumer_key = 'ck_a403d5a360f15491f53b83dc5315e0f572fc8e9d'  # your consumer_key goes here
        admin_consumer_secret = 'cs_fdc7223b05013054533fd8da119bf167de2c5840'  # your consumer_secret goes here

        # create an instance of API object provided by the WooCommerce Python wrapper
        # this object is responsible for authentication and for sending the requests
        self.wcapi = API(
            url="http://127.0.0.1/ak_store",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            wp_api=True,
            version="wc/v1")
            # version="v3"


    def test_api(self):
        """
        This method is used to test if the API is running and the requests can go through normally.
        The response should be information about the site such as name, version, and more ..... in a json format.
        :return: None
        """

        # make a call to the base url and print the response
        print self.wcapi.get("").json()

    def post(self, endpoint, data):
        """
        This method is used to make a POST Rest request.
        :param endpoint: the end point to be called (this is not the entire url but only the endpoint)
        :param data: the payload for the request
        :return: a list of response status code, body and url
        """

        # make the api call
        result = self.wcapi.post(endpoint, data)

        # extract the status code, the response body and the url from the response
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        """
        This method is used to make a GET Rest request
        :param endpoint: the end point to be called (this is not the entire url but only the endpoint)
        :return: a list of response status code, body and url
        """

        # make the api call
        result = self.wcapi.get(endpoint)

        # extract the status code, the response body and the url from the response
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

x = REQ()
x.test_api()