* Handle error caused by creating a new coupon with an existing coupon code
* Coupon & User doesn't get deleted via the celery tasks
* Strike webhook doesn't work because of incorrect params due to API changes
* Make changes to the mock API test call for upcoming invoice
* Make changes to tests/billing/test_models/TestInvoice/test_parse_payload_from_event