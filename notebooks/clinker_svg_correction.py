import argparse
import json
import logging
from lxml import etree

log_format = "%(levelname)-8s %(asctime)s   %(message)s"
date_format = "%d/%m %H:%M:%S"
logging.basicConfig(format=log_format, datefmt=date_format, level=logging.DEBUG)

def correct_svg_colors(svg_file, json_file, output_file):
    """
    This function correct the fill color of 'genePolygon' elements in a clinker SVG file
    based on a provided color map from a clinker JSON session file.

    Parameters:
    svg_file (str): The path to the input SVG file.
    json_file (str): The path to the JSON file containing the color map.
    output_file (str): The path to the output SVG file.
    """

    logging.info('Loading color map from JSON file...')
    # Load the color map from the JSON file
    with open(json_file, "r") as f:
        data = json.load(f)

    color_map = {}
    for group in data["groups"]:
        label = group["label"]
        colour = group["colour"]
        for gene in group["genes"]:
            color_map[gene] = {"colour" : colour, "label" : label}

    logging.info('Parsing SVG file...')
    # Parse the SVG file
    tree = etree.parse(svg_file)

    # Get the root of the SVG file
    root = tree.getroot()

    logging.info('Correcting colors...')
    # Iterate over all 'gene' elements
    for gene in root.findall(".//*[@class='gene']"):
        uid = gene.attrib["id"].split("gene_")[-1]
        child_element = gene.getchildren()
        for child in child_element:
            if 'genePolygon' in str(child.attrib["class"]):
                color = child.attrib['fill']
            if 'geneLabel' in str(child.attrib["class"]):
                label = child.text
        if color != color_map[uid]["colour"]:
            # Replace the fill color with the color from the colormap
            logging.warning(f"Color mismatch found in: {uid} {label}")
            for child in child_element:
                if 'genePolygon' in str(child.attrib["class"]):
                    child.attrib['fill'] = color_map[uid]["colour"]

    logging.info(f'Writing modified SVG to output file: {output_file}')
    # Write the modified tree back to the SVG file
    tree.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify clinker SVG colors based on a color map from a clinker JSON session file.')
    parser.add_argument('svg_file', type=str, help='The path to the clinker input SVG file.')
    parser.add_argument('json_file', type=str, help='The path to the JSON session file containing the color map.')
    parser.add_argument('output_file', type=str, help='The path to the output SVG file.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    correct_svg_colors(args.svg_file, args.json_file, args.output_file)