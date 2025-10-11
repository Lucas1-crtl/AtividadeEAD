import pytest
from django.urls import reverse


def test_rota_retorna_home() :
        url = reverse('home')
        assert url == '/'
        
