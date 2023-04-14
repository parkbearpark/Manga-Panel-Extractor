# stdlib
import argparse
from argparse import RawTextHelpFormatter
import cv2
# project
from PanelExtractor.PanelExtractor import PanelExtractor


def main(args):
    panel_extractor = PanelExtractor(
        keep_text=args.keep_text, min_pct_panel=args.min_panel, max_pct_panel=args.max_panel)
    panels = panel_extractor.extract(args.input_folder)
    for key, imgs in panels.items():
        cnt = 0
        for img in imgs:
            cv2.imwrite(f"./output/{key}_{cnt}.png", img)
            cnt += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Implementation of a Manga Panel Extractor and dialogue bubble text eraser.",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument("-kt", "--keep_text", action='store_true',
                        help="Do not erase the dialogue bubble text.")
    parser.add_argument("-minp", "--min_panel", type=int, choices=range(1, 99), default=2, metavar="[1-99]",
                        help="Percentage of minimum panel area in relation to total page area.")
    parser.add_argument("-maxp", "--max_panel", type=int, choices=range(1, 99), default=90, metavar="[1-99]",
                        help="Percentage of minimum panel area in relation to total page area.")
    parser.add_argument("-i", '--input_folder', default='./images/', type=str,
                        help="""folder path to input manga pages.""")

    args = parser.parse_args()
    main(args)
