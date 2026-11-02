from unittest.mock import Mock

def test_comparison():
 mock = Mock()

 def fetch(value):
  return value.upper()
 mock.fetch.side_effect = fetch




 assert mock.fetch() == "STATIC"
 assert mock.fetch() == "STATIC"
 assert mock.fetch() == "STATIC"

 print(mock.fetch("hello"))