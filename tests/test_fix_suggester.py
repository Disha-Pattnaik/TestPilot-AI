from testpilot.fixes.fix_suggester import suggest_fix


def test_assertion_error():

    result = suggest_fix("AssertionError")

    assert "suggestion" in result
    assert "assertion" in result["suggestion"].lower()


def test_import_error():

    result = suggest_fix("ImportError")

    assert "suggestion" in result
    assert "import" in result["suggestion"].lower()


def test_unknown_error():

    result = suggest_fix("SomeUnknownError")

    assert "suggestion" in result
    assert len(result["suggestion"]) > 0