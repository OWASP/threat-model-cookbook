# https://github.com/izar/pytm
from pytm import (
    TM, Server, Dataflow, Boundary, Actor, ExternalEntity, Process
)

payment_online = TM("stripe")
payment_online.description = "stripe payment"
payment_online.isOrdered = True
payment_online.mergeResponses = True

Customer_Client_Web = Boundary("Customer/Internet")
Merchant_Web = Boundary("Merchant/Web")
Stripe_API = Boundary("Stripe/Web")

customer = Actor("Customer")

customer_client = ExternalEntity("Customer Client")
customer_client.inBoundary = Customer_Client_Web
# user.levels = [2]

merchant_web = Server("Merchant Web Server")
merchant_web.inBoundary = Merchant_Web
merchant_web.OS = "Ubuntu"
merchant_web.isHardened = True
merchant_web.onAWS = True
# web.levels = [2]

stripe_api = ExternalEntity("Stripe API service")
stripe_api.inBoundary = Stripe_API
stripe_api.onAWS = False

stripe_process = Process("Stripe Payment Service")
stripe_process.inBoundary = Stripe_API

customer_to_customer_client = Dataflow(customer, customer_client, "Customer logs into the merchant site (*)")
customer_to_customer_client.protocol = "HTTPS"
customer_to_customer_client.dstPort = 443
customer_to_customer_client.data = 'OAuth'

customer_to_customer_client = Dataflow(customer, customer_client, "Customer proceeds to payment page to make a purchase (*)")
customer_to_customer_client.protocol = "HTTPS"
customer_to_customer_client.dstPort = 443

customer_client_to_merchant_web = Dataflow(customer_client, merchant_web, "Customer Client sends order intent, including order amount (*)")
customer_client_to_merchant_web.protocol = "HTTPS"
customer_client_to_merchant_web.dstPort = 443

merchant_web_to_stripe_api = Dataflow(merchant_web, stripe_api, "Merchant sends order information inc amount and currency (*)")
merchant_web_to_stripe_api.data = 'POST /v1/payment_intents'

stripe_api_to_merchant_web = Dataflow(stripe_api, merchant_web, "Return PaymentIntent to the Merchant (*)")
stripe_api_to_merchant_web.data = 'Response'
stripe_api_to_merchant_web.responseTo = merchant_web_to_stripe_api

merchant_web_to_customer_client = Dataflow( merchant_web, customer_client, "Return PaymentIntent to the Customer Client (*)")
merchant_web_to_customer_client.data = 'merchant_secret'
merchant_web_to_customer_client.responseTo = customer_client_to_merchant_web

customer_to_customer_client = Dataflow(customer, customer_client, "Customer provides card details and finalizes payment (*)")

customer_client_to_stripe_api = Dataflow(customer_client, stripe_api, "Customer Client sends stripe.confirmCardPayment() (*)")
customer_client_to_stripe_api.data = "client_secret and card details"

stripe_api_to_stripe_process = Dataflow(stripe_api, stripe_process, "Attempt payment")
stripe_process_to_stripe_api = Dataflow(stripe_process, stripe_api, "Payment Response")

stripe_api_to_customer_client = Dataflow(stripe_api, customer_client, "Return the PaymentIntent with status (*)")
stripe_api_to_customer_client.data = "Return the PaymentIntent with status 'succeeded'"

payment_online.process()