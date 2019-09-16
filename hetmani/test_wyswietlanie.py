from hetmani.wyswietlanie import wyswietl_hetmanow


def test_proste_wyswietlanie():
    assert wyswietl_hetmanow([0]) == "H       \n"
    assert wyswietl_hetmanow([1]) == " H      \n"
    assert wyswietl_hetmanow([2]) == "  H     \n"
    assert wyswietl_hetmanow([3]) == "   H    \n"
    assert wyswietl_hetmanow([0, 3]) == "H       \n   H    \n"