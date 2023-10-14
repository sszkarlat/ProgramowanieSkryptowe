import cut


def test_cut(capsys):
    options = ["-d", ":", "-f", "1"]
    inputData = ["ol:pol:gol", "fis:cis:mis", "jop:pop:do", "dd:ss:zz"]

    cut.cut(options, inputData)
    out, err = capsys.readouterr()
    assert out == "ol\nfis\njop\ndd\n"
