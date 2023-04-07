from pkg_wordslookup.pkg_wordslookup import words_lookup

def test_words_lookup():
    """Test words lookup"""
    expected = "1 prueba de contadores\n2 prueba de impresion\n3 prueba de pkg\n5 prueba geral\n7 prueba arr\nThe word \"prueba\" appeared 5 times"
    #path = """E:\Projects\ProjectsPython\pkg_wordslookup\\tests\\test_txt.txt"""
    print(expected)
    actual = words_lookup("E:\\Projects\\ProjectsPython\\pkg_wordslookup\\tests\\test_txt.txt","prueba")
    assert actual == expected, "test_txt file processed incorrectly"