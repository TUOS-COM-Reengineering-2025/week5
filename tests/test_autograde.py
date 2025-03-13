import os

def test_result():
    assert os.path.exists("findings.md"), 'Cannot find findings.md'
    assert os.path.getsize("findings.md") > 100, 'Your report is too short.'
