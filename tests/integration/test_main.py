from curly_fiesta.cli import main
from curly_fiesta.utils import greet


def test_full_flow(capsys, sample_name):
    main()
    captured = capsys.readouterr()
    assert "curly fiesta!" in captured.out
    assert greet(sample_name) == f"Hello, {sample_name}!"
