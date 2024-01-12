#!/usr/bin/python
import os
import sys
import glob

def buildpdf1(filename):
    os.makedirs("pdf1")
    os.chdir("pdf1")
    os.system("pdflatex ../" + filename)
    os.chdir("../")

def buildpdf2(filename):
    os.makedirs("pdf2")
    os.chdir("pdf2")
    os.system("texliveonfly ../" + filename)
    os.chdir("../")

def buildhtml1(filename):
    os.makedirs("html1")
    os.chdir("html1")
    os.system("htlatex ../" + filename)
    os.chdir("../")

def buildhtml2(filename):
    os.makedirs("html2")
    os.chdir("html2")
    os.system("latex2html ../" + filename + " -dir $(pwd)")
    os.chdir("../")

def buildhtml3(filename):
    os.makedirs("html3")
    os.chdir("html3")
    os.system("make4ht ../" + filename + " \"mathjax\"")
    os.chdir("../")

def buildFile(file):
    print("Building tex file: ", file)
    name = file.rsplit(".", 1)[0]
    os.makedirs("build/" + name)
    os.chdir("build/" + name)
    buildpdf1("../../" + file)
    buildpdf2("../../" + file)
    buildhtml1("../../" + file)
    buildhtml2("../../" + file)
    buildhtml3("../../" + file)
    os.chdir("../../")

filenames = glob.glob("*.tex")
for file in filenames:
    buildFile(file)

