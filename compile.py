import os
import subprocess

PDFLATEX_PATH = r"D:\miktex\miktex\bin\x64\pdflatex.exe"
AUX_EXTENSIONS = [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"]


def compile_latex_to_pdf():
    tex_file = "resume.tex"
    output_pdf = "Het_Bhalani_Resume.pdf"

    subprocess.run([PDFLATEX_PATH, "-interaction=nonstopmode", tex_file], check=True)

    if not os.path.exists("resume.pdf"):
        raise FileNotFoundError("resume.pdf not generated")

    if os.path.exists(output_pdf):
        os.remove(output_pdf)
    os.rename("resume.pdf", output_pdf)

    for ext in AUX_EXTENSIONS:
        file_name = "resume" + ext
        if os.path.exists(file_name):
            os.remove(file_name)


if __name__ == "__main__":
    compile_latex_to_pdf()