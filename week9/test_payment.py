from unittest.mock import Mock
from payment import OrderProcessor

def test_order_processing():
    fakeGateway = Mock()
    fakeGateway.charge.return_value = "SUCCESS-12345"

    processor =OrderProcessor(fakeGateway)
    result = processor.process(100)

    assert result == "Order processed: SUCCESS-12345"