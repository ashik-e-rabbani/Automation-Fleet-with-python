import pytest

class TestExample:
    """
    Example test class with various pytest markers.
    """

    @pytest.mark.skip(reason="Test is skipped unconditionally.")
    def test_skip_example(self):
        """
        This test is skipped unconditionally.
        """
        assert True

    @pytest.mark.skipif(True, reason="Test is skipped conditionally.")
    def test_skipif_example(self):
        """
        This test is skipped conditionally based on the skipif condition.
        """
        assert True

    @pytest.mark.xfail(reason="Test is expected to fail.")
    def test_xfail_example(self):
        """
        This test is expected to fail.
        """
        assert False

    @pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
    def test_parametrize_example(self, input, expected):
        """
        Parametrized test with multiple input values and expected outcomes.
        """
        assert input * 2 == expected

    @pytest.mark.timeout(5)
    def test_timeout_example(self):
        """
        This test has a maximum execution time of 5 seconds.
        """
        # Test code with a timeout of 5 seconds

    @pytest.mark.smoke
    def test_custom_marker_example(self):
        """
        This test is categorized as a smoke test using a custom marker.
        """
        assert True

    @pytest.mark.authentication
    def test_grouping_example_1(self):
        """
        Test belonging to the 'authentication' group.
        """
        assert True

    @pytest.mark.authentication
    def test_grouping_example_2(self):
        """
        Another test belonging to the 'authentication' group.
        """
        assert True
