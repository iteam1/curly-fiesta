from curly_fiesta.cli import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "curly fiesta!\n"
