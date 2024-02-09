import os
import pytest
from project import write_to_pdf

def test_write_to_pdf(tmp_path):

    text = "Text to write to PDF"
    pdf_path = tmp_path / "output.pdf"

    write_to_pdf(text, str(pdf_path))

    assert pdf_path.exists()

    os.remove(pdf_path)

def test_write_new_to_pdf(tmp_path):

    text = "A situation happened at work today that I can’t get out of my head"
    pdf_path = tmp_path / "output.pdf"

    write_to_pdf(text, str(pdf_path))

    assert pdf_path.exists()

    os.remove(pdf_path)

def test_write_new_to_pdf(tmp_path):

    text = ""
    pdf_path = tmp_path / "output.pdf"

    write_to_pdf(text, str(pdf_path))

    assert pdf_path.exists()

    os.remove(pdf_path)
