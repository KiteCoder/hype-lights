from django.http import JsonResponse
from hypertron import show_builder
from django.shortcuts import render, redirect
from xml.dom import minidom

def path_extracter():

    svg_file = "/static/Regions_de_France.svg"
    # svg_file = "filename"

    doc = minidom.parse(svg_file)  # parseString also exists
    path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
    doc.unlink()

    print('the url worked')

    print(path_strings)

    return path_strings