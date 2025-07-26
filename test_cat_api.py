import pytest
import requests
from unittest.mock import patch, Mock
from cat_api import get_random_cat_image

def test_successful_request():
    """Тест успешного запроса."""
    # Создаем мок-ответ с полной структурой
    mock_response = Mock()
    mock_response.json.return_value = [{"url": "https://example.com/cat.jpg"}]
    mock_response.raise_for_status.return_value = None
    mock_response.ok = True

    with patch('requests.get', return_value=mock_response):
        url = get_random_cat_image()
        assert url == "https://example.com/cat.jpg"

def test_failed_request():
    """Тест неуспешного запроса."""

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_response.ok = False

    with patch('requests.get', return_value=mock_response):
        url = get_random_cat_image()
        assert url is None

